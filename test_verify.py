from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.用户名验证唯一性[参数空值提交]
def test_username1():
    test_username1 = inter.username(
        username = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.用户名验证唯一性[参数空值提交]",test_username1,test_username1.text)
    print("="*100)
# test_username1()
    assert str(test_username1.status_code) == "400"
#2.用户名验证唯一性[参数正则提交]
def test_username2():
    test_username2 = inter.username(
        username = "mingv"+str(random.randint(0,999)), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.用户名验证唯一性[参数正则提交]",test_username2,test_username2.json())
    print("="*100)
# test_username2()
    assert str(test_username2.json()['exist']) == "False"
#3.用户名验证唯一性[参数已存在提交]
def test_username3():
    test_username3 = inter.username(
        username = "zhangmingwei", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.用户名验证唯一性[参数已存在提交]",test_username3,test_username3.json())
    print("="*100)
# test_username3()
    assert str(test_username3.json()['exist']) == "True"
#4.email验证唯一性[参数空值提交]
def test_email1():
    test_email1 = inter.email(
        email = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.email验证唯一性[参数空值提交]",test_email1,test_email1.text)
    print("="*100)
# test_email1()
    assert str(test_email1.status_code) == "400"
#5.email验证唯一性[参数正则提交]
def test_email2():
    test_email2 = inter.email(
        email = "mingv"+str(random.randint(0,999))+"@email.co", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.email验证唯一性[参数正则提交]",test_email2,test_email2.json())
    print("="*100)
# test_email2()
    assert str(test_email2.json()['exist']) == "False"
#6.email验证唯一性[参数已存在提交]
def test_email3():
    test_email3 = inter.email(
        email = "zhangmingwei@zhangmingwei.com", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.email验证唯一性[参数已存在提交]",test_email3,test_email3.json())
    print("="*100)
# test_email3()
    assert str(test_email3.json()['exist']) == "True"

