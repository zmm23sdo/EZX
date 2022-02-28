

def login(page,username,password):#   封装 用户名+密码 登录
    # Open new page
    # page.wait_for_timeout(1000)
    # Go to http://ezx-admin.test.ezx.com.my/
    page.goto("http://ezx-admin.test.ezx.com.my/")
    # page.wait_for_timeout(1000)
    # Go to http://ezx-admin.test.ezx.com.my/user/login
    page.goto("http://ezx-admin.test.ezx.com.my/user/login")
    # page.wait_for_timeout(1000)
    # Fill input[type="text"]
    page.locator("input[type=\"text\"]").fill(username)
    # page.wait_for_timeout(1000)
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill(password)
    # page.wait_for_timeout(1000)
    # Click button:has-text("Login")
    page.locator("button:has-text(\"Login\")").click()
    # page.wait_for_timeout(1000)

def loginEZX(page, username, password):
    login(page, username, password)
    # Click text=EZX># with page.expect_navigation(url="http://ezx-admin.test.ezx.com.my/user-management"):
    with page.expect_navigation():
        page.locator("text=EZX>").click()
    # Click h1:has-text("EZX")
    # page.locator("h1:has-text(\"EZX\")").click()

def loginGOGOCAR(page, username, password):
    # Click text=EZX># with page.expect_navigation(url="http://ezx-admin.test.ezx.com.my/user-management"):
    login(page, username, password)
    with page.expect_navigation():
        page.locator("text=Gogocar>").click()
    # Click h1:has-text("Gogocar")
    # page.locator("h1:has-text(\"Gogocar\")").click()