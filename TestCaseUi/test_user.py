from UI.login import loginEZX

def test_create_user(page):
    username = "mingv"
    password = "qwer`1234"
    loginEZX(page, username, password)