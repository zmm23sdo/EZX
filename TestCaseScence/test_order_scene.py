
from UI.login import loginEZX
from UI.order import create_order, audit_order, detail_order, search_order


# with page.expect_navigation():
#         content = page.text_content(".ant-message-notice-content")# 定位反馈气泡
#     print("\ntest_audit_order")

#     if content == "Operate Successfully":
#         print("\tSuccess")
#     else:
#         print("\tFail")
#     #   断言
#     assert content == "Operate Successfully"
    

def test_audit_order(page):
    username = "mingv"
    password = "qwer`1234"
    loginEZX(page, username, password)
    doc_id = create_order(page)
    search_order(page,doc_id)
    # audit_order(page)
    # order_id = detail_order(page)
    # print(f'\norder_id:',{order_id})
