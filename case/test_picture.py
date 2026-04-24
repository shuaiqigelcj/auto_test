from api.api_picture import ApiPicture
from parameterized import parameterized
import unittest
from tools.read_json import ReadJson

def get_data():
    arrs=[]
    data=ReadJson("login.json").read_json()
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")
                 ))
    return arrs



class TestPicture(unittest.TestCase):
    @parameterized.expand(get_data)
    def test_put_colpic(self,url,headers,expect_result,status_code):
        r = ApiPicture().test_put_picture(url=url,headers=headers)
        print("返回数据结果为", r.json())
        self.assertEqual(expect_result,r.json()["message"])
        self.assertEqual(status_code,r.status_code)

if __name__ == '__main__':
    unittest.main()
