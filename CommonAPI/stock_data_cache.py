#coding:utf-8
class day_stock_data(object):
    '''
                股票日数据信息
    '''
    m_open=None
    m_close=None
    m_high=None
    m_close=None

    def get_open(self):
        return self.m_open
    def get_close(self):
        return self.m_close
    def get_high(self):
        return self.m_high
    def get_low(self):
        return self.low
    
    
class minute_stock_data():
    '''
             股票分时数据
    '''
    m_open=None
    m_close=None
    m_high=None
    m_close=None

    def get_open(self):
        return self.m_open
    def get_close(self):
        return self.m_close
    def get_high(self):
        return self.m_high
    def get_low(self):
        return self.low
    def get_last_open(self):
        if self.m_open is None:
            return None
        return self.m_open[-1]
    def get_last_close(self):
        if self.m_close is None:
            return None
        return self.m_close[-1]
    def get_last_high(self):
        if self.m_high is None:
            return None
        return self.m_high[-1]
    def get_last_low(self):
        if self.self.low is None:
            return None
        return self.low[-1]