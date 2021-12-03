from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取transferred订单[参数空值提交]
def test_transferred1():
    test_transferred1 = inter.transferred(
        pageSize = "", 
        page = "", 
        status = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取transferred订单[参数空值提交]",test_transferred1,test_transferred1.text)
    print("="*100)
# test_transferred1()
    assert str(test_transferred1.status_code) == "400"
#2.获取transferred订单[参数Status提交]
def test_transferred2():
    test_transferred2 = inter.transferred(
        pageSize = 1, 
        page = 1, 
        status = 2, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取transferred订单[参数Status提交]",test_transferred2,test_transferred2.json())
    print("="*100)
# test_transferred2()
    assert str(test_transferred2.status_code) == "200"
#3.获取transferred订单[参数正则提交]
def test_transferred3():
    test_transferred3 = inter.transferred(
        pageSize = 10, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.获取transferred订单[参数正则提交]",test_transferred3,test_transferred3.json())
    print("="*100)
# test_transferred3()
    assert str(test_transferred3.status_code) == "200"
#4.获取transferred订单[参数空值提交]
def test_transferredDocid1():
    test_transferredDocid1 = inter.transferredDocid(
        doc_id = "", 
        pageSize = "", 
        page = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.获取transferred订单[参数空值提交]",test_transferredDocid1,test_transferredDocid1.text)
    print("="*100)
# test_transferredDocid1()
    assert str(test_transferredDocid1.status_code) == "404"
#5.获取transferred订单[参数正则提交]
def test_transferredDocid2():
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
    test_transferredDocid2 = inter.transferredDocid(
        doc_id = doc_idTransferred, 
        pageSize = 100, 
        page = 1, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.获取transferred订单[参数空值提交]",test_transferredDocid2,test_transferredDocid2.text)
    print("="*100)
# test_transferredDocid2()
    assert str(test_transferredDocid2.status_code) == "200"