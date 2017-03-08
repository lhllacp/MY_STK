#coding:utf-8
import urllib.request
import lxml.html
import re
import json
import sys
import os
from CommonAPI.Log import LOG_ERROR


def code_to_symbol(code):
    if len(code) == 6 :
        return 'sh%s'%code if code[:1] in ['5', '6', '9'] else 'sz%s'%code 
    else:
        return "" 
def time_to_second(t):
    t=t.strip(' ')
    t_list=t.split(':')
    return t_list[0] * 3600 + t_list[1] * 60 + t_list[2]



def get_A_stock_code_dict(st=True):
    ''' 
    60XXXX 上海A股
    000XXX 001696 001896 深圳A股
    002XXX  深圳中小板
    300XXX  深圳创业板
    900XXX  上海B股
    200XXX  深圳B股
    '''
    url="http://quote.eastmoney.com/stocklist.html"
    html=urllib.request.urlopen(url).read()
    tree = lxml.html.fromstring(html)
    code_list = tree.xpath("//*[@id='quotesearch']/ul[position()<3]/li[*]/a/text()")
    print(len(code_list))
    code_dict={}
    for code in code_list:
        vk=code.split('(')
        k=vk[1].strip(')')
        v=vk[0]
        if re.match("(^000|^60|^000|^002|^300|001696|001896)", k) != None:
            if re.match("(^\*ST|^ST)", v) == None:
                code_dict[k] = v
    return code_dict


def fiter_stock_code_list(code_list):
    ret_code_list=[]
    for code in code_list:
        if re.match("(^000|^60|^000|^002|^300|001696|001896)", code) != None:
            ret_code_list.append(code)
    return ret_code_list
    
def get_shA_stock_code_list(st=True):
    
    pass




def local_stock_code_list():
    code_list=[]
    fp=open("../resource/stockcode.txt", "r")
    for line in fp.readlines():
        code=line.strip('\n')
        code_list.append(code)
    return code_list







def stock_real_time_data_dict(code_list):
#['股票名称', '今开', '昨收', '现价', '最高价', '最低价', '竞买价', '竞卖价', '成交股数', '成交金额', '买一（股）', '买一（价）','买二（股）', '买二（价）','买三（股）', '买三（价）','买四（股）', '买四（价）','买五（股）', '买五（价）', '卖一（股）', '卖一（价）','卖二（股）', '卖二（价）','卖三（股）', '卖三（价）','卖四（股）', '卖四（价）','卖五（股）', '卖五（价）', '日期', '时间']
    num=len(code_list)
    url=None
    if num == 1:
        url="http://hq.sinajs.cn/list=" + code_to_symbol(code_list[0])
    else:
        for i in range(num):
            if i != 0:
                url=url + ","+ code_to_symbol(code_list[i])
            else:
                url="http://hq.sinajs.cn/list=" + code_to_symbol(code_list[0])   
    data={}
    if url != None:
        try:
            lines=urllib.request.urlopen(url).readlines()
        except:
            LOG_ERROR("open url[%s] failed", os.path.basename(sys._getframe().f_code.co_filename), sys._getframe().f_lineno)
            return None
        else:
            for j in range(len(lines)):
                line=lines[j].decode('GB18030')            
                t=str(line)
                index=t.find("\"")
                v=t[index+1:-3]
                k=code_list[j]
                data[k]=v.split(',')
        
    return data      



def valid_stock_code_list():
    '''
            属于股票，上市  非停牌
    '''
    ret_list=[]
    code_list=local_stock_code_list()
    index=0
    code_list_len=len(code_list)
    while index < code_list_len:
        data_dict=None
        if code_list_len - index < 50:
            data_dict=stock_real_time_data_dict(code_list[index:])
        else:
            data_dict=stock_real_time_data_dict(code_list[index: index + 51])
        index=index + 50
        if data_dict != None:
            for k, v in data_dict.items():
                if len(v) > 1:
                    if v[1] != 0.0:
                        ret_list.append(k)
    return ret_list





def stock_yesterday_close_price(code):    
    data_dict=stock_real_time_data_dict([code])
    try:
        if data_dict != None:
            v=data_dict[code]
            if len(v) != 0:
                return float(v[2])
            else:
                None
        else:
            return None
    except:
        print(data_dict)
        return None
def stock_yesterday_close_price_dict(code_list):
    ret_dict={}
    data_dict=stock_real_time_data_dict(code_list)
    if data_dict != None:
        for k,v in data_dict.items():
            if len(v) != 0:                
                ret_dict[k]=v[2]
            else:
                ret_dict[k]=None
        if len(ret_dict) != len(code_list):
            ret_dict = None
    else:
        ret_dict = None
    return ret_dict
def stock_history_data_day_dict(code):
    #http://api.finance.ifeng.com/akdaily/?code=sz000877&type=last
    data_dict={}
    url="http://api.finance.ifeng.com/akdaily/?code=" + code_to_symbol(code) + "&type=last"
    data=urllib.request.urlopen(url).read().decode()[12:-3]
    data_list=str(data).split("],[")
    for i in data_list:
        i=i.strip("\"")
        i = i.replace("\",\"", " ")
        i = i.replace(",", "")
        i_list=i.split(" ")
        k=i_list[0]
        v=i_list[1:-1]
        data_dict[k]=v
    return data_dict
def stock_history_data_day_list(code):
    #http://api.finance.ifeng.com/akdaily/?code=sz002735&type=last
    #[日期 今开 最高 收盘 最低 成交量  价格变动 涨幅率 5日均价 10日均价 20日均价  5日均量 10日均量  20日均量  换手率]
    data_list=[]
    url="http://api.finance.ifeng.com/akdaily/?code=" + code_to_symbol(code) + "&type=last"
    data=urllib.request.urlopen(url).read().decode()[12:-3]
    d_list=str(data).split("],[")
    for i in d_list:
        i=i.strip("\"")
        i = i.replace("\",\"", " ")
        i = i.replace(",", "")
        data_list.append(i.split(" "))
    return data_list
def stock_history_data_day(code_list, d, t):
    pass

def stock_today_data_min_list(code):
    code_str=code_to_symbol(code)
    url="http://web.ifzq.gtimg.cn/appstock/app/minute/query?code=" + code_str
    data_list=[]
    try:
        data=urllib.request.urlopen(url).read().decode()
        js=json.loads(data) 
        data_list=js["data"][code_str]["data"]["data"]
    except:
        LOG_ERROR("open url[%s] failed")
        return None
    ret_list=[]
    v=0.0
    for i in data_list:
        str_list=i.split(" ")
        t=float(str_list[-1])
        str_list[-1]= t - v
        str_list[-2]=float(str_list[-2])
        v=t
        ret_list.append(str_list)
    return ret_list

def local_stock_history_data_day(code_list, d, t):
    pass
def local_stock_history_minute(code_list, d, t):
    pass
if __name__ == "__main__":
    LOG_ERROR("xxx")
    