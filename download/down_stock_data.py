
import datetime
import os
import sys
sys.path.append(r"..")
from CommonAPI.StockInfo import stock_today_data_sec_list, get_A_stock_code_list

def get_date_dir():
    return os.path.join("sec",datetime.datetime.now().strftime("%Y_%m_%d"))
def get_file_path(code_str):
    return os.path.join("sec",datetime.datetime.now().strftime("%Y_%m_%d"), code_str)
def down_second_data():
        code_list = get_A_stock_code_list()
        calc =0
        for i in code_list:
            path = get_file_path(i)
            if os.path.exists(path) != True:
                data_list = stock_today_data_sec_list(i)
                fp = open(path, "w+")
                for data in data_list:
                    buf="%s\n"%(data)
                    fp.write(buf)
                fp.close()
            calc = calc+1
            print("%d %d"%(calc, len(code_list)))

            
            
            
            
if __name__ == "__main__":
    down_second_data()