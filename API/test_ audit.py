from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.绑定审核[参数空值提交]
def test_audit1():
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
        remark = "未绑定审核"+str(random.randint(0,100)), 
        sub_total = "38", 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idAdd = confirmedAdd.json()['doc_id']
    print("="*100)
    print("创建confirmed订单",confirmedAdd.json())
    print("doc_idAdd",doc_idAdd)
    print("="*100)
    test_audit1 = inter.audit(
        doc_id = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.绑定审核[参数空值提交]",test_audit1,test_audit1.text)
    print("="*100)
# test_audit1()
    assert str(test_audit1.status_code) == "404"
#2.绑定审核[参数正则提交]
def test_audit2():
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
        remark = "未绑定审核"+str(random.randint(0,100)), 
        sub_total = "38", 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idAdd = confirmedAdd.json()['doc_id']
    print("="*100)
    print("创建confirmed订单",confirmedAdd.json())
    print("doc_idAdd",doc_idAdd)
    print("="*100)
    test_audit2 = inter.audit(
        doc_id = doc_idAdd, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("##2.绑定审核[参数正则提交]",test_audit2,test_audit2.json())
    print("="*100)
# test_audit2()
    assert str(test_audit2.status_code) == "200"
#3.取消绑定审核[参数空值提交]
def test_auditCancel1():
    test_auditCancel1 = inter.auditCancel(
        doc_id = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.取消绑定审核[参数空值提交]",test_auditCancel1,test_auditCancel1.text)
    print("="*100)
# test_auditCancel1()
    assert str(test_auditCancel1.status_code) == "404"
#4.取消绑定审核[参数正则提交]
def test_auditCancel2():
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
        remark = "未绑定审核"+str(random.randint(0,100)), 
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
    test_auditCancel2 = inter.auditCancel(
        doc_id = doc_idAdd, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.取消绑定审核[参数正则提交]",test_auditCancel2,test_auditCancel2.text)
    print("="*100)
# test_auditCancel2()
    assert str(test_auditCancel2.status_code) == "200"