import requests


server_url = "http://localhost:8080"

get_response = requests.get(f"{server_url}/")
print("GET запрос:")
print(get_response.text)
print("="*50)

post_data = {"subject": "Math", "score": "5"}
post_response = requests.post(f"{server_url}/add_score", data=post_data)
print("POST запрос:")
print(post_response.text)
print("="*50)

get_response_after_post = requests.get(f"{server_url}/")
print("GET запрос после POST:")
print(get_response_after_post.text)

post_data = {"subject": "Chemistry", "score": "2"}
post_response = requests.post(f"{server_url}/add_score", data=post_data)
print("POST запрос:")
print(post_response.text)
print("="*50)

post_data = {"subject": "Physics", "score": "3"}
post_response = requests.post(f"{server_url}/add_score", data=post_data)
print("POST запрос:")
print(post_response.text)
print("="*50)

get_response_after_post = requests.get(f"{server_url}/")
print("GET запрос после ещё двух POST:")
print(get_response_after_post.text)

