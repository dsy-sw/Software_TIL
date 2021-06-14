class Date:
    def __init__(self, month):
        self.__month = month

    def getmonth(self):
        return self.__month

    def setmonth(self, month):
        if 1 <= month <= 12:
            self.month = month


today = Date(8)
today.month = 15

print(today.month)
