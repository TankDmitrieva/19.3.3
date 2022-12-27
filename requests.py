import requests
import json
email = "trugal@mail.ru"
passw = "12345"
base_url = "https://petfriends.skillfactory.ru/"
headers_get_api = {
            'email': email,
            'password': passw,
            'accept': 'application/json'
        }
res_get_api_key = requests.get(base_url+'api/key', headers=headers_get_api)
print(res_get_api_key.json())

url_get = "https://petstore.swagger.io/v2/pet/findByStatus"
res_get = requests.get(f"{url_get}", params={'status': 'available'}, headers={'accept': 'application/json'})
print(res_get.text)
print(res_get.status_code)
info = {
    "id": 7325,
    "category": {"id": 2, "name": "Cat"},
    "name": "trustor",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "available"
}
url_post = "https://petstore.swagger.io/v2/pet"
res_post = requests.post(url_post, headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info, ensure_ascii=False))
print(res_post.text)
print(res_post.status_code)
info_put = {
    "id": 7325,
    "category": {"id": 2, "name": "Cat"},
    "name": "trustorer",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "available"
}
url_put = "https://petstore.swagger.io/v2/pet"
res_put = requests.put(url_put, headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                      data=json.dumps(info_put, ensure_ascii=False))
print(res_put.text)
print(res_put.status_code)
pet_id = "7325"
headers_del = res_get_api_key.json()
url_del = "https://petstore.swagger.io/v2/pet/"
res_del = requests.delete(url_del + pet_id, headers=headers_del)
print(res_del.text)
print(res_del.status_code)
