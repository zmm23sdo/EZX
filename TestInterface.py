import requests
import json

from requests.api import patch


class Interface:
    def __init__(self):
        self.url = "http://ezx-admin.test.ezx.com.my"
        """初始化host url"""


    '''【session】'''
    #登录step-1 验证用户名密码
    def verify(self,username,password,platform):
        path = "/admin/d/session/verify"
        res = requests.post(self.url+path,json={
                "username":username,
                "password":password,
                "platform":platform
        })
        return res
        '''platform:登录的平台，默认为admin
        枚举: admin,app'''
    #登录step-2 获取登录凭证
    def session(self,token,company):
        path = "/auth/d/session"
        res = requests.post(self.url+path,json={
                "token":token,
                "company":company
        })
        return res
        '''company:1 ez 2 gogocar'''
    #使用refreshtoken获取新token
    def sessionPut(self,refresh_token):
        path = "/auth/d/session"
        res = requests.put(self.url+path,params={
                "refresh_token":refresh_token
        })
        return res
    #切换公司
    def sessionPatch(self,company):
        path = "/auth/d/session"
        res = requests.patch(self.url+path,params={
                "company":company
        })
        return res
        '''company:要登录的公司 1 ez 2 gogocar	'''
    #重置accesstoken到期时间
    def sessionAccessToken(self,headers):
        path = "/auth/n/session"
        res = requests.patch(self.url+path
        ,headers=headers)
        return res
    #登出
    def sessionDelete(self,headers):
        path = "/auth/n/session"
        res = requests.delete(self.url+path
        ,headers=headers)
        return res


    '''【users】'''
    #用户列表
    def users(self,pageSize,page,search,headers):
        path = "/admin/n/users"
        if search == None:
            res = requests.get(self.url+path,params={
                "pageSize":pageSize,
                "page":page
            },headers=headers)
        else:
            res = requests.get(self.url+path,params={
                "pageSize":pageSize,
                "page":page,
                "search":search
            },headers=headers)
        return res
    #添加用户
    def usersAdd(self,username,name,phone,email,role,password,headers):
        path = "/admin/n/users"
        res = requests.post(self.url+path,json={
            "username":username,
            "name":name,
            "phone":phone,
            "email":email,
            "role":role,
            "password":password,
        },headers=headers)
        return res
        '''role:Admin,Owner,SalesAgent,Picker,Checker'''
    #修改用户信息
    def userEdit(self,uuid,role,name,email,phone,headers):
        path = "/admin/n/users/"
        res = requests.patch(self.url+path+uuid,params={
            "role":role,
            "name":name,
            "email":email,
            "phone":phone
        },headers=headers)
        return res
    #修改用户密码
    def password(self,uuid,password,headers):
        path = "/admin/n/users/"
        res = requests.put(self.url+path+uuid+"/password",params={
            "password":password
        },headers=headers)
        return res
    #注销用户
    def password(self,uuid,headers):
        path = "/admin/n/users/"
        res = requests.delete(self.url+path+uuid
        ,headers=headers)
        return res


    '''【account】'''
    #获取账户信息
    def account(self,headers):
        path = "/admin/n/account"
        res = requests.delete(self.url+path
        ,headers=headers)
        return res
    #修改账户信息
    def accountEdit(self,email,phone,name,headers):
        path = "/admin/n/account"
        res = requests.patch(self.url+path,params={
            "email":email,
            "phone":phone,
            "name":name
        },headers=headers)
        return res
    #修改密码
    def passwordAccount(self,password,new_password,confirm_password,headers):
        path = "/admin/n/account/password"
        res = requests.patch(self.url+path,params={
            "password":password,
            "new_password":new_password,
            "confirm_password":confirm_password
        },headers=headers)
        return res


    '''【customers】'''
    #获取顾客列表
    def customers(self,pageSize,page,search,headers):
        path = "/admin/n/customers"
        if search == None:
            res = requests.get(self.url+path,params={
                "pageSize":pageSize,
                "page":page
            },headers=headers)
        else:
            res = requests.get(self.url+path,params={
                "pageSize":pageSize,
                "page":page,
                "search":search
            },headers=headers)
        return res
    #获取顾客信息
    def customersCode(self,code,headers):
        path = "/admin/n/customers/"
        res = requests.get(self.url+path+code,headers=headers)
        return res


    '''【products】'''
    #获取产品列表
    def products(self,pageSize,page,search,headers):
        path = "/admin/n/products"
        if search == None:
            res = requests.get(self.url+path,params={
                "pageSize":pageSize,
                "page":page
            },headers=headers)
        else:
            res = requests.get(self.url+path,params={
                "pageSize":pageSize,
                "page":page,
                "search":search
            },headers=headers)
        return res
    #修改产品图片
    def productsCode(self,code,img,headers):
        path = "/admin/n/products/"
        res = requests.put(self.url+path+code,params={
            "img":img
        },headers=headers)
        return res
    #获取oss授权
    def oss(self,userDir,headers):
        path = "/admin/n/oss/token"
        res = requests.post(self.url+path,json={
            "userDir":userDir
        },headers=headers)
        return res
    

    '''【transactionsConfirmed】'''
    #获取订单号
    def orderNumber(self,userDir,headers):
        path = "/admin/n/orderNumber"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取confirmed订单列表
    def confirmed(self,pageSize,page,status,headers):
        path = "/admin/n/transactions/confirmed"
        if status == None:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page
        },headers=headers)
        else:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page,
            "status":status
        },headers=headers)
        return res
        '''status:订单状态 1-pending 2-pick pending 3-check pending 
        4-Stock Exception 5-Packed 6-delivery pending 7-cancel'''
    #创建confirmed订单
    def confirmedAdd(self,customer,shop_name,doc_date,address,
                          customer_name,credit_term,sales_agent,
                          code,name,umo,qty,unit_price,remark,sub_total,
                          foc,headers):
        path = "/admin/n/transactions/confirmed"
        res = requests.post(self.url+path,json={
        "customer":customer,
        "shop_name":shop_name,
        "doc_date":doc_date,
        "address":address,
        "customer_name":customer_name,
        "credit_term":credit_term,
        "sales_agent":sales_agent,
        "detail":[{
            "code":code,
            "name":name,
            "umo":umo,
            "qty":qty,
            "unit_price":unit_price,
            "remark":remark,
            "sub_total":sub_total,
            "foc":foc,
        }]
        },headers=headers)
        return res
    #获取confirmed订单详情
    def confirmedDocid(self,doc_id,pageSize,page,headers):
        path = "/admin/n/transactions/confirmed/"
        res = requests.get(self.url+path+doc_id,params={
        "pageSize":pageSize,
        "page":page
        },headers=headers)
        return res
    #修改confirm订单基本信息
    def general(self,doc_id,customer,doc_date,shop_name,customer_name,
                     address,sales_agent,admin_remark,credit_term,headers):
        path = "/admin/n/transactions/confirmed/"
        res = requests.put(self.url+path+doc_id+"/general",params={
        "customer":customer,
        "doc_date":doc_date,
        "shop_name":shop_name,
        "customer_name":customer_name,
        "address":address,
        "sales_agent":sales_agent,
        "admin_remark":admin_remark,
        "credit_term":credit_term
        },headers=headers)
        return res
    ##修改confirm订单商品信息
    def detailN(self,doc_id,index,discount,sold_price,sold_qty,foc,headers):
        path = "/n/transactions/confirmed/"
        res = requests.put(self.url+path+doc_id+"/detail",params=[{
        "index":index,
        "discount":discount,
        "sold_price":sold_price,
        "sold_qty":sold_qty,
        "foc":foc
        }],headers=headers)
        return res
    #批准confirmed订单
    def confirmedApproval(self,doc_id,headers):
        path = "/admin/n/transactions/confirmed/"
        res = requests.put(self.url+path+doc_id,headers=headers)
        return res
    #取消confirmed订单
    def confirmedCancel(self,doc_id,reason,headers):
        path = "/admin/n/transactions/confirmed/"
        res = requests.delete(self.url+path+doc_id,params={
        "reason":reason
        },headers=headers)
        return res
    #修改confirm订单商品信息
    def detail(self,doc_id,index,discount,sold_price,sold_qty,foc,headers):
        path = "/admin/n/transactions/confirmed/"
        res = requests.put(self.url+path+doc_id+"/detail",params=[{
        "index":index,
        "discount":discount,
        "sold_price":sold_price,
        "sold_qty":sold_qty,
        "foc":foc
        }],headers=headers)
        return res
    
    
    '''【transactionsApp】'''
    #获取in-app订单列表
    def app(self,pageSize,page,status,headers):
        path = "/admin/n/transactions/app"
        if status == None:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page
        },headers=headers)
        else:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page,
            "status":status
        },headers=headers)
        return res
        '''status:订单状态 1-pending 2-pick pending 3-check pending 
        4-Stock Exception 5-Packed 6-delivery pending 7-cancel'''
    #app订单详情
    def confirmedDocid(self,doc_id,pageSize,page,headers):
        path = "/admin/n/transactions/app/"
        res = requests.get(self.url+path+doc_id,params={
        "pageSize":pageSize,
        "page":page
        },headers=headers)
        return res


    '''【dropdown】'''
    #客户下拉框列表
    def customersGet(self,headers):
        path = "/admin/n/dropdown/customers"
        res = requests.get(self.url+path,headers=headers)
        return res 
    #销售员下拉列表
    def agentGet(self,headers):
        path = "/admin/n/dropdown/agent"
        res = requests.get(self.url+path,headers=headers)
        return res 
    #产品下拉列表
    def productsGet(self,search,headers):
        path = "/admin/n/dropdown/products"
        if search == None:
            res = requests.get(self.url+path,headers=headers)
        else:
            res = requests.get(self.url+path,params={
                "search":search
            },headers=headers)
        return res 
    #admin下拉列表
    def adminGet(self,headers):
        path = "/admin/n/dropdown/admin"
        res = requests.get(self.url+path,headers=headers)
        return res 


    '''【audit】'''
    #绑定审核
    def audit(self,doc_id,headers):
        path = "/admin/n/audit"
        res = requests.post(self.url+path,json={
            "doc_id":doc_id
        },headers=headers)
        return res 
    #取消绑定审核
    def auditCancel(self,doc_id,headers):
        path = "/admin/n/audit"
        res = requests.delete(self.url+path,json={
            "doc_id":doc_id
        },headers=headers)
        return res 


    '''【transactionsTransferred】'''
    #获取transferred订单
    def transferred(self,pageSize,page,status,headers):
        path = "/admin/n/transactions/transferred"
        if status == None:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page
        },headers=headers)
        else:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page,
            "status":status
        },headers=headers)
        return res
        '''status:订单状态 1-pending 2-pick pending 3-check pending 
        4-Stock Exception 5-Packed 6-delivery pending 7-cancel'''
    #获取transferred订单详情
    def transferredDocid(self,doc_id,pageSize,page,headers):
        path = "/admin/n/transactions/transferred/"
        res = requests.get(self.url+path+doc_id,params={
            "pageSize":pageSize,
            "page":page
        },headers=headers)
        return res
    #取消transferred订单
    def transferredDocid(self,doc_id,reason,headers):
        path = "/admin/n/transactions/transferred/"
        res = requests.delete(self.url+path+doc_id,params={
            "reason":reason
        },headers=headers)
        return res
    #修改transferred订单基本信息
    def transferredGeneral(self,doc_id,customer,doc_date,shop_name,
                                customer_name,address,sales_agent,
                                admin_remark,credit_term,picker,
                                picker_remark,checker,checker_remark,headers):
        path = "/admin/n/transactions/transferred/"
        res = requests.put(self.url+path+doc_id+"/general",params={
            "customer":customer,
            "doc_date":doc_date,
            "shop_name":shop_name,
            "customer_name":customer_name,
            "address":address,
            "sales_agent":sales_agent,
            "admin_remark":admin_remark,
            "credit_term":credit_term,
            "picker":picker,
            "picker_remark":picker_remark,
            "checker":checker,
            "checker_remark":checker_remark
        },headers=headers)
        return res
    #修改transferred订单商品信息
    def transferredDetail(self,doc_id,index,sold_qty,headers):
        path = "/admin/n/transactions/transferred/"
        res = requests.put(self.url+path+doc_id+"/detail",params=[{
            "index":index,
            "sold_qty":sold_qty
        }],headers=headers)
        return res
    #提交勾选订单*
    def complete(self,value,headers):
        path = "/admin/n/transactions/transferred/complete"
        res = requests.post(self.url+path,params=[
            value
        ],headers=headers)
        return res


    '''【orderHistory】'''
    #获取订单历史
    def orderHistory(self,doc_id,pageSize,page,headers):
        path = "/admin/n/orderHistory/"
        res = requests.get(self.url+path+doc_id,params=[{
            "pageSize":pageSize,
            "page":page
        }],headers=headers)
        return res


    '''【transactionsPost】'''
    #获取post订单列表
    def post(self,pageSize,page,status,headers):
        path = "/admin/n/transactions/post"
        if status == None:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page
        },headers=headers)
        else:
            res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "page":page,
            "status":status
        },headers=headers)
        return res
        '''status:订单状态 1-pending 2-pick pending 3-check pending 
        4-Stock Exception 5-Packed 6-delivery pending 7-cancel'''
    #获取post订单详情
    def postDocid(self,doc_id,headers):
        path = "/admin/n/transactions/post/"
        res = requests.get(self.url+path+doc_id,headers=headers)
        return res


    '''【export】'''
    #导出勾选订单
    def export(self,value,headers):
        path = "/admin/n/export"
        res = requests.post(self.url+path,params=[
            value
        ],headers=headers)
        return res


    '''【verify】'''
    #用户名验证唯一性
    def username(self,username,headers):
        path = "/auth/n/verify/username"
        res = requests.get(self.url+path,params={
            "username":username
        },headers=headers)
        return res
    #email验证唯一性
    def email(self,username,headers):
        path = "/auth/n/verify/email"
        res = requests.get(self.url+path,params={
            "email":email
        },headers=headers)
        return res