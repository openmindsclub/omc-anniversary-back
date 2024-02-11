from requests import post


URI = "http://127.0.0.1:8000"
#URI = "https://zaqksdev.pythonanywhere.com"
POST = {
    "name":"zak2",
    "phonenum":"0799999906",
    "email":"zak22@gmail.com",
    "year":"2015"
    }


def postFunc(uri, data):
    response  =post(uri, data)
    print(response.json())

    return response



postFunc(URI, POST)
