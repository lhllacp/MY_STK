#coding:utf-8
from multiprocessing.dummy import Pool
import threading
import sys
from CommonAPI.Log import LOG_INFO, SET_LOG_NAME, LOG_DEBUG
sys.path.append(r"..")
from CommonAPI.MathAPI import ema, hhv,  LAST
from CommonAPI.StockInfo import stock_today_data_min_list, stock_yesterday_close_price, valid_stock_code_list
from CommonAPI.StoreData import StoreData
from CommonAPI.TimeFunc import  now_time_lt, get_now_weekday
'''
HJ_1:=EMA(CLOSE,12)-EMA(CLOSE,26);
HJ_2:=EMA(HJ_1,9);
HJ_3:=(HJ_1-HJ_2)*2;
HJ_4:=HJ_3>0 AND HJ_1>0 AND HJ_2>0;
HJ_5:=HOUR=10 AND MINUTE=0;
HJ_6:=HHV(HIGH,30);
HJ_7:=BARSLAST(HJ_5);
HJ_8:=REF(HJ_6,HJ_7);
HJ_9:=CONST(HJ_8);
HJ_10:=CLOSE;
HJ_11:=EMA(CLOSE,37);
HJ_12:=HJ_10>HJ_9 AND REF(HJ_10<=HJ_9,1) AND HJ_10>HJ_11;
HJ_13:=FILTER(HJ_12,HJ_7);
HJ_14:=DYNAINFO(3);
HJ_15:=HJ_10<=HJ_14*1.04 AND HJ_10>HJ_14;
DRAWICON(HJ_4 AND HJ_13 AND HJ_15 AND HJ_8>HJ_14,HJ_9,34);

HJ_1赋值:收盘价的12日指数移动平均-收盘价的26日指数移动平均
HJ_2赋值:HJ_1的9日指数移动平均
HJ_3赋值:(HJ_1-HJ_2)*2
HJ_4赋值:HJ_3>0 AND HJ_1>0 AND HJ_2>0
HJ_5赋值:小时=10 AND 分钟=0
HJ_6赋值:30日内最高价的最高值
HJ_7赋值:上次HJ_5距今天数
HJ_8赋值:HJ_7日前的HJ_6
HJ_9赋值:HJ_8的最后一日取值设为常数
HJ_10赋值:收盘价
HJ_11赋值:收盘价的37日指数移动平均
HJ_12赋值:HJ_10>HJ_9 AND 1日前的HJ_10<=HJ_9 AND HJ_10>HJ_11
HJ_13赋值:HJ_12的HJ_7日过滤
HJ_14赋值:前收盘价
HJ_15赋值:HJ_10<=HJ_14*1.04 AND HJ_10>HJ_14
当满足条件HJ_4ANDHJ_13ANDHJ_15ANDHJ_8>HJ_14时,在HJ_9位置画34号图标
'''


class TimeShareBuy(object):
    def __init__(self, code):
        self.m_code=code
        self.m_filter_len=0
        self.m_len=30  #10:00
        self.m_init=False
        self.m_cl=[]
        self.m_calc=0   #1分钟内无法处理完成，需要从上一次计算位置开始计算
        self.m_ema12=[]
        self.m_ema26=[]
        self.m_ema37=[]
        self.m_hj1=[]
        self.m_hj2=[]
        self.m_hj3=[]
        self.m_hj6=[]
        self.m_hj11=[]
        self.m_yesterday_close= stock_yesterday_close_price(self.m_code)
        if self.m_yesterday_close == None:
            assert(0)
    def display(self):
        print(self.m_ema12)
        print(self.m_ema26)
        print(self.m_hj1)
        print(self.m_hj2)
        print(self.m_hj3)
        print(self.m_hj6[30])
        print(self.m_cl)
        print(self.m_cl[60:75])
    def filter(self, CL):
        try:
            x = CL[-1]
            self.m_cl.append(x)
            if self.m_init:            
                e = self.m_ema12[-1]
                self.m_ema12.append(ema(e, x, 12))
                e = self.m_ema26[-1]
                self.m_ema26.append(ema(e, x, 26))
               
                self.m_hj1.append(self.m_ema12[-1] - self.m_ema26[-1])
                e = self.m_hj2[-1]
                self.m_hj2.append(ema(e, self.m_hj1[-1], 9))
                self.m_hj3.append((self.m_hj1[-1] - self.m_hj2[-1]) * 2)
            
                self.m_hj6.append(hhv(LAST(CL, 30)))
                e = self.m_hj11[-1]
                self.m_hj11.append(ema(e, x, 37))
            else:
                self.m_init = True
                self.m_ema12.append(ema(0, x, 12))
                self.m_ema26.append(ema(0, x, 26))
               
                self.m_hj1.append(self.m_ema12[-1] - self.m_ema26[-1])
                self.m_hj2.append(ema(0, self.m_hj1[-1], 9))
                self.m_hj3.append((self.m_hj1[-1] - self.m_hj2[-1]) * 2)
            
                self.m_hj6.append(x)
                self.m_hj11.append(ema(0, x, 37))
        except:
            print(CL)
            
            
        cl_len=len(CL)
        if cl_len < self.m_len:
            return None  

        if not (self.m_hj1[-1] > 0.0 and self.m_hj2[-1] > 0.0 and self.m_hj3[-1] >0.0):
            LOG_INFO("%d %f %f %f %f "%(cl_len, CL[-1], self.m_hj1[-1], self.m_hj2[-1], self.m_hj3[-1]))
            return None
        
        
        HJ_7 = cl_len - self.m_len
        HJ_8 = self.m_hj6[-HJ_7]
        if (cl_len - self.m_filter_len) < (self.m_filter_len - self.m_len):            
            return None       
        if not (CL[-1] > HJ_8 and CL[-2] <= HJ_8 and self.m_hj11[-1] <= CL[-1]):
            LOG_INFO("%d %f %f %f %f "%(cl_len, CL[-1], CL[-2], HJ_8, self.m_hj11[-1]))         
            return None
        
        
        if not(CL[-1] <= self.m_yesterday_close * 1.04 and CL[-1] > self.m_yesterday_close):
            return None
        self.m_filter_len = cl_len
        if cl_len <= 121:
            t=(cl_len + 30) / 60 + 9
            m=(cl_len + 30) % 60
        else:
            t=(cl_len-122) / 60 + 13
            m=(cl_len-122) % 60 
        #时间    股票    当前价格
        ret=[]
        ret.append("%d:%02d"%(t, m))
        ret.append("%s"%(self.m_code))
        ret.append("%.2f"%(CL[-1]))
        LOG_INFO("%d:%d\t%s\t%.2f"%(t, m, self.m_code, CL[-1]))
        return ret       
    def run(self):
        LOG_DEBUG("code:%s"%(self.m_code))
        ret=None
        data_list=stock_today_data_min_list(self.m_code)
        if data_list != None:
            price_list=[x[1] for x in data_list]
            data_len=len(price_list)
            while self.m_calc < data_len: 
                self.m_calc=self.m_calc + 1
                CL=price_list[0:self.m_calc]
                ret=self.filter(CL)  
        return ret      
                
        
        
class TimeShareBuyModel(object):
    def __init__(self):
        self.m_A_stock_code_list=valid_stock_code_list()
        self.m_object_list=[]
        for code in self.m_A_stock_code_list:
            self.m_object_list.append(TimeShareBuy(code))
        self.m_data=[]
        self.m_lock=threading.Lock()
    def thread_func(self, obj):
        data = obj.run()
        if data != None:
            self.m_lock.acquire()
            self.m_data.append(data)
            self.m_lock.release()
    def store(self, data_list):
        s=StoreData("TimeShareBuyModel", "a+")
        for i in data_list:
            buf="%s\t%s\t%s"%(i[0], i[1], i[2])
            s.record(buf)
            print(buf)
            
    def run(self):
        while True:
            threads_pool = Pool(10)
            threads_pool.map(self.thread_func, self.m_object_list)
            threads_pool.close()
            threads_pool.join()
            if len(self.m_data) != 0:
                t=sorted(self.m_data, key=lambda v : v[0])
                self.store(t)
                self.m_data.clear()
            if now_time_lt("15:00:00") == False or get_now_weekday() >= 5:
                print("---------finished-------------")
                break
            
        #for obj in self.m_object_list:
            #obj.run()
        
 
    
if __name__ == "__main__":
    SET_LOG_NAME("TimeShareBuyModel")
    model=TimeShareBuyModel()
    model.run()
    #t=TimeShareBuy("603239")
    #t.run()
    #t.display()
    
    
