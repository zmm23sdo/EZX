import json
from TestInterface import Interface
from Common import GBK2312, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取顾客列表[参数空值提交]
def test_customers1():
    test_customers1 = inter.customers(
        pageSize = "", 
        page = "", 
        search = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取顾客列表[参数空值提交]",test_customers1)
    print("="*100)
# test_customers1()
    assert str(test_customers1.status_code) == "400"
#2.获取顾客列表[参数Search提交]
def test_customers2():
    test_customers2 = inter.customers(
        pageSize = 1, 
        page = 1, 
        search = "300-W025", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取顾客列表[参数Search提交]",test_customers2.json())
    print("="*100)
# test_customers2()
    assert str(test_customers2.status_code) == "200"
#3.获取顾客列表[参数正则提交]
def test_customers3():
    test_customers3 = inter.customers(
        pageSize = 100, 
        page = 1, 
        search = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.获取顾客列表[参数正则提交]",test_customers3.json())
    print("="*100)
# test_customers3()
    assert str(test_customers3.status_code) == "200"
#4.获取顾客信息[参数空值提交]
def test_customersCode1():
    test_customersCode1 = inter.customersCode(
        code = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.获取顾客信息[参数空值提交]",test_customersCode1)
    print("="*100)
# test_customersCode1()
    assert str(test_customersCode1.status_code) == "404"
#5.获取顾客信息[参数错误提交]
def test_customersCode2():
    test_customersCode2 = inter.customersCode(
        code = "不存在", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.获取顾客信息[参数错误提交]",test_customersCode2)
    print("="*100)
# test_customersCode2()
    assert str(test_customersCode2.status_code) == "404"
#6.获取顾客信息[参数正则提交]
def test_customersCode3():
    test_customersCode3 = inter.customersCode(
        code = "300-W025", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#6.获取顾客信息[参数正则提交]",test_customersCode3.json())
    print("="*100)
# test_customersCode3()
    assert str(test_customersCode3.status_code) == "200"