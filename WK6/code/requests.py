import requests 
import json 

"""
1. GET Request
   ```sh
   curl https://jsonplaceholder.typicode.com/posts/1
   ```
   
2. POST Request
   ```sh
   curl -X POST https://jsonplaceholder.typicode.com/posts -H "Content-Type: application/json" -d '{"title": "foo", "body": "bar", "userId": 1}'
   ```
---

3. PUT Request
   ```sh
   curl -X PUT https://jsonplaceholder.typicode.com/posts/1 -H "Content-Type: application/json" -d '{"id": 1, "title": "foo", "body": "bar", "userId": 1}'
   ```

4. DELETE Request
   ```sh
   curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
   ```
"""

# GET Request

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())

# GET Request with parameters

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts", 
    params={"userId": 1}
)
print(response.status_code)
print(response.json())

# Or can include the parameters in the URL

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts?userId=1"
)
print(response.status_code)
print(response.json())


# POST Request

response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "foo", "body": "bar", "userId": 1})
print(response.status_code)
print(response.json())

# PUT Request

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={"id": 1, "title": "foo", "body": "bar", "userId": 1})
print(response.status_code)
print(response.json())

# DELETE Request

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())



