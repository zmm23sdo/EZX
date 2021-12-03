from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取in-app订单列表[参数空值提交]
def test_app1():
    test_app1 = inter.app(
        pageSize = "", 
        page = "", 
        status = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取in-app订单列表[参数空值提交]",test_app1,test_app1.text)
    print("="*100)
# test_app1()
    assert str(test_app1.status_code) == "400"
#2.获取in-app订单列表[参数Status提交]
def test_app2():
    test_app2 = inter.app(
        pageSize = 1, 
        page = 1, 
        status = 1, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取in-app订单列表[参数Status提交]",test_app2,test_app2.json())
    print("="*100)
# test_app2()
    assert str(test_app2.status_code) == "200"
#3.获取in-app订单列表[参数正则提交]
def test_app3():
    test_app3 = inter.app(
        pageSize = 10, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.获取in-app订单列表[参数正则提交]",test_app3,test_app3.json())
    print("="*100)
# test_app3()
    assert str(test_app3.status_code) == "200"
#4.app订单详情[参数空值提交]
def test_confirmedDocidApp1():
    test_confirmedDocidApp1 = inter.confirmedDocidApp(
        doc_id = "", 
        pageSize = "", 
        page = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.app订单详情[参数空值提交]",test_confirmedDocidApp1)
    print("="*100)
# test_confirmedDocidApp1()
    assert str(test_confirmedDocidApp1.status_code) == "404"
#5.app订单详情[参数正则提交]
def test_confirmedDocidApp2():
    appGet = inter.app(
        pageSize = 10, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idAPP = str(appGet.json()['detail'][0]['doc_id'])
    print("="*100)
    print("#获取in-app订单列表",appGet.json())
    print("doc_idAPP",doc_idAPP)
    print("="*100)
    test_confirmedDocidApp2 = inter.confirmedDocidApp(
        doc_id = doc_idAPP, 
        pageSize = 100, 
        page = 1, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.app订单详情[参数正则提交]",test_confirmedDocidApp2)
    print("="*100)
# test_confirmedDocidApp2()
    assert str(test_confirmedDocidApp2.status_code) == "200"
