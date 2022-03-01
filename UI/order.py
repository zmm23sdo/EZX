import random
from urllib import response
def create_order(page):
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
    # Click text=Item:Please Enter Product Code / Name >> div >> nth=3
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
    page.locator("input[type=\"text\"]").nth(2).fill("UITest"+str(random.randint(0,99)))
    # Click button:has-text("Submit")
    # with page.expect_navigation(url="http://ezx-admin.test.ezx.com.my/transactions"):

    with page.expect_request_finished(lambda request: request.url == "http://ezx-admin.test.ezx.com.my/admin/n/transactions/confirmed") as request_info:
        page.locator("button:has-text(\"Submit\")").click()

    doc_id = str(request_info.value.response().json()["doc_id"])
    print(f'\ndoc_id: {doc_id}')
    return doc_id 
def audit_order(page):
    # Go to http://ezx-admin.test.ezx.com.my/transactions/
    page.goto("http://ezx-admin.test.ezx.com.my/transactions/")
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-page-container-children-content > div:nth-child(3) > div > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > div > div > a > span > svg").hover()
    with page.expect_navigation():
        page.locator("text=Audit").click()
    # Click button:has-text("Approve")
    page.locator("button:has-text(\"Approve\")").click()
    # Click button:has-text("Ok")
    # with page.expect_navigation(url="http://ezx-admin.test.ezx.com.my/transactions/"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Ok\")").click()
   
def detail_order(page):#    check create_new_aduit_order's detail
    # create_order(page)# creat a new order
    # audit_order(page)#  audit the new order
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-page-container-children-content > div:nth-child(4) > div > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > div > div > a > span > svg > path").hover()
    with page.expect_navigation():
        page.locator("text=Order Detail").click()
   
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-page-container-children-content > div:nth-child(1) > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > span.ant-descriptions-item-content")
    order_id = str(content)#    Get the order ID whose status is "Pick Pending"
    # print(f'\norder_id:',{order_id})
    return order_id
    
def search_order(page, data):
    page.goto("http://ezx-admin.test.ezx.com.my/transactions/")
    # Fill input[type="text"]
    page.locator("input[type=\"text\"]").fill(data)
    # Click #advanced_search button
    page.locator("#advanced_search button").click()
    with page.expect_navigation():
        if page.locator("text={data}").is_visible:
            print(f'\nCan Found:{data}')
        else:
            print(f'\nCannot Found:{data}')
    

