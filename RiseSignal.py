def fast_rise(data, n, r):
    '''
    name: fast rise signal
    in:data  -历史数据
       n     -时间周期n内的上涨率
       r     -上涨幅度r，按百分比计算
    out: 是否符合上涨条件
    ''' 
    num=len[data]
    if num < 2:
        return False
    elif num < n:
        n=num
    index=num - n
    for i in range(n):
        t1=data[index + i]
        t2=data[index + i + 1]
        if (t2 - t1) / t1  < r:
            return False
    return True
def func(x, y):
    print(x + y)

FUNC_NAME_DICT={0:fast_rise}
FUNC_ARG_DICT={0:3}
if __name__ == "__main__":
    pass
