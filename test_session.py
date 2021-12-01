from TestInterface import Interface
from Common import TimeNow

inter = Interface()
Random = TimeNow()

#1.登录step-1 验证用户名密码[空值提交]
def test_verify_1():
    test_verify_1 = inter.verify(
        username = "", 
        password = "", 
        platform = "admin"
    )
    print("="*100)
    print("#1.登录step-1 验证用户名密码[空值提交]:",test_verify_1.json())
    print("="*100)
#test_verify_1()
    assert str(test_verify_1.json()['code']) == "401.2"