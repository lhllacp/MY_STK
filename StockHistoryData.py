#coding=gb2312
import urllib.request
from BaseLib import *
class StockHistoryData(object):    
    m_root_dir=""
    m_slash=""
    m_dir_max=100
    m_head_list=['']
    def __init__(self):
        sys_str=platform.system()
        if sys_str == "Windows":
            self.m_root_dir=r"E:\stock\data"
        else:
            self.m_root_dir="/stock/data"
        self.m_slash=get_slash()
    def __get_history_data(self, code):
        url="http://api.finance.ifeng.com/akdaily/?code=%s&type=last" % (code_to_symbol(code))
        data=urllib.request.urlopen(url).read()[12:-3]
        data_list=data.split("],[")
        return data_list    
    def __code_to_dir_name(self, code):
        return "%s%s%d%s%s" % (self.m_root_dir, self.m_slash,  hash(code) % self.m_dir_max, self.m_slash, code)
    def __save_data(self, code, data_list):       
        dir_name=self.__code_to_dir_name(code)
        if os.path.exists(dir_name) == False:
            os.makedirs(dir_name)
        store_data(dir_name, data_list)
    def store_stock_history_data(self, code):
        dir_name=self.__code_to_dir_name(code)
        if os.path.exists(dir_name) == True:
            data_str= read_data(dir_name, -1)
            data_list=self.__get_history_data(code)
            if len(data_str) == 0:
                self.__save_data(code, data_list)
            else:
                index = data_list.index(data_str)
                self.__save_data(code, data_list[index+1:])   
        else:
            assert(0)
if __name__ == "__main__":
    s = StockHistoryData()
    print(s.store_stock_history_data("600386"))
    