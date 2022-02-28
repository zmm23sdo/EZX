from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取订单号[参数正则提交]
def test_orderNumber():
    test_orderNumber = inter.orderNumber(
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取订单号[参数正则提交]",test_orderNumber.json())
    print("="*100)
# test_orderNumber()
    assert str(test_orderNumber.status_code) == "200"
#2.获取confirmed订单列表[参数空值提交]
def test_confirmed1():
    test_confirmed1 = inter.confirmed(
        pageSize = "", 
        page = "", 
        status = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取confirmed订单列表[参数空值提交]",test_confirmed1)
    print("="*100)
# test_confirmed1()
    assert str(test_confirmed1.status_code) == "400"
#3.获取confirmed订单列表[参数Status提交]
def test_confirmed2():
    test_confirmed2 = inter.confirmed(
        pageSize = 1, 
        page = 1, 
        status = 1, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.获取confirmed订单列表[参数Status提交]",test_confirmed2.json())
    print("="*100)
# test_confirmed2()
    assert str(test_confirmed2.status_code) == "200"
#4.获取confirmed订单列表[参数正则提交]
def test_confirmed3():
    test_confirmed3 = inter.confirmed(
        pageSize = 100, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.获取confirmed订单列表[参数正则提交]",test_confirmed3.json())
    print("="*100)
# test_confirmed3()
    assert str(test_confirmed3.status_code) == "200"
#5.创建confirmed订单[参数空值提交]
def test_confirmedAdd1():
    test_confirmedAdd1 = inter.confirmedAdd(
        customer = "", 
        shop_name = "", 
        doc_date = "", 
        address = "", 
        customer_name = "", 
        credit_term = "", 
        sales_agent = "", 
        code = "", 
        name = "", 
        umo = "", 
        qty = "", 
        unit_price = "", 
        remark = "", 
        sub_total = "", 
        foc = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.创建confirmed订单[参数空值提交]",test_confirmedAdd1)
    print("="*100)
# test_confirmedAdd1()
    assert str(test_confirmedAdd1.status_code) == "400"
#6.创建confirmed订单[参数正则提交]
def test_confirmedAdd2():
    test_confirmedAdd2 = inter.confirmedAdd(
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
        remark = "Test"+str(random.randint(0,100)), 
        sub_total = "38", 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#6.创建confirmed订单[参数正则提交]",test_confirmedAdd2.json(),test_confirmedAdd2)
    print("="*100)
# test_confirmedAdd2()
    assert str(test_confirmedAdd2.status_code) == "201"
#7.获取confirmed订单详情[参数空值提交]
def test_confirmedDocid1():
    test_confirmedDocid1 = inter.confirmedDocid(
        doc_id = "", 
        pageSize = "", 
        page = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#7.获取confirmed订单详情[参数空值提交]",test_confirmedDocid1)
    print("="*100)
# test_confirmedDocid1()
    assert str(test_confirmedDocid1.status_code) == "404"
#8.获取confirmed订单详情[参数正则提交]
def test_confirmedDocid2():
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
        remark = "Test"+str(random.randint(0,100)), 
        sub_total = "38", 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idAdd = confirmedAdd.json()['doc_id']
    print("="*100)
    print("创建confirmed订单",confirmedAdd.json())
    print("doc_idAdd",doc_idAdd)
    print("="*100)
    test_confirmedDocid2 = inter.confirmedDocid(
        doc_id = doc_idAdd, 
        pageSize = "1", 
        page = "1", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#8.获取confirmed订单详情[参数正则提交]",test_confirmedDocid2.json())
    print("="*100)
# test_confirmedDocid2()
    assert str(test_confirmedDocid2.status_code) == "200"
#9.修改confirm订单基本信息[参数空值提交]
def test_general1():
    test_general1 = inter.general(
        doc_id = "",
        admin_remark = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#9.修改confirm订单基本信息[参数空值提交]",test_general1)
    print("="*100)
# test_general1()
    assert str(test_general1.status_code) == "400"
#10.修改confirm订单基本信息[参数未绑定审核提交]
def test_general2():
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
        remark = "Test"+str(random.randint(0,100)), 
        sub_total = "38", 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idAdd = confirmedAdd.json()['doc_id']
    print("="*100)
    print("创建confirmed订单",confirmedAdd.json())
    print("doc_idAdd",doc_idAdd)
    print("="*100)
    test_general2 = inter.general(
        doc_id = doc_idAdd, 
        admin_remark = "TestEdit"+str(random.randint(0,100)), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#10.修改confirm订单基本信息[参数未绑定审核提交]",test_general2,test_general2.text)
    print("="*100)
# test_general2()
    assert str(test_general2.json()['code']) == "401.7"
#11.修改confirm订单基本信息[参数绑定审核后提交]
def test_general3():
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
        remark = "Test"+str(random.randint(0,100)), 
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
    test_general3 = inter.general(
        doc_id = doc_idAdd, 
        admin_remark = "TestEdit"+str(random.randint(0,100)), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#11.修改confirm订单基本信息[参数绑定审核后提交]",test_general3,test_general3.text)
    print("="*100)
# test_general3()
    assert str(test_general3.json()['code']) == "200"
#12.批准confirmed订单[参数空值提交]
def test_confirmedApproval1():
    test_confirmedApproval1 = inter.confirmedApproval(
        doc_id = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#12.批准confirmed订单[参数空值提交]",test_confirmedApproval1)
    print("="*100)
# test_confirmedApproval1()
    assert str(test_confirmedApproval1.status_code) == "404"
#13.批准confirmed订单[参数未绑定审核提交]
def test_confirmedApproval2():
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
    test_confirmedApproval2 = inter.confirmedApproval(
        doc_id = doc_idAdd, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#13.批准confirmed订单[参数未绑定审核提交]",test_confirmedApproval2.json())
    print("="*100)
# test_confirmedApproval2()
    assert str(test_confirmedApproval2.json()['code']) == "401.7"


#15.批准confirmed订单[参数绑定后审核提交]
def test_confirmedApproval3():
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
    test_confirmedApproval3 = inter.confirmedApproval(
        doc_id = doc_idAdd, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#15.批准confirmed订单[参数绑定后审核提交]",test_confirmedApproval3.json())
    print("="*100)
# test_confirmedApproval3()
    assert str(test_confirmedApproval3  .json()['code']) == "200"




#16.取消confirmed订单[参数正则提交]
def test_confirmedCancel1():
    test_confirmedCancel1 = inter.confirmedCancel(
        doc_id = "", 
        reason = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#16.取消confirmed订单[参数正则提交]",test_confirmedCancel1)
    print("="*100)
# test_confirmedCancel1()
    assert str(test_confirmedCancel1.status_code) == "404"
#17.取消confirmed订单[参数未绑定审核提交]
def test_confirmedCancel2():
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
    test_confirmedCancel2 = inter.confirmedCancel(
        doc_id = doc_idAdd, 
        reason = "未绑定审核"+str(random.randint(0,100)), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#17.取消confirmed订单[参数未绑定审核提交]",test_confirmedCancel2,test_confirmedCancel2.text)
    print("="*100)
# test_confirmedCancel2()
    assert str(test_confirmedCancel2.status_code) == "200"
#18.取消confirmed订单[参数绑定审核后提交]
def test_confirmedCancel3():
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
    test_confirmedCancel3 = inter.confirmedCancel(
        doc_id = doc_idAdd, 
        reason = "未绑定审核"+str(random.randint(0,100)), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#18.取消confirmed订单[参数绑定审核后提交]",test_confirmedCancel3,test_confirmedCancel3.text)
    print("="*100)
# test_confirmedCancel3()
    assert str(test_confirmedCancel3.status_code) == "200"
#19.修改confirm订单商品信息[参数空值提交]
def test_detail1():
    test_detail1 = inter.detail(
        doc_id = "", 
        index = "", 
        discount = "", 
        sold_price = "", 
        sold_qty = "", 
        foc = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#19.修改confirm订单商品信息[参数空值提交]",test_detail1)
    print("="*100)
# test_detail1()
    assert str(test_detail1.status_code) == "400"
#20.修改confirm订单商品信息[参数未绑定审核提交]
def test_detail2():
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
    test_detail2 = inter.detail(
        doc_id = doc_idAdd, 
        index = 0, 
        discount = "0.00", 
        sold_price = "0.00", 
        sold_qty = 1, 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#20.修改confirm订单商品信息[参数未绑定审核提交]",test_detail2,test_detail2.text)
    print("="*100)
# test_detail2()
    assert str(test_detail2.json()['code']) == "401.7"
#21.修改confirm订单商品信息[参数绑定审核后提交]
def test_detail3():
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
    test_detail3 = inter.detail(
        doc_id = doc_idAdd, 
        index = 0, 
        discount = "0.00", 
        sold_price = "0.00", 
        sold_qty = 1, 
        foc = 2, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#21.修改confirm订单商品信息[参数绑定审核后提交]",test_detail3,test_detail3.json())
    print("="*100)
# test_detail3()
    assert str(test_detail3.json()['code']) == "200"
