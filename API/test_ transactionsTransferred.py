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
#4.获取transferred订单详情[参数空值提交]
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
#5.获取transferred订单详情[参数正则提交]
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
    print("#5.获取transferred订单[参数正则提交]",test_transferredDocid2,test_transferredDocid2.text)
    print("="*100)
# test_transferredDocid2()
    assert str(test_transferredDocid2.status_code) == "200"
#6.取消transferred订单[参数空值提交]
def test_transferredCancel1():
    test_transferredCancel1 = inter.transferredCancel(
        doc_id = "", 
        reason = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#6.取消transferred订单[参数空值提交]",test_transferredCancel1,test_transferredCancel1.text)
    print("="*100)
# test_transferredCancel1()
    assert str(test_transferredCancel1.status_code) == "404"
#7.取消transferred订单[参数正则提交]
def test_transferredCancel2():
    confirmedAdd = inter.confirmedAdd(
        customer = "300-W003", 
        shop_name = "WAH PERFECT ZONE CAR AIR-COND & ACCESSORIES", 
        doc_date = Now(), 
        address = "NO. 52 PUSAT PERNIAGAAN KM 2 KM 2 JLN. LIPIS 27600 RAUB,PAHANG", 
        customer_name = "WAH", 
        credit_term = "90", 
        sales_agent = "RYAN", 
        code = "STK113", 
        name = "30CM x 10 METER LAMP STICKER (LIGHT BLACK)(EZ)* ", 
        umo = "PCS", 
        qty = 1, 
        unit_price = "", 
        remark = "绑定审核"+str(random.randint(0,100)), 
        sub_total = "38", 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idAdd = confirmedAdd.json()['doc_id']
    print("="*100)
    print("创建confirmed订单",confirmedAdd.json())
    print("doc_idAdd",doc_idAdd)
    print("="*100)
    auditAdd = inter.audit(
        doc_id = doc_idAdd, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("绑定审核",auditAdd.json())
    print("="*100)
    confirmedApproval= inter.confirmedApproval(
        doc_id = doc_idAdd, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("批准confirmed订单",confirmedApproval.json())
    print("="*100)
    test_transferredCancel2 = inter.transferredCancel(
        doc_id = doc_idAdd, 
        reason = "TestCancel"+str(random.randint(0,100)), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#7.取消transferred订单[参数正则提交]",test_transferredCancel2,test_transferredCancel2.json())
    print("="*100)
# test_transferredCancel2()
    assert str(test_transferredCancel2.status_code) == "200"
#8.修改transferred订单基本信息[参数空值提交]
def test_transferredGeneral1():
    test_transferredGeneral1 = inter.transferredGeneral(
        doc_id = "", 
        admin_remark = "",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#8.修改transferred订单基本信息[参数空值提交]",test_transferredGeneral1,test_transferredGeneral1.text)
    print("="*100)
# test_transferredGeneral1()
    assert str(test_transferredGeneral1.status_code) == "400"
#9.修改transferred订单基本信息[参数正则提交]
def test_transferredGeneral2():
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
    auditAdd = inter.audit(
        doc_id = doc_idTransferred, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("绑定审核",auditAdd.json())
    print("="*100)
    test_transferredGeneral2 = inter.transferredGeneral(
        doc_id = doc_idTransferred, 
        admin_remark = "Admin Remark"+str(random.randint(0,100)),
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("9.修改transferred订单基本信息[参数正则提交]",test_transferredGeneral2,test_transferredGeneral2.json())
    print("="*100)
# test_transferredGeneral2()
    assert str(test_transferredGeneral2.status_code) == "200"
#10.修改transferred订单商品信息[参数空值提交]
def test_transferredDetail1():
    test_transferredDetail1 = inter.transferredDetail(
        doc_id = "", 
        index = "", 
        sold_qty = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("10.修改transferred订单商品信息[参数空值提交]",test_transferredDetail1,test_transferredDetail1.text)
    print("="*100)
# test_transferredDetail1()
    assert str(test_transferredDetail1.status_code) == "400"
#11.修改transferred订单商品信息[参数正则提交]
def test_transferredDetail2():
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
    auditAdd = inter.audit(
        doc_id = doc_idTransferred, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("绑定审核",auditAdd.json())
    print("="*100)
    test_transferredDetail2 = inter.transferredDetail(
        doc_id = doc_idTransferred, 
        index = 0, 
        sold_qty = 1, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#11.修改transferred订单商品信息[参数正则提交]",test_transferredDetail2,test_transferredDetail2.json())
    print("="*100)
# test_transferredDetail2()
    assert str(test_transferredDetail2.status_code) == "200"



#12.提交勾选订单[正则提交]
def test_complete():
    test_complete = inter.complete(
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#12.提交勾选订单[正则提交]",test_complete,test_complete.json())
    print("="*100)
# test_complete()
    assert str(test_complete.status_code) == "200"


