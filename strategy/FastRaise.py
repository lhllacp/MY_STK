#coding:utf-8
import sys
sys.path.append(r"..")

from CommonAPI.StockInfo import local_stock_code_list,stock_real_time_data,time_to_second,\
    fiter_stock_code_list
from GUI.RLCBWidget import  RLCBWidget
from CommonAPI.StockLog import StockLog

global_stock_code_data=local_stock_code_list()

#dictMerged2=dict(dict1, **dict2)




def init_stock_code_data(code_step=50):
    code_data={} 
    '''
    {code:[开盘  最高价   现价 涨幅， 时间]}
    '''
    code_list=local_stock_code_list()
    code_list=fiter_stock_code_list(code_list)   
    t_code_list=[]
    del_code_list=[]
    for code in code_list:
        if len(t_code_list) != code_step:
            t_code_list.append(code)
        if len(t_code_list) == code_step or code == code_list[-1]:
            t_code_data=stock_real_time_data(t_code_list)
            for k, v in t_code_data.items():                
                if len(v) > 1: #暂停上市股票
                    if float(v[1]) != 0.0: #停牌股票
                        rate=(float(v[3]) - float(v[1])) / float(v[1]) * 100.0
                        if rate < 9.0:  #涨停股票不关注
                            data=[v[1], v[4],  v[3], rate, v[-2]]
                            code_data[k] = data
                        else:
                            del_code_list.append(k)
                    else:
                        del_code_list.append(k)
                else:
                    del_code_list.append(k)
            t_code_list=[]
    for code in del_code_list:
        code_list.remove(code)         
    return code_list, code_data

def stock_code_data(code_list, code_step=50):
    '''
    {code:[开盘， 现价，最高价， 涨幅， 时间]}
    '''
    
    code_data={}
    t_code_list=[]
    del_code_list=[]
    for code in code_list:
        if len(t_code_list) != code_step:
            t_code_list.append(code)
        if len(t_code_list) == code_step or code == code_list[-1]:
            t_code_data=stock_real_time_data(t_code_list)
            for k, v in t_code_data.items():
                if v[3] >= v[4] : #当前价格为最高价,
                    rate=(float(v[3]) - float(v[1])) / float(v[1]) * 100.0
                    if rate < 9.0:
                        if rate >= 2.0:
                            data=[v[1], v[4],  v[3],  rate, v[-2]]
                            code_data[k] = data
                    else:
                        del_code_list.append(k)  
            t_code_list=[]
    for code in del_code_list:
        code_list.remove(code)
    return code_data
def fast_raise(global_code_data, code_data, rate=0.5, t=60):
    '''
    {code:[开盘     现价      时间  1  涨幅1  时间2  涨幅2  时间差     涨幅差]}
    '''
    code_dict={}
    for k, v in code_data.items():
        v0=global_code_data[k]
        diff_second = int(time_to_second(v[-1])) - int(time_to_second(v0[-1]))
        diff_raise = v[-2] - v0[-2]
        if diff_raise >= rate and diff_second < 2 * t:
            code_dict[k]=[v[0], v[1], v0[-1], v0[-2], v[-1], v[-2], diff_second, diff_raise]
        if diff_second >= t:  #超过指定时间间隔，更新数据，     
            global_code_data[k] = v
    return code_dict
    
def data_to_str(code_dict):
    str_list=[]
    for k, v in code_dict.items():
        t="%s %s %s %s %.2f %s %.2f %d %.2f"%(k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7])
        print(t)
        str_list.append(t)
    return str_list


def run():
    g_code_list, g_code_data =  init_stock_code_data()
    l=StockLog("FastRaise")
    while True:
        code_data=stock_code_data(g_code_list)
        show_code=data_to_str(fast_raise(g_code_data, code_data))
        if len(show_code) != 0:
            l.add_log(show_code)
        
        #t=["xxx", "bbb"]
        #d=RLCBWidget();
        #d.display(t)

def regression_test():
    
    pass

if __name__ == "__main__":
    run()
    