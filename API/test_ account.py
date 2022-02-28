import json
from TestInterface import Interface
from Common import GBK2312, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取账户信息[正则提交]
def test_account():
    test_account = inter.account(
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取账户信息[正则提交]",test_account.json())
    print("="*100)
# test_account()
    assert str(test_account.status_code) == "200"
#2.修改账户信息[参数空值提交]
def test_accountEdit1():
    test_accountEdit1 = inter.accountEdit(
        email = "", 
        phone = "", 
        name = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.修改账户信息[参数空值提交]",test_accountEdit1.json())
    print("="*100)
# test_accountEdit1()
    assert str(test_accountEdit1.json()['code']) == "400.1"
#3.修改账户信息[参数错误提交]
def test_accountEdit2():
    test_accountEdit2 = inter.accountEdit(
        email = "ABC", 
        phone = "ABC", 
        name = "ABC", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.修改账户信息[参数错误提交]",test_accountEdit2.json())
    print("="*100)
# test_accountEdit2()
    assert str(test_accountEdit2.json()['code']) == "400.1"
#4.修改账户信息[参数正则提交]
def test_accountEdit3():
    test_accountEdit3 = inter.accountEdit(
        email = "zhangmingwei@zhangmingwei.com", 
        phone = TimeNow(), 
        name = "zhangmingwei", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.修改账户信息[参数正则提交]",test_accountEdit3.json())
    print("="*100)
# test_accountEdit3()
    assert str(test_accountEdit3.status_code) == "200"
#5.修改密码[参数空值提交]
def test_passwordAccount1():
    test_passwordAccount1 = inter.passwordAccount(
        password = "", 
        new_password = "", 
        confirm_password = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.修改密码[参数空值提交]",test_passwordAccount1.json())
    print("="*100)
# test_passwordAccount1()
    assert str(test_passwordAccount1.json()['code']) == "401.11"

#6.修改密码[参数错误提交]
def test_passwordAccount2():
    test_passwordAccount2 = inter.passwordAccount(
        password = "qwer`123", 
        new_password = "qwer`123", 
        confirm_password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#6.修改密码[参数错误提交]",test_passwordAccount2.json())
    print("="*100)
# test_passwordAccount2()
    assert str(test_passwordAccount2.json()['code']) == "401.4"
#7.修改密码[参数不匹配提交]
def test_passwordAccount3():
    test_passwordAccount3 = inter.passwordAccount(
        password = "qwer`123", 
        new_password = "qwer`123", 
        confirm_password = "qwer`1234", 
        headers = {'Authorization': loginOther()}
    )
    print("="*100)
    print("#7.修改密码[参数不匹配提交]",test_passwordAccount3.json())
    print("="*100)
# test_passwordAccount3()
    assert str(test_passwordAccount3.json()['code']) == "401.6"
#8.修改密码[参数正则提交]
def test_passwordAccount4():
    test_passwordAccount4 = inter.passwordAccount(
        password = "qwer`123", 
        new_password = "qwer`123", 
        confirm_password = "qwer`123", 
        headers = {'Authorization': loginOther()}
    )
    print("="*100)
    print("#8.修改密码[参数正则提交]",test_passwordAccount4.json())
    print("="*100)
# test_passwordAccount4()
    assert str(test_passwordAccount4.json()['code']) == "200"
