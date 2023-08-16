Данный проект реализует JSON API для получения данных открытого и публичного профиля VK.

### Stack
* Python 3.11
* FastAPI
* Redis
* Docker

### Запуск
1. Установите Docker или Docker-desktop, если он еще не установлен.

2. Клонируйте репозиторий в заранее созданную папку

```bash
cd <folder_name>
git clone ...
```

3. В VK создайте Сайт - приложение и в настройках приложения получите сервисный ключ доступа.
4. Переименуйте .env-sample в .env и заполните его полученным ключом.
5. Перейдите в папку проекта и запустите docker-compose

```bash
docker-compose up --build
```

### Инструкция по использованию API

1. Перейдите на http://localhost:8000/docs
2. В endpoint `likes` введите ссылку на пост в VK в поле `link`, например: https://vk.com/wall3460930_218216 <br>
Ответ:
```
{
  "status": "success",
  "code": 200,
  "data": {
    "post_id": "3460930_218216",
    "url": "https://vk.com/wall3460930_218216",
    "likes": "280",
    "share": "26",
    "views": "120646"
  }
}
```
3. Перейдите в endpoint `profile-data` и введите username или id пользователя,
в методе напишите `profile` и выполните запрос <br>
Ответ:
```
{
  "status": "success",
  "code": 200,
  "data": {
    "profile_id": "3460930",
    "avatar_url": "https://sun6-21.userapi.com/s/v1/ig2/bxhGgm_Qp45lF4TAJFzXJmOph7q0lvHWynIcdGR4YlkOgwVRPPBk8ekT7rru5MS8KBP1TtuSmploJi4U4MzxWDOX.jpg?size=400x400&quality=96&crop=165,0,792,792&ava=1",
    "followers": "117267",
    "following": "23"
  }
}
```

4. В том же endpoint `profile-data` измените метод на posts и выполните запрос <br>
Ответ:
```
{
  "status": "success",
  "code": 200,
  "data": {
    "profile_id": "3460930",
    "avatar_url": "https://sun6-21.userapi.com/s/v1/ig2/bxhGgm_Qp45lF4TAJFzXJmOph7q0lvHWynIcdGR4YlkOgwVRPPBk8ekT7rru5MS8KBP1TtuSmploJi4U4MzxWDOX.jpg?size=400x400&quality=96&crop=165,0,792,792&ava=1",
    "posts": [
      {
        "post_id": "3460930_218216",
        "url": "https://vk.com/wall3460930_218216",
        "likes": "280",
        "share": "26",
        "views": "120646"
      },
      {
        "post_id": "3460930_228831",
        "url": "https://vk.com/wall3460930_228831",
        "likes": "598",
        "share": "91",
        "views": "72575"
      },
      {
        "post_id": "3460930_218189",
        "url": "https://vk.com/wall3460930_218189",
        "likes": "149",
        "share": "12",
        "views": "52383"
      },
      {
        "post_id": "3460930_218187",
        "url": "https://vk.com/wall3460930_218187",
        "likes": "79",
        "share": "4",
        "views": "34792"
      },
      {
        "post_id": "3460930_218134",
        "url": "https://vk.com/wall3460930_218134",
        "likes": "195",
        "share": "15",
        "views": "39989"
      },
      {
        "post_id": "3460930_218080",
        "url": "https://vk.com/wall3460930_218080",
        "likes": "154",
        "share": "6",
        "views": "32549"
      },
      {
        "post_id": "3460930_218015",
        "url": "https://vk.com/wall3460930_218015",
        "likes": "2498",
        "share": "12",
        "views": "43814"
      },
      {
        "post_id": "3460930_218014",
        "url": "https://vk.com/wall3460930_218014",
        "likes": "88",
        "share": "4",
        "views": "22476"
      },
      {
        "post_id": "3460930_218009",
        "url": "https://vk.com/wall3460930_218009",
        "likes": "83",
        "share": "17",
        "views": "20057"
      },
      {
        "post_id": "3460930_218005",
        "url": "https://vk.com/wall3460930_218005",
        "likes": "51",
        "share": "0",
        "views": "15072"
      }
    ]
  }
}
```
