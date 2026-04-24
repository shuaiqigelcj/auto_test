import requests

class ApiPicture():
    def test_put_picture(self,url,headers):
        return requests.put(url=url,headers=headers)
