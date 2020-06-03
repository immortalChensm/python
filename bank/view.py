import time

class view(object):
    admin = 'admin'
    passwd= '123'

    def showLogin(self):
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                                                                          *")
        print("*                    Welcome to use jackcsm bank system                    *")
        print("*                                                                          *")
        print("*                                                                          *")
        print("****************************************************************************")

    def showFunction(self):
        print("****************************************************************************")
        print("*         开户[open]                            查询[search]               *")
        print("*         存款[save]                            取款[withdraw]             *")
        print("*         转账[account]                         改密[passwd]               *")
        print("*         锁定[lock]                            解锁[unlock]               *")
        print("*         销户[cancel]                          补卡[card]                 *")
        print("*                            退出[exit]                                    *")
        print("****************************************************************************")

    def loginAndExit(self):
        inputAdmin = input("请输入账号：")
        if self.admin != inputAdmin:
            print("账号错误")
            return -1
        inputPasswd = input("请输入密码：")
        if self.passwd != inputPasswd:
            print("密码错误")
            return -1
        print("操作成功，请稍候...")
        time.sleep(2)
        return 0