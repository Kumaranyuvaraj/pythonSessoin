import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}
todo1 = {"title":"car"}
response = requests.patch(url,json=todo1)
print(response.json())






