from api.api_login import ApiLogin
import unittest
from parameterized import parameterized
from tools.read_json import ReadJson
def get_data():
    arrs = []
    datas = ReadJson("login_more.json").read_json()
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")
                     ))
    return arrs

class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_longin(self,url,mobile,code,expect_result,status_code):
        # # 暂时存放数据 url mobile code
        # url = "https://api-toutiao-web.itheima.net/mp/v1_0/authorizations"
        # mobile = "12011111111"
        # code = "246810"
        res = ApiLogin().api_post_login(url,mobile,code)
        #查看响应结果
        print("返回数据结果为",res.json())
        #断言响应数据
        # self.assertEqual("OK",res.json()["message"])
        self.assertEqual(expect_result, res.json()["message"])
        # self.assertEqual(201,res.status_code)
        self.assertEqual(status_code, res.status_code)

if __name__ == '__main__':
    unittest.main()