import asyncio_redis
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

REDIS_HOST = 'redis'
REDIS_PORT = 6379
KEY_EXPIRATION_TIME = 10
PROTECTED_ENDPOINTS = ["/api/v1/likes/", "/api/v1/profile-data/"]


class SingleRequestMiddleware(BaseHTTPMiddleware):

    @staticmethod
    async def is_concurrent_request(connection, client_ip, path):
        # Ключи для likes и profile-data
        likes_key = f"{client_ip}-/api/v1/likes/"
        profile_data_key = f"{client_ip}-/api/v1/profile-data/"

        likes_active = await connection.get(likes_key)
        profile_data_active = await connection.get(profile_data_key)

        return likes_active or profile_data_active

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        if request.url.path in PROTECTED_ENDPOINTS:
            connection = await asyncio_redis.Connection.create(host=REDIS_HOST, port=REDIS_PORT)

            if await self.is_concurrent_request(connection, client_ip, request.url.path):
                connection.close()
                return JSONResponse(content={"error": "Only one concurrent request allowed per IP for this endpoint"},
                                    status_code=429)

            # Устанавливаем ключ для текущего запроса
            current_key = f"{client_ip}-{request.url.path}"
            await connection.setex(current_key, KEY_EXPIRATION_TIME, '1')

            response = await call_next(request)

            connection.close()
            return response

        return await call_next(request)
