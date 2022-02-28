
from UI.login import loginEZX

# inter = Interface()
# #   API创建订单
# #   创建订单要传的参数：
# customer = "300-W003"
# shop_name = "WAH PERFECT ZONE CAR AIR-COND & ACCESSORIES"
# doc_date = Now()
# address = "NO. 52 PUSAT PERNIAGAAN KM 2 KM 2 JLN. LIPIS 27600 RAUB,PAHANG"
# customer_name = "WAH"
# credit_term = "90"
# sales_agent = "RYAN"
# code = "STK113"
# name = "30CM x 10 METER LAMP STICKER (LIGHT BLACK)(EZ)* "
# umo = "PCS"
# qty = 1
# unit_price = ""
# remark = "UiApi"+str(random.randint(0,100))
# sub_total = "38"
# foc = 2
# #   创建订单并拿到新创建的订单的Doc ID：
# def creat_confirmed():
#     creat_confirmed = inter.confirmedAdd(
#         customer = customer, 
#         shop_name = shop_name, 
#         doc_date = doc_date, 
#         address = address, 
#         customer_name = customer_name, 
#         credit_term = credit_term, 
#         sales_agent = sales_agent, 
#         code = code, 
#         name = name, 
#         umo = umo, 
#         qty = qty, 
#         unit_price = unit_price, 
#         remark = remark, 
#         sub_total = sub_total, 
#         foc = foc, 
#         headers = {'Authorization': loginEZ()}
#     )
#     # print("="*100)
#     # print("创建confirmed订单",creat_confirmed.json(),creat_confirmed)
#     # print("="*100)
#     doc_id_created = str(creat_confirmed.json()["doc_id"])
#     # print(f'doc_id_created: {doc_id_created}')
#     return doc_id_created
# # creat_confirmed()

def test_create_order(page):
    username = "mingv"
    password = "qwer`1234"
    loginEZX(page, username, password)
    #   #UI create order:
    # Click a:has-text("Transaction")
    page.locator("a:has-text(\"Transaction\")").click()
    # assert page.url == "http://ezx-admin.test.ezx.com.my/transactions"
    # Click button:has-text("Add Order")
    page.locator("button:has-text(\"Add Order\")").click()
    assert page.url == "http://ezx-admin.test.ezx.com.my/transaction/confirmed/create"
    # Click .ant-select-selector >> nth=0
    page.locator(".ant-select-selector").first.click()
    # Click text=300-1001 >> nth=1
    page.locator("text=300-1001").nth(1).click()
    # Click .ant-picker-input
    page.locator(".ant-picker-input").click()
    # Click tr:nth-child(5) .ant-picker-cell.ant-picker-cell-start .ant-picker-cell-inner
    page.locator("tr:nth-child(5) .ant-picker-cell.ant-picker-cell-start .ant-picker-cell-inner").click()
    # Click .ant-form div:nth-child(3) .ant-col.ant-col-7 .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector
    page.locator(".ant-form div:nth-child(3) .ant-col.ant-col-7 .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector").click()
    #   将选项改成 'MINGVTEST1'
    page.evaluate("() => { document.querySelector('#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-page-container-children-content > div:nth-child(1) > div > form > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control > div > div > div > div > span.ant-select-selection-item').innerText = 'MINGVTEST1' }")
    # page.pause()  #   调试用的暂停
    page.locator("text=Item:Please Enter Product Code / Name >> div").nth(3).click()
    # Click text=14000(OFFICE EQUIPMENT)
    page.locator("text=14000(OFFICE EQUIPMENT)").click()
    # Click input[type="text"] >> nth=0
    page.locator("input[type=\"text\"]").first.click()
    # Fill input[type="text"] >> nth=0
    page.locator("input[type=\"text\"]").first.fill("1")
    # Click text=14000OFFICE EQUIPMENTPCS >> input[role="combobox"]
    page.locator("text=14000OFFICE EQUIPMENTPCS >> input[role=\"combobox\"]").click()
    # Fill text=14000OFFICE EQUIPMENTPCS >> input[role="combobox"]
    page.locator("text=14000OFFICE EQUIPMENTPCS >> input[role=\"combobox\"]").fill("2")
    # Click input[type="text"] >> nth=1
    page.locator("input[type=\"text\"]").nth(1).click()
    # Fill input[type="text"] >> nth=1
    page.locator("input[type=\"text\"]").nth(1).fill("3")
    # Click input[type="text"] >> nth=2
    page.locator("input[type=\"text\"]").nth(2).click()
    # Fill input[type="text"] >> nth=2
    page.locator("input[type=\"text\"]").nth(2).fill("UITest")
    # Click button:has-text("Submit")
    # with page.expect_navigation(url="http://ezx-admin.test.ezx.com.my/transactions"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Submit\")").click()
   