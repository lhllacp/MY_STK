'''
Created on 2017年1月18日

@author: Administrator
'''
import urllib.request
import time
def code_to_symbol(code):
    if len(code) == 6 :
        return 'sh%s'%code if code[:1] in ['5', '6', '9'] else 'sz%s'%code 
    else:
        return ""
def code_to_url(code_list, step=50):
    num=len(code_list)
    i=0
    j=0
    k= i + j * step
    url_list=[]
    while k < num:
        url=None
        for i in range(step):
            k=i + j * step
            if k < num:
                if i != 0:
                    url=url + ","+code_to_symbol(code_list[k])
                else:
                    url="http://hq.sinajs.cn/list=" + code_to_symbol(code_list[k])
            else:
                break
        if url != None:
            url_list.append(url)
        i=0
        j=j+1
        
    return url_list

'''
http://hq.sinajs.cn/list=sh600386,sh600386
HEAD_LIST=['股票名称', '今开', '昨收', '现价', '最高价', '最低价', '竞买价', '竞卖价', '成交股数', '成交金额', '买一（股）', '买一（价）','买二（股）', '买二（价）','买三（股）', '买三（价）','买四（股）', '买四（价）','买五（股）', '买五（价）', '卖一（股）', '卖一（价）','卖二（股）', '卖二（价）','卖三（股）', '卖三（价）','卖四（股）', '卖四（价）','卖五（股）', '卖五（价）', '日期', '时间']
'''           
def stock_real_time_data(url_list):
    data=[]
    for url in url_list:  
        lines=urllib.request.urlopen(url).readlines()
        for line in lines:
            t=str(line.decode('gb2312'))
            index=t.find("\"")
            data.append(t[index+1:-3])
    return data


if __name__ == "__main__":
    stock_code=["600386", "600919","002370", "002403", "603959", "002653", "002113", "002722","300426", "600386", "600919","002370", "002403", "603959", "002653", "002113", "002722","300426","600386", "600919","002370", "002403", "603959", "002653", "002113", "002722","300426", "600386", "600919","002370", "002403", "603959", "002653", "002113", "002722","300426"];
    url_list=code_to_url(stock_code, 50)
    #a1=datetime.datetime.now().microsecond
    a1=time.time()
    data=stock_real_time_data(url_list)
    #a2=datetime.datetime.now().microsecond
    a2=time.time()
    #print(a1)
    #print(a2)
    print(a2 -a1)
    #for i in data:
    #    print(i)
    
        