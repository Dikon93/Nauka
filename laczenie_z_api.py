import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if (response.status_code != requests.codes.ok):
    print("Coś nie tak")
else:
    print(response.json())

requestBody = {
    "title": "Naszy tytuł",
    "body": "Treśc posta",
    "userID": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=requestBody)

if (response.status_code != requests.codes.created):
    print("Coś nie tak")
else:
    print(response.json())
