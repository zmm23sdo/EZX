from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.获取post订单列表[参数空值提交]
def test_post1():
    test_post1 = inter.post(
        pageSize = "", 
        page = "", 
        status = "", 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.获取post订单列表[参数空值提交]",test_post1,test_post1.text)
    print("="*100)
# test_post1()
    assert str(test_post1.status_code) == "400"
#2.获取post订单列表[参数Status提交]
def test_post2():
    test_post2 = inter.post(
        pageSize = 1, 
        page = 1, 
        status = 2, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#2.获取post订单列表[参数Status提交]",test_post2,test_post2.json())
    print("="*100)
# test_post2()
    assert str(test_post2.status_code) == "200"
#3.获取post订单列表[参数正则提交]
def test_post3():
    test_post3 = inter.post(
        pageSize = 10, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#3.获取post订单列表[参数正则提交]",test_post3,test_post3.json())
    print("="*100)
# test_post3()
    assert str(test_post3.status_code) == "200"
#4.获取post订单详情[参数空值提交]
def test_postDocid1():
    test_postDocid1 = inter.postDocid(
        doc_id = "", 
        pageSize = "", 
        page = "",
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("4.获取post订单详情[参数空值提交]",test_postDocid1,test_postDocid1.text)
    print("="*100)
# test_postDocid1()
    assert str(test_postDocid1.status_code) == "404"
#5.获取post订单详情[参数正则提交]
def test_postDocid2():
    postGet = inter.post(
        pageSize = 10, 
        page = 1, 
        status = None, 
        headers = {'Authorization': loginEZ()}
    )
    doc_idPost = str(postGet.json()['detail'][0]['doc_id'])
    print("="*100)
    print("获取post订单列表",postGet,postGet.json())
    print("doc_idPost",doc_idPost)
    print("="*100)
    test_postDocid2 = inter.postDocid(
        doc_id = doc_idPost, 
        pageSize = 10, 
        page = 1,
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#5.获取post订单详情[参数正则提交]",test_postDocid2,test_postDocid2.text)
    print("="*100)
# test_postDocid2()
    assert str(test_postDocid2.status_code) == "200"