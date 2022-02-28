from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.客户下拉框列表[正则提交]
def test_customersGet():
    test_customersGet = inter.customersGet(
        headers =  {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#6.客户下拉框列表[正则提交]",test_customersGet,test_customersGet.json())
    print("="*100)
# test_customersGet()
    assert str(test_customersGet.status_code) == "200"
#2.销售员下拉列表[正则提交]
def test_agentGet():
    test_agentGet = inter.customersGet(
        headers =  {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#7.销售员下拉列表[正则提交]",test_agentGet,test_agentGet.json())
    print("="*100)
# test_agentGet()
    assert str(test_agentGet.status_code) == "200"
#3.产品下拉列表[Search提交]
def test_productsGet1():
    test_productsGet1 = inter.productsGet(
        search = "STK113",
        headers =  {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.产品下拉列表[Search提交]",test_productsGet1,test_productsGet1.json())
    print("="*100)
# test_productsGet1()
    assert str(test_productsGet1.status_code) == "200"
#4.产品下拉列表[正则提交]
def test_productsGet2():
    test_productsGet2 = inter.productsGet(
        search = None,
        headers =  {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.产品下拉列表[正则提交]",test_productsGet2,test_productsGet2.json())
    print("="*100)
# test_productsGet2()
    assert str(test_productsGet2.status_code) == "200"
#5.admin下拉列表[正则提交]
def test_adminGet():
    test_adminGet = inter.adminGet(
        headers =  {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.admin下拉列表[正则提交]",test_adminGet,test_adminGet.json())
    print("="*100)
# test_adminGet()
    assert str(test_adminGet.status_code) == "200"
