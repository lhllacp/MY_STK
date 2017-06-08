#coding:utf-8
import urllib.request
from time import sleep
from nt import system
from fileinput import close
stock_code=["600386", "600919","002370", "002403", "603959", "002653", "002113", "002722","300426"];
def code_to_symbol(code):
    if len(code) == 6 :
        return 'sh%s'%code if code[:1] in ['5', '6', '9'] else 'sz%s'%code 
    else:
        return ""
class StockRealTimeData(object):
    EXTEND_HEAD_LIST=['涨幅率','成本价', '盈利', '盈利率']    
    HEAD_LIST=['股票名称', '今开', '昨收', '现价', '最高价', '最低价', '竞买价', '竞卖价', '成交股数', '成交金额', '买一（股）', '买一（价）','买二（股）', '买二（价）','买三（股）', '买三（价）','买四（股）', '买四（价）','买五（股）', '买五（价）', '卖一（股）', '卖一（价）','卖二（股）', '卖二（价）','卖三（股）', '卖三（价）','卖四（股）', '卖四（价）','卖五（股）', '卖五（价）', '日期', '时间']
    def stock_code_dict(self):
        ret_dict={}
        hd = open("StockCode", "r")
        buf_list=hd.readlines();
        for buf in buf_list:
            t=buf.split()
            ret_dict[t[0]] = t[1]
        hd.close();
        return ret_dict
    
    def format_data_head(self, mode=0):
        if mode == 0:
            pass
        elif mode == 1:
            print("%-10s\t%s\t%s\t%s\t%s\t%s"% (self.HEAD_LIST[0], self.HEAD_LIST[3],self.HEAD_LIST[1],self.HEAD_LIST[2],self.HEAD_LIST[4], self.HEAD_LIST[5]))
        elif mode == 2:
            print("%-10s\t%s\t%s\t%s\t%s\t%s\t%s"% (self.HEAD_LIST[0], self.HEAD_LIST[3],self.EXTEND_HEAD_LIST[0],self.HEAD_LIST[1],self.HEAD_LIST[2],self.HEAD_LIST[4], self.HEAD_LIST[5]))
        else:
            pass    
    def format_data(self, data, mode=0):
        data_str=""        
        if len(data) > 0:
            index=data.find("\"")
            data_str=data[index+1:-3]
        if mode == 0:
            print(data_str)
        elif mode == 1:
            data_list=data_str.split(",")
            outbuf="%-10s\t%s\t%s\t%s\t%s\t%s"% (data_list[0],data_list[3],data_list[1],data_list[2],data_list[4],data_list[5])
            print(outbuf)
        elif mode == 2:
            data_list=data_str.split(",")
            outbuf="%-10s\t%s\t%-6.2f\t%s\t%s\t%s\t%s"% (data_list[0],data_list[3],(float(data_list[3]) - float(data_list[2])) / float(data_list[2]) * 100.0, data_list[1],data_list[2],data_list[4],data_list[5])
            print(outbuf)
        else:
            pass   
    def stock_current_price(self, code_list):
        code_str=""
        for i in code_list:
            code_str=code_str + ","+code_to_symbol(i)
        '''
        if(len(code_list) == 1):
            code_str=code_to_symbol(code_list[0])
        else:
            code_str=code_to_symbol(code_list[0])       
            for i in range(1, len(code_list)):
                code_str=code_str + ","+code_to_symbol(code_list[i])
       
        http://hq.sinajs.cn/list=sh600386,sh600386
        '''
        url = 'http://hq.sinajs.cn/list=%s'%code_str
        return urllib.request.urlopen(url).readlines()
       
    def stock_read_time_data(self, mode=1, time=1):
        code_dict=self.stock_code_dict()
        code_list=code_dict.keys()
        while 1:            
            data_list = self.stock_current_price(code_list)
            system("cls")       
            self.format_data_head(mode)        
            for line in data_list:
                self.format_data(str(line.decode('gb2312')), mode)
            sleep(time)
            
if __name__ == "__main__":
    s = StockRealTimeData()
    #s.stock_code_dict()
    s.stock_read_time_data(2)