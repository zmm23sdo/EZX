from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取订单历史[参数空值提交]
def test_orderHistory1():
    test_orderHistory1 = inter.orderHistory(
        doc_id = "", 
        pageSize = "", 
        page = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取订单历史[参数空值提交]",test_orderHistory1,test_orderHistory1.text)
    print("="*100)
# test_orderHistory1()
    assert str(test_orderHistory1.status_code) == "404"
#2.获取订单历史[参数正则提交]
def test_orderHistory2():
    transferredGet = inter.transferred(
        pageSize = 100, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idTransferred = str(transferredGet.json()['detail'][0]['doc_id'])
    print("="*100)
    print("获取transferred订单",transferredGet,transferredGet.json())
    print("="*100)
    test_orderHistory2 = inter.orderHistory(
        doc_id = doc_idTransferred, 
        pageSize = 10, 
        page = 1, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取订单历史[参数正则提交]",test_orderHistory2,test_orderHistory2.json())
    print("="*100)
# test_orderHistory2()
    assert str(test_orderHistory2.status_code) == "200"