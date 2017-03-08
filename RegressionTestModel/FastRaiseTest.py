#coding:utf-8

'''
name:
times:


'''
from datetime import datetime, date, timedelta
from CommonAPI.StockLog import StockLog
from CommonAPI.StockInfo import stock_history_data_day_list
class FastRaiseTest():
    def stock_buy_price_dict(self, day=None):#默认昨天 或者20170215
        price_dict={}
        if day== None:
            day=date.today()- timedelta(days=1)
        log=StockLog("FastRaise", day)
        log_list=log.get_log_list()           
        for line in log_list:
            line_list=line.split(" ")
            k = line_list[0]
            v= price_dict.get(k)
            if v != None:
                if float(line_list[2]) > float(v):
                    price_dict[k] = float(line_list[2])
            else:
                price_dict[k] = float(line_list[2]) 
        return price_dict
    def history_price_list(self,code, begin_day, days=None):
        price_list=[]
        data_list=stock_history_data_day_list(code)
        num=len(data_list)
        for i in range(num):
            index=-1 - i
            data=data_list[index]
            d=datetime.strptime(data[0], "%Y-%m-%d").date()
            if d >= begin_day:
                price_list.insert(0, float(data[3]))
        if days != None:
            price_list=price_list[0:days]
            if len(price_list) < days:
                for i in range(days - len(price_list)):
                    price_list.append(None)
        return price_list
    
    
    def profit_statistics(self, rate_list):

        total_num=0.0
        profit_num=0.0
        loss_num=0.0
        max_profit=0.0
        max_loss=0.0
        sum_profit=0.0
        sum_loss=0.0

        for rate in rate_list:
            if rate != None:
                total_num = total_num + 1.0
                if rate > 0.0:
                    profit_num = profit_num + 1.0
                    sum_profit = sum_profit + rate
                    if max_profit < rate:
                        max_profit = rate
                else:
                    loss_num=loss_num + 1.0
                    sum_loss = sum_loss + rate
                    if max_loss > rate:
                        max_loss = rate
        if profit_num != 0.0:
            avg_profit = sum_profit / profit_num
        if loss_num != 0.0:
            avg_loss = sum_loss / loss_num
        
        return [total_num, profit_num, sum_profit, avg_profit, max_profit, loss_num, sum_loss, avg_loss, max_loss]
                    
    def run(self, d=date.today(), days=5):
        buy_dict=self.stock_buy_price_dict(d)
        tomorrow = d + timedelta(days=1)
        income_list=[]
        for k, v in buy_dict.items():
            price_list=self.history_price_list(k, tomorrow, days)
            price_rate_list=[]
            for price in price_list:
                if price != None:
                    price_rate_list.append((price - v) / v * 100.0)
                else:
                    price_rate_list.append(None)
            income_list.append(price_rate_list)
        for i in range(len(income_list[0])):
            rate_list= [example[i] for example in income_list]
            if rate_list.count(None) != len(rate_list):                
                profit=self.profit_statistics(rate_list)
                print(profit)
                
           
if __name__ == "__main__":
    f=FastRaiseTest()
    d=datetime.strptime("20170213", "%Y%m%d").date()
    f.run(d)