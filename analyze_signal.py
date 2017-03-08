import random
import sys


CANDLE_FORM_CODE_TO_NAME={0:"NULL", 1:"tsgx", 2:"czx"}
CANDLE_FORM_NAME_TO_CODE={"NULL":0, "tsgx":1, "czx":2}
class candle_form(object):
    def __init__(self, op, cp, hp, lp):
        self.m_open=op
        self.m_close=cp
        self.m_high=hp
        self.m_low=lp
    
    def tsgx(self):
        '''
                            潭水杆线:无上影线，下影线至少是实体部分3倍
        '''
        code = 0
        if self.m_open == self.m_high:
            if (self.m_close - self.m_low) / (self.m_close - self.m_open) > 3.0:
                code = CANDLE_FORM_NAME_TO_CODE["tsgx"]        
        return code
    def czx(self):
        '''
                            锤子线
        '''
        code = 0
        if self.m_open == self.m_high:
            x=(self.m_close - self.m_low) / (self.m_close - self.m_open)
            if  x <= 3.0 and x >=2.0:
                code = CANDLE_FORM_NAME_TO_CODE["czx"]        
        return code
        
    






















def   save(text):
        sys.stdout.write(text)
        sys.stdout.flush()
class stock_data(object):
    def __init__(self, stock_code, cycle, unit):
        self.m_stock_code=stock_code
        self.m_cycle=cycle
        self.m_unit=unit
        self.m_close_list=None
        self.m_open_list=None
        self.m_high_list=None
        self.m_low_list=None
        self.m_volume_list=None
    def get_stock_code(self):
        return self.m_stock_code
    def get_close_list(self):
        if self.m_close_list == None:
            t=[]
            for i in range(1, self.m_cycle + 1):
                t.append(i*3)
            self.m_close_list = t
        return self.m_close_list
    def get_open_list(self):
        if self.m_open_list == None:
            t=[]
            for i in range(1, self.m_cycle + 1):
                t.append(i*2);
            self.m_open_list=t
        return self.m_open_list
    def get_high_list(self):
        if self.m_high_list == None:
            t=[]
            for i in range(1, self.m_cycle + 1):
                t.append(i*4)
            self.m_high_list=t
        return self.m_high_list
    def get_low_list(self):
        if self.m_low_list == None:
            t=[]
            for i in range(1, self.m_cycle + 1):
                t.append(i*1)
            self.m_low_list = t
        return self.m_low_list
    def get_volume_list(self):
        if self.m_volume_list == None:
            t=[]
            for i in range(1, self.m_cycle + 1):
                t.append(i*1)
            self.m_volume_list = t
        return self.m_volume_list
    def get_open(self):
        if self.m_open_list == None:
            self.get_open_list()
        return self.m_open_list[-1]
    def get_close(self):
        if self.m_close_list == None:
            self.get_close_list()
        return self.m_close_list[-1]
    def get_high(self):
        if self.m_high_list == None:
            self.get_high_list()
        return self.m_high_list[-1]
    def get_low(self):
        if self.m_low_list == None:
            self.get_low_list()
        return self.m_low_list[-1]
    def get_volume(self):
        if self.m_volume_list == None:
            self.get_volume_list()
        return self.m_volume_list[-1]
    def print_debug(self):
        save("--------------stock data----------\n")
        save("%s\n"%self.m_stock_code)
        save("%s\n"%self.m_cycle)
        save("%s\n"%self.m_unit)
        save("%s\n"%self.get_open_list())
        save("%s\n"%self.get_close_list())
        save("%s\n"%self.get_high_list())
        save("%s\n"%self.get_low_list())
        
class stock(object):
    def __init__(self, stock_code, buy_price, cycle):
        self.m_signal = None
        self.m_buy_price=buy_price
        self.m_days=0
        self.m_cycle= cycle
    def is_over_statistics(self):
        if self.m_days == self.m_cycle:
            return True
        else:
            return False 
    def get_profit(self, price):
        profit_rate= (price - self.m_buy_price) / self.m_buy_price * 100
        self.m_days = self.m_days + 1
        return profit_rate, self.m_days
    def get_signal(self):
        return None


SIGNAL_TREND={0:"NOT", 1:"UP", 2:"DOWN"}
SIGNAL_VERIFY={0:"FALSE", 1:"TRUE", 2:"recommend"}
SIGNAL_TYPE={0:"R-", 1:"R+", 2:"continue" }
class signale_base(object):
    def __init__(self, s_name,s_type, s_trend, s_verify):
        self.m_name= s_name
        self.m_type = s_type
        self.m_trend = s_trend
        self.m_verify = s_verify
        self.m_frequency=0
    def print_debug(self):
        save("Name:%s\t Type:%s\n"%(self.m_name, SIGNAL_TYPE[self.m_type]))
        save("Trend:%s\t Verify:%s\n"%(SIGNAL_TREND[self.m_trend], SIGNAL_VERIFY[self.m_verify]))
class xtdj(signale_base):
    def __init__(self):
        signale_base.__init__(self, "xtdj", 1, 1, 1)
    #def print_debug(self):
    #   signale_base.print_debug(self)
    pass
class analyze_stock_signal(object):
    def __init__(self, stock_code):
        self.m_stock_data=stock_data(stock_code, 10, "1d")        
    def get_signal(self):        
        pass
    def print_debug(self):
        self.m_stock_data.print_debug()

class signal_statement(object):
    def __init__(self, s, cycle):
        self.m_name = s
        self.m_cycle= cycle
        self.m_occurrences = {}
        self.m_up={}
        self.m_down={}
        self.m_avg_profit_rate= {}
        self.m_max_profit_rate= {}
        self.m_min_profit_rate= {}
        for i in range(1, self.m_cycle + 1):
            self.m_avg_profit_rate[i] = 0.0
            self.m_max_profit_rate[i] = 0.0
            self.m_min_profit_rate[i] = 0.0
            self.m_occurrences[i] = 0.0
            self.m_up[i] = 0.0
            self.m_down[i] = 0.0
        
    def input_profit(self, cycle, profit_rate):
        if profit_rate > self.m_max_profit_rate[cycle]:
            self.m_max_profit_rate[cycle] = profit_rate
        if profit_rate < self.m_min_profit_rate[cycle]:
            self.m_min_profit_rate[cycle] = profit_rate
        self.m_occurrences[cycle] = self.m_occurrences[cycle] + 1
        self.m_avg_profit_rate[cycle] =   (self.m_avg_profit_rate[cycle]*(self.m_occurrences[cycle] - 1) + profit_rate) / self.m_occurrences[cycle]
        if profit_rate > 0.0:
            self.m_up[cycle] = self.m_up[cycle] + 1
        else:
            self.m_down[cycle] = self.m_down[cycle] + 1
        
        
    def print_statement(self):
        save("Name:%s\t"%(self.m_name))        
        save("\nmax:\t")
        for i in range(1, self.m_cycle + 1):
            save("%-.3f\t"%self.m_max_profit_rate[i])      
        save("\nmin:\t")
        for i in range(1, self.m_cycle + 1):
            save("%-.3f\t"%self.m_min_profit_rate[i])

        
        save("\nAVG:\t")
        for i in range(1, self.m_cycle + 1):
            save("%-.3f\t"%self.m_avg_profit_rate[i])

        
        save("\nmin:\t")
        for i in range(1, self.m_cycle + 1):
            save("%-.3f\t"%self.m_min_profit_rate[i])

        save("\nup:\t")
        for i in range(1, self.m_cycle + 1):
            up_rate= self.m_up[i] / self.m_occurrences[i]
            save("%-.3f\t"%up_rate)

        save("\ndown:\t")
        for i in range(1, self.m_cycle + 1):
            down_rate= self.m_down[i] / self.m_occurrences[i]
            save("%-.3f\t"%down_rate)
        save("\n")
class statistics_result(object):
    
    pass

if __name__ == "__main__":
    cycle=10
    x=signal_statement("dfada", cycle)   
    for i in range(0, 10000):
        r=random.randint(-10, 10) / 100.0
        for i in range(1, cycle + 1):
            x.input_profit(i, r)
        #print(r)
        
    x.print_statement()
    t = xtdj()
    t.print_debug()
    pass
    