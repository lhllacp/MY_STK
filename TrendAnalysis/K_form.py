#coding:utf-8
from CommonAPI.MathAPI import llv, hhv
'''
O:开盘价
C:收盘价
L:最低价
H:最高加
V:成交量
OL:开盘价列表
CL:收盘价列表
LL:最低价列表
HL:最高价列表
VL：成交量列表

0:
'''
def lxxd(OL, CL, N=5):
    '''
            连续下跌 
    '''
    down=0
    for i in range(N):
        if OL[i] > CL[i]:
            down = down + 1
    if down / N >= 0.8:
        return True
    else:
        return False
def lxsz(OL, CL, N=5):         
    '''
            连续上涨
    '''
    up = 0
    for i in range(N):
        if CL[i] > OL[i]:
            up = up + 1
    if up / N >=0.8:
        return True
    else:
        return False
def czx_or_sdx(O, C, L, H):
    '''
            锤子线:实体很小，处于交易价格顶部，无上影线（或很短），下影线大于实体部分（2-3倍）
        
    '''
    pass
def szx(op, cp, rate=0.5):
    '''
            十字星：开盘价与收盘价几乎相等
    '''
    if abs(op - cp ) / op * 100.0 <= rate:
        return True
    else:
        return False

def cbst(OL, CL, L, H, rate=0.5):
    '''
            长白实体：开盘价在最低价附近，收盘价在最高价附近，且收盘价明显高于开盘价，明确意义上的它的实体长度应该是前一天的3倍
    '''
    O0=OL[-1]
    O1=OL[-2]
    C0=CL[-1]
    C1=CL[-2]
    
    if szx(O0, C0) == True:
        return False
    
    if (O0 - L)/L * 100.0 <=rate and (H - C0) / H * 100 <=rate:
        if ((C0 - O0)/O0) / ((abs(C1 - O1)) /O1) >= 3:
            return True
        else:
            return False
    else:
        return False
        
        
def cbst_djq(OL, CL, L, H):
    '''
            低价区长白实体：出现在低价区，底部见底信号，趋势反转
    '''
    if lxxd(OL, CL) and cbst(OL, CL, L, H):
        return True
    else:
        return False
def cbst_qrzc(OL, CL, LL, HL):
    '''
            长白实体确认支撑：长白实体由支撑位（趋势线，移动平均线，价格回调区等重要支撑位）向上反弹，显示多头强劲
    '''
    pass

def cbst_tpzl(OL, CL, LL, HL):
    '''
            长白实体突破阻力：证明势头强劲
    '''
    pass   
    
def cbst_gczc(OL, CL, LL, HL):
    '''
            长白实体构成支撑:
    '''
    pass
def chst(OL, CL, L, H, rate=0.5):
    '''
            长黑实体
    '''
    O0=OL[-1]
    C0=CL[-1]
    O1=OL[-2]
    C1=CL[-2]
    if szx(O0, C0) == True:
        return False
    
    if (O0 - L)/L * 100.0 <=rate and (H - C0) / H * 100 <=rate:
        if ((O0 - C0)/O0) / ((abs(C1 - O1)) /O1) >= 3:
            return True
        else:
            return False
    else:
        return False
def chst_gjq(OL, CL, L, H):
    '''
            高价区长黑实体：长黑实体长度明显大于此前几个根
    '''
    
    
    

    
    
    
    
    
    
K_form_func_dict={0:czx_or_sdx,1:szx,2:cbst}
k_dict={0:0, 1:0, 2:0}
if __name__ == '__main__':
    pass