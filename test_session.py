from requests.sessions import session
from TestInterface import Interface
from Common import GBK2312, TimeNow, Unicode, loginOne, loginTwo
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
#2.登录step-1 验证用户名密码[参数错误提交]
def test_verify_2():
    test_verify_2 = inter.verify(
        username = GBK2312(), 
        password = Unicode(), 
        platform = "admin"
    )
    print("="*100)
    print("#2.登录step-1 验证用户名密码[参数错误提交]:",test_verify_2.json())
    print("="*100)
# test_verify_2()
    assert str(test_verify_2.json()['code']) == "401.2"
#3.登录step-1 验证用户名密码[参数不匹配提交]
def test_verify_3():
    test_verify_3 = inter.verify(
        username = "zmm23sdo", 
        password = "qwer1234", 
        platform = "admin"
    )
    print("="*100)
    print("#3.登录step-1 验证用户名密码[参数不匹配提交]",test_verify_3.json())
    print("="*100)
# test_verify_3()
    assert str(test_verify_3.json()['code']) == "401.2"
#4.登录step-1 验证用户名密码[参数正则提交]
def test_verify_4():
    test_verify_4 = inter.verify(
        username = "zhangmingwei", 
        password = "qwer1234", 
        platform = "admin"
    )
    print("="*100)
    print("#4.登录step-1 验证用户名密码[参数正则提交]",test_verify_4.json())
    print("#4.登录step-1 验证用户名密码[参数正则提交]",test_verify_4.status_code)
    print("="*100)
# test_verify_4()
    assert str(test_verify_4.status_code) == "200"


#5.登录step-2 获取登录凭证[参数空值提交]
def test_session_1():
    test_session_1 = inter.session(
        token = "", 
        company = ""
    )
    print("="*100)
    print("#5.登录step-2 获取登录凭证[参数空值提交]",test_session_1.json())
    print("="*100)
# test_session_1()
    assert str(test_session_1.json()['code']) == "400.1"
#6.登录step-2 获取登录凭证[参数错误提交]
def test_session_2():
    test_session_2 = inter.session(
        token = "abc", 
        company = "efg"
    )
    print("="*100)
    print("#6.登录step-2 获取登录凭证[参数错误提交]",test_session_2.json())
    print("="*100)
# test_session_2()
    assert str(test_session_2.json()['code']) == "400.1"
#7.登录step-2 获取登录凭证[参数正则提交]
def test_session_3():
    token = loginOne()
    print("token:",token)
    test_session_3 = inter.session(
        token = token, 
        company = 1
    )
    print("="*100)
    print("#7.登录step-2 获取登录凭证[参数正则提交]",test_session_3.json())
    print("="*100)
# test_session_3()
    assert str(test_session_3.status_code) == "200"
#8.使用refreshtoken获取新token[参数空值提交]
def test_sessionPut1():
    refresh_token = loginTwo()
    test_sessionPut1 = inter.sessionPut(
        refresh_token = "",
        headers = {'Authorization': refresh_token}
    )
    print("="*100)
    print("#8.使用refreshtoken获取新token[参数空值提交]",test_sessionPut1.json())
    print("="*100)
# test_sessionPut1()
    assert str(test_sessionPut1.json()['code']) == "401.5"
#9.使用refreshtoken获取新token[参数错误提交]
def test_sessionPut2():
    refresh_token = loginTwo()
    test_sessionPut2 = inter.sessionPut(
        refresh_token = "123",
        headers = {'Authorization': refresh_token}
    )
    print("="*100)
    print("#9.使用refreshtoken获取新token[参数错误提交]",test_sessionPut2.json())
    print("="*100)
# test_sessionPut2()
    assert str(test_sessionPut2.json()['code']) == "401.5"
#10.使用refreshtoken获取新token[参数正则提交]
def test_sessionPut3():
    refresh_token = loginTwo()
    test_sessionPut3 = inter.sessionPut(
        refresh_token = refresh_token,
        headers = {'Authorization': refresh_token}
    
    )
    print("="*100)
    print("#10.使用refreshtoken获取新token[参数正则提交]",test_sessionPut3.json())
    print("="*100)
# test_sessionPut3()
    assert str(test_sessionPut3.status_code) == "200"
