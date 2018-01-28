import requests

var = 0

response = requests.get(
    url = "http://127.0.0.1:5000/api/" + str(2) + "/" + str(6) + "/" + str(1) + "/" + str(8)
    #url = "http://localhost:5000/api/" + str(var)
)

print(response.status_code)
print(response.content)
