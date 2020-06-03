from view import view
from atm import ATM
import os
import pickle
import time
def main():
    viewObj = view()

    #展示登录界面
    viewObj.showLogin()
    #验证管理员登录
    login = viewObj.loginAndExit()
    if login==-1:
        return -1

    filepath = os.path.join(os.getcwd(), "allUsers.txt")
    if os.path.isfile(filepath):
        f = open(filepath, "rb")
        allUsers = pickle.load(f)
        f.close()
    else:
        allUsers = {}


    atmObj = ATM(allUsers)
    while True:
        #展示功能界面
        viewObj.showFunction()
        option = input("请输入您的操作")
        if option == 'open':
            atmObj.createUser()
        elif option == 'search':
            atmObj.searchUser()

        elif option =='save':
            atmObj.saveMoney()
        elif option == 'withdraw':
            atmObj.withDraw()
        elif option == 'account':
            atmObj.transferMoney()
        elif option =='passwd':
            pass
        elif option == 'lock':
            atmObj.lockCard()
        elif option == 'unlock':
            atmObj.unlockCard()
        elif option == 'cancel':
            pass
        elif option == 'card':
            pass
        elif option == 'exit':
            if not viewObj.loginAndExit():


                f = open(filepath,"wb")
                pickle.dump(atmObj.allUsers,f)
                f.close()
                return -1

        time.sleep(2)


if __name__ == '__main__':
    main()