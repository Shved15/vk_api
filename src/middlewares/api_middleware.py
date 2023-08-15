import asyncio_redis
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class SingleRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        unique_key = f"{client_ip}"

        connection = await asyncio_redis.Connection.create(host='localhost', port=6379)

        is_active = await connection.get(unique_key)

        if is_active:
            return JSONResponse(content={"error": "Only one concurrent request allowed per IP"}, status_code=429)

        await connection.setex(unique_key, 10, '1')

        response = await call_next(request)

        connection.close()

        return response
