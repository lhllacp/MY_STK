#coding=gb2312
from datetime import datetime
class StockTradeInfo:
    def __init__(self, i, s, p):
        self.id = i
        self.stock = s
        self.buy = p
        self.sale = 0
        self.sale_singal = False
        self.profit = 0
        self.buy_date = datetime.today()
        self.sale_date = None
    def get_stock(self):
        return self.stock
    def get_buy_price(self):
        return self.buy
    def get_sale_price(self):
        return self.sale
    def get_profit(self):
        return self.sale / self.buy - 1.0
    def get_hold_days(self):
        return (self.sale_date - self.buy_date).days
    def set_sale_date(self, d = datetime.today()):
        self.sale_date = d
    def set_sale_price(self, p):
        self.sale = p
    def log(self):
        print("%d %s %d %d %s"%(self.id, self.stock, self.buy, self.sale, self.buy_date))
class StockTradeRecord:
    def __init__(self):
        self.record = {}
    def set_stock_sale_price(self, k, p):
        stock = self.record[k]
        if stock != None:
            stock.set_sale_price(p)
            self.record[k] = stock
        else:
            print("%d is no exist"%(k))
    def set_stock_sale_date(self, k, d = datetime.today()):
        stock = self.record[k]
        if stock != None:
            stock.set_sale_date(d)            
            self.record[k] = stock
        else:
            print("%d is no exist"%(k))
    def get_stock(self, id):
        return self.record[id]
    
    def add_stock(self, s):
        k = s.id
        if self.record.get(k) == None:
            self.record[k] = s
        else:
            print("%d is exist"%(k))
    def input_record(self):
        for k in self.record.keys():
            s = self.record[k]
            print("%d %s %d %d %f %s %s %d"%(s.id, s.stock, s.buy, s.sale, s.get_profit(), s.buy_date, s.sale_date, s.get_hold_days()))


buy_stock_list=[]

class StockSaleStrategy:
    def sale_signal_1(self, s, p):#连续上涨后下跌卖出
        pass
if __name__ == "__main__":
    x = StockTradeRecord()
    x.add_stock(StockTradeInfo(0, "000001.sz", 12.1))
    x.set_stock_sale_date(0, datetime(2016, 11, 27))
    x.set_stock_sale_price(0, 14.4)
    x.input_record()
