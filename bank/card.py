class Card(object):
    def __init__(self,cardId,cardMoney,passwd):
        self.cardId = cardId
        self.cardMoney = cardMoney
        self.passwd    = passwd
        self.cardLock  = False