
from datetime import date
import threading

class StoreData(object):  
    
    def __init__(self, modename, mode="a+",  v_date=None, path=None):
        if v_date== None:
            v_date = date.today()
        if path == None:
            self.m_filename="%s%s_%s.data"%(r"../resource/", v_date, modename)
        else:
            self.m_filename="%s%s_%s.data"%(path, v_date, modename)
        self.m_fp=open(self.m_filename, mode)
        if self.m_fp == None:
            print("open filename[%s] failed."%(self.m_filename))
            assert(0)
        self.m_lock=threading.Lock()
    def __del__(self):
        if self.m_fp != None:
            self.m_fp.close()
    def record(self, data):
        self.m_lock.acquire()
        self.m_fp.write(data)
        self.m_lock.release()
    def record_list(self, data_list):
        self.m_lock.acquire()
        self.m_fp.writelines(data_list)
        self.m_lock.release()
    def read_list(self):
        return self.m_fp.readline()
        








if __name__ == '__main__':
    x=[]
    x.append(["xxx"])
    x.append(["aaa"])
    print(sorted(x, key=lambda student : student[0]))
    z=0.01000
    print(z)
    print("%.2f"%(z))
    
    
    pass