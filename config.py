from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.environ.get("VK_SERVICE_KEY")
VK_USER_GET_ULR = "https://api.vk.com/method/users.get"
VK_SUBSCRIPTION_URL = "https://api.vk.com/method/users.getSubscriptions"
VK_WALL_URL = "https://api.vk.com/method/wall.get"
VK_WALL_URL_GBI = "https://api.vk.com/method/wall.getById"
