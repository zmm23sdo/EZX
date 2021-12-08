import json
from TestInterface import Interface
from Common import GBK2312, TimeNow, Unicode, loginEZ
import random
inter = Interface()
Random = TimeNow()


#1.用户列表[参数空值提交]
def test_users1():
    test_users1 = inter.users(
        pageSize = None, 
        page = None, 
        search = None, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.用户列表[参数空值提交]",test_users1)
    print("="*100)
# test_users1()
    assert str(test_users1.status_code) == "400"
#2.用户列表[参数Search提交]
def test_users2():
    test_users2 = inter.users(
        pageSize = 1, 
        page = 1, 
        search = "zhangmingwei", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.用户列表[参数Search提交]",test_users2.json())
    print("="*100)
# test_users2()
    assert str(test_users2.status_code) == "200"
#3.用户列表[参数正则提交]
def test_users3():
    test_users3 = inter.users(
        pageSize = 100, 
        page = 1, 
        search = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.用户列表[参数正则提交]",test_users3.json())
    print("="*100)
# test_users3()
    assert str(test_users3.status_code) == "200"
#4.添加用户[参数空值提交]
def test_usersAdd1():
    test_usersAdd1 = inter.usersAdd(
        username = "", 
        name = "", 
        phone = "", 
        email = "", 
        role = "", 
        password = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#4.添加用户[参数空值提交]",test_usersAdd1.json())
    print("="*100)
# test_usersAdd1()
    assert str(test_usersAdd1.json()['code']) == "400.1"
#5.添加用户[参数正则提交]
def test_usersAdd2():
    username = "mtest"+str(random.randint(0,100))
    email = username+"@users.com"
    test_usersAdd2 = inter.usersAdd(
        username = username, 
        name = Unicode()+GBK2312()+TimeNow(), 
        phone = Random, 
        email = email,
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.添加用户[参数正则提交]",test_usersAdd2.json(),test_usersAdd2)
    print("="*100)
# test_usersAdd2()
    assert str(test_usersAdd2.status_code) == "201"
#6.添加用户[参数用户名已存在提交]
def test_usersAdd3():
    username = "mvtest"+str(random.randint(0,100))
    email = username+"@users.com"
    test_usersAdd3 = inter.usersAdd(
        username = "test001", 
        name = Unicode()+GBK2312()+TimeNow(), 
        phone = Random, 
        email = email,
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#6.添加用户[参数用户名已存在提交]",test_usersAdd3.json())
    print("="*100)
# test_usersAdd3()
    assert str(test_usersAdd3.json()['code']) == "422.1.1"
#7.修改用户信息[参数空值提交]
def test_userEdit1():
    test_userEdit1 = inter.userEdit(
        uuid = "", 
        role = "", 
        name = "", 
        email = "", 
        phone = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#7.修改用户信息[参数空值提交]",test_userEdit1)
    print("="*100)
# test_userEdit1()
    assert str(test_userEdit1.status_code) == "404"
#8.修改用户信息[参数错误提交]
def test_userEdit2():
    test_userEdit2 = inter.userEdit(
        uuid = "ABC", 
        role = "", 
        name = "", 
        email = "", 
        phone = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#8.修改用户信息[参数错误提交]",test_userEdit2.json())
    print("="*100)
# test_userEdit2()
    assert str(test_userEdit2.json()['code']) == "400.1"
#9.修改用户信息[参数正则提交]
def test_userEdit3():
    username = "mvest"+str(random.randint(0,100))
    email = username+"@users.com"
    addUsers = inter.usersAdd(
        username = username, 
        name = Unicode()+GBK2312()+TimeNow(), 
        phone = Random, 
        email = email,
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("添加一个可用用户",addUsers.json())
    print("="*100)
    #获取用户的uuid,email
    uuid_usersadd = addUsers.json()["uuid"]
    email_usersadd = addUsers.json()["email"]
    print("="*100)
    print("uuid_usersadd",uuid_usersadd)
    print("email_usersadd",email_usersadd)
    print("="*100)
    test_userEdit3 = inter.userEdit(
        uuid = uuid_usersadd, 
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        name = Unicode()+GBK2312()+TimeNow(), 
        email = email_usersadd, 
        phone = TimeNow(), 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#9.修改用户信息[参数正则提交]",test_userEdit3.json())
    print("="*100)
# test_userEdit3()
    assert str(test_userEdit3.status_code) == "200"
#10.修改用户密码[参数空值提交]
def test_password1():
    username = "mvtest"+str(random.randint(0,100))
    email = username+"@users.com"
    addUsers = inter.usersAdd(
        username = username, 
        name = Unicode()+GBK2312()+TimeNow(), 
        phone = Random, 
        email = email,
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("添加一个可用用户",addUsers.json())
    print("="*100)
    #获取用户的uuid,email
    uuid_usersadd = addUsers.json()["uuid"]
    print("="*100)
    print("uuid_usersadd",uuid_usersadd)
    print("="*100)
    test_password1 = inter.password(
        uuid = "uuid_usersadd", 
        password = "",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("10.修改用户密码[参数空值提交]",test_password1.json())
    print("="*100)
# test_password1()
    assert str(test_password1.json()['code']) == "401.11"
#11.修改用户密码[参数正则提交]
def test_password2():
    username = "mvtest"+str(random.randint(0,1000))
    email = username+"@users.com"
    addUsers = inter.usersAdd(
        username = username, 
        name = Unicode()+GBK2312()+TimeNow(), 
        phone = Random, 
        email = email,
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("添加一个可用用户",addUsers.json())
    print("="*100)
    #获取用户的uuid,email
    uuid_usersadd = addUsers.json()["uuid"]
    print("="*100)
    print("uuid_usersadd",uuid_usersadd)
    print("="*100)
    test_password2 = inter.password(
        uuid = "uuid_usersadd", 
        password = "qwer`123",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#11.修改用户密码[参数正则提交]",test_password2.json())
    print("="*100)
# test_password2()
    assert str(test_password2.json()['code']) == "200"
#12.注销用户[参数空值提交]
def test_usersDelete1():
    test_usersDelete1 = inter.usersDelete(
        uuid = "",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#12.注销用户[参数空值提交]",test_usersDelete1)
    print("="*100)
# test_usersDelete1()
    assert str(test_usersDelete1.status_code) == "404"
#13.注销用户[参数错误提交]
def test_usersDelete2():
    test_usersDelete2 = inter.usersDelete(
        uuid = "ABC",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#13.注销用户[参数错误提交]",test_usersDelete2.json())
    print("="*100)
# test_usersDelete2()
    assert str(test_usersDelete2.json()['code']) == "200"
#14.注销用户[参数正则提交]
def test_usersDelete3():
    username = "mvtest"+str(random.randint(0,1000))
    email = username+"@users.com"
    addUsers = inter.usersAdd(
        username = username, 
        name = Unicode()+GBK2312()+TimeNow(), 
        phone = Random, 
        email = email,
        role = ["Admin", "Owner", "SalesAgent", "Picker", "Checker"], 
        password = "qwer`123", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("添加一个可用用户",addUsers.json())
    print("="*100)
    #获取用户的uuid,email
    uuid_usersadd = addUsers.json()["uuid"]
    print("="*100)
    print("uuid_usersadd",uuid_usersadd)
    print("="*100)
    test_usersDelete3 = inter.usersDelete(
        uuid = uuid_usersadd,
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#14.注销用户[参数正则提交]",test_usersDelete3.json())
    print("="*100)
# test_usersDelete3()
    assert str(test_usersDelete3.json()['code']) == "200"