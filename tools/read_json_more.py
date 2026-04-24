#导包
import json

#打开JSON，获取文件流
# with open("../data/login.json","r",encoding="utf-8") as f:
#     #调用load方法
#     data=json.load(f)
#     print("导入结果为：",data)

# def read_json(filename):
#     with open("../data/" + filename, "r", encoding="utf-8") as f:
#         # 调用load方法
#         return json.load(f)
class ReadJson(object):
    def __init__(self,filename):
        self.filepath = "../data/" + filename
    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法
            return json.load(f)
'''
self相当于往这个类上添加自身属性，可以永远存储，并且带着走，其他方法只需要传入self参数便
可以使用
'''
if __name__ == '__main__':
    #为了运用param必须调整格式
    arrs=[]
    datas=ReadJson("login_more.json").read_json()
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")
                     ))
    print(arrs)