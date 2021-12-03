import json
from TestInterface import Interface
from Common import GBK2312, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取产品列表[参数空值提交]
def test_products1():
    test_products1 = inter.products(
        pageSize = "", 
        page = "", 
        search = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取产品列表[参数空值提交]",test_products1)
    print("="*100)
# test_products1()
    assert str(test_products1.status_code) == "400"
#2.获取产品列表[参数Search提交]
def test_products2():
    test_products2 = inter.products(
        pageSize = 1, 
        page = 1, 
        search = "STK113", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取产品列表[参数Search提交]",test_products2.json())
    print("="*100)
# test_products2()
    assert str(test_products2.status_code) == "200"
#3.获取产品列表[参数正则提交]
def test_products3():
    test_products3 = inter.products(
        pageSize = 10, 
        page = 1, 
        search = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.获取产品列表[参数正则提交]",test_products3.json())
    print("="*100)
# test_products3()
    assert str(test_products3.status_code) == "200"
#4.修改产品图片[参数空值提交]
def test_productsCode1():
    test_productsCode1 = inter.productsCode(
        code = "", 
        img = [], 
        name = "",
        net_price = "",
        qty = "",
        type = "",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.修改产品图片[参数空值提交]",test_productsCode1)
    print("="*100)
# test_productsCode1()
    assert str(test_productsCode1.status_code) == "404"
#5.修改产品图片[参数正则提交]
def test_productsCode2():
    test_productsCode2 = inter.productsCode(
        code = "STK113", 
        img = ["https://ezx-test.oss-cn-hongkong.aliyuncs.com/products/STK113/2021-12-03_011339_zhangmingwei"], 
        name = "30CM x 10 METER LAMP STICKER (LIGHT BLACK)(EZ)*  ",
        net_price = "38.00",
        qty = "0",
        type = "C",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.修改产品图片[参数正则提交]",test_productsCode2.json())
    print("="*100)
# test_productsCode2()
    assert str(test_productsCode2.status_code) == "200"
#6.获取oss授权[参数空值提交]
def test_oss1():
    test_oss1 = inter.oss(
        userDir = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("6.获取oss授权[参数空值提交]",test_oss1.json())
    print("="*100)
# test_oss1()
    assert str(test_oss1.status_code) == "200"
#7.获取oss授权[参数正则提交]
def test_oss2():
    test_oss2 = inter.oss(
        userDir = "products/STK113", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#7.获取oss授权[参数正则提交]",test_oss2.json())
    print("="*100)
# test_oss2()
    assert str(test_oss2.status_code) == "200"