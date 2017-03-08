from datetime  import datetime
class PerformanceStatistics(object):
    def __init__(self, func_name="N/A"):
        self.m_start=datetime.now()
        self.m_func_name=func_name
        self.m_display=True
    def __del__(self):
        if self.m_display:
            self.m_end=datetime.now()
            print("%s cost: %ss"%(self.m_func_name, (self.m_end - self.m_start).seconds))
    def start(self):
        self.m_start=datetime.now()    
    def end(self):
        self.m_end=datetime.now()       
        print("%s cost: %ds"%(self.m_func_name, (self.m_end - self.m_start).seconds))
        self.m_display = False
        