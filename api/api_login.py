import requests

class ApiLogin():
    def api_post_login(self,url,data,headers):
        #定义数据
        headers={
            "Content-Type": "application/json"
        }
        data={"mobile" : "12011111111","code" : "246810"}
        return requests.post(url=url,json=data,headers=headers)



