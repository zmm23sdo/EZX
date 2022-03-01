from UI.login import loginEZX
from UI.order import create_order, audit_order

def test_create_order(page):
    username = "mingv"
    password = "qwer`1234"
    loginEZX(page, username, password)
    create_order(page)
    with page.expect_navigation():
        content = page.text_content(".ant-message-custom-content")# 定位反馈气泡
    print("\ntest_create_order")

    if content == "Add Order Successfully!":
        print("\tSuccess")
    else:
        print("\tFail")
    #   断言
    assert content == "Add Order Successfully!"

def test_audit_order(page):
    username = "mingv"
    password = "qwer`1234"
    loginEZX(page, username, password)
    create_order(page)# 创建一条新的订单，避免 新旧数据交叉操作
    audit_order(page)
    with page.expect_navigation():
        content = page.text_content(".ant-message-notice-content")# 定位反馈气泡
    print("\ntest_audit_order")

    if content == "Operate Successfully":
        print("\tSuccess")
    else:
        print("\tFail")
    #   断言
    assert content == "Operate Successfully"
    