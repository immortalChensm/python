import random
from card import Card
from user import User
class ATM(object):

    def __init__(self,allUsers):
        self.allUsers = allUsers
        #保存用户和卡数据

    def createUser(self):

        name   = input("请输入您的大名：")
        idcard = input("请输入您的身份证号：")
        phone  = input("请输入您的电话：")

        depositMoney = int(input("请输入预存款："))
        if depositMoney < 0:
            print("预存款输入错误，开户失败")
            return -1
        firstPwd = input("请设置密码：")
        if not self.verifyPwd(firstPwd):
            print("确认密码错误，开户失败")
            return -1

        #生成一个随机卡号
        cardNum = self.generatorCardId()
        #卡号  卡余额  卡密码
        card = Card(cardNum,depositMoney,firstPwd)
        #用户名  用户电话  用户卡  用户身份证
        user = User(name,phone,card,idcard)
        self.allUsers[cardNum] = user

        print("开户成功，请牢记卡号：%s"%(cardNum))

    def searchUser(self):

        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if user.card.cardLock:
            print("您的卡号已经被锁定，无法使用其它功能，请解锁")
            return -1
        if not self.verifyPwd(user.card.passwd):
            print("卡密码错误，查询失败")
            #三次都错误，则锁定卡
            user.card.cardLock = True
            return -1
        print("账号：%s   余额：%d"%(user.card.cardId,user.card.cardMoney))
    def saveMoney(self):
        cardNum= input("请输入您的卡号:")

        user = self.allUsers.get(cardNum)
        if not user:
            print("您的卡不存在，无法办理存款")
            return -1
        if not self.verifyPwd(user.card.passwd):
            print("卡密码输入错误，无法办理存款")
            return -1
        if user.card.cardLock:
            print("卡已经被锁，无法办理存款")
            return -1
        money = int(input("请输入存款金额"))
        user.card.cardMoney+=money
        print("存款成功，余额为：%d"%(user.card.cardMoney))

    def withDraw(self):

        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在，取款失败")
            return -1
        if not self.verifyPwd(user.card.passwd):
            print("取款密码错误，取款失败")
            return -1
        if user.card.cardLock:
            print("卡已被锁定，无法取款，请解锁")
            return -1
        money = int(input("请输入取款金额："))
        if money>user.card.cardMoney:
            print("余额不足，取款失败")
            return -1
        user.card.cardMoney-=money
        print("取款成功，余额为%d"%(user.card.cardMoney))
    def transferMoney(self):

        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("您的卡号不存在，无法转账")
            return -1
        if not self.verifyPwd(user.card.passwd):
            print("输入密码错误，无法转账")
            return -1
        if user.card.cardLock:
            print("您的卡已被锁定，无法转账")
            return -1
        account = input("请输入对方账号：")
        anotherUser = self.allUsers.get(account)
        if not anotherUser:
            print("对方账号不存在，无法转账")
            return -1
        #打印对方账户信息
        print("对方账号是：%s"%(anotherUser.name))
        isTransfer = input("是否要转账[yes][cancel]")
        if isTransfer=='cancel':
            print("取消转账")
            return -1
        money = int(input("请输入转账金额："))
        user.card.cardMoney-=money
        anotherUser.card.cardMoney+=money
        print("转账成功，您的余额为：%d"%(user.card.cardMoney))

    def passwd(self):
        pass
    def lockCard(self):
        #锁定卡的条件：卡要存在  卡密码要对  身份要对
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，无法锁定")
            return -1
        if not self.verifyPwd(user.card.passwd):
            print("卡密码不对，无法锁定")
            return -1
        tempIdcard = input("请输入您的身份证号码：")
        if user.Idcard!=tempIdcard:
            print("身份证号码不对，无法锁定")
            return -1
        user.card.cardLock = True
        print("锁定成功")
    def unlockCard(self):
        #解锁条件：卡存在 卡密码对  身份对
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡都没有，无法解锁")
            return -1
        if not self.verifyPwd(user.card.passwd):
            print("输入的卡密码不对，无法解锁")
            return -1
        tempIdcard = input("请输入您的身份证号：")
        if tempIdcard!=user.Idcard:
            print("身份证不对，无法解锁")
            return -1
        #解锁
        user.card.cardLock = False
        print("解锁成功")

    def newCard(self):
        pass
    def removeUser(self):
        pass

    def verifyPwd(self,pwd):

        for i in range(3):
            tempPwd = input("请输入确认密码:")
            if tempPwd==pwd:
                return True

        return False
    #生成唯一卡号
    def generatorCardId(self):
        while True:
            str = ""
            for i in range(6):
                str += chr(random.randrange(ord('0'), ord('9') + 1))

            if not self.allUsers.get(str):
                return str
