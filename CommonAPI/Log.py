from datetime import date
import sys, os, time
G_LOG_INFO    =4
G_LOG_DEBUG   =2
G_LOG_ERROR   =1
G_LOG_NO      =0

class Log(object):
    __instance=None
    def __new__(self, *args, **kwargs):
        if Log.__instance == None:
            Log.__instance = object.__new__(self, *args, **kwargs)
            self.m_path="%s%s_%s.log"%(r"../resource/", date.today(), "All")
            self.m_fp=open(self.m_path, "a+")
            if self.m_fp == None:
                print("open filename[%s] failed."%(self.m_path))
                assert(0)
            self.m_log_level=G_LOG_ERROR | G_LOG_DEBUG
        return Log.__instance
                     
    def __del__(self):
        if self.m_fp != None:
            self.m_fp.close()
    
   
    def __write_log__(self, level,  buf, filename, lineno):
        self.m_fp.seek(0, 2)
        t=time.strftime("%H:%M:%S", time.localtime())
        line="%s:%s:%s--%s:%s\n"%(t, level, buf, filename, lineno)
        self.m_fp.write(line)
        self.m_fp.flush()
    def __write_log_list__(self, level,  buf_list, filename, lineno):
        self.m_fp.seek(0, 2)
        t=time.strftime("%H:%M:%S", time.localtime())
        for buf in buf_list:
            line="%s:%s:%s--%s:%s\n"%(t, level, buf, filename, lineno)
            self.m_fp.write(line)
        self.m_fp.flush()

    def set_log_name(self, filename, v_date=None, path=r"../resource/"):
        if v_date == None:
            v_date = date.today()
        t="%s%s_%s.log"%(path, v_date, filename)
        if t != self.m_path:
            self.m_path = t
        if self.m_fp != None:
            self.m_fp.close()
        self.m_fp = open(self.m_path, "a+")
        if self.m_fp == None:
            print("open filename[%s] failed."%(self.m_path))
            assert(0)
    def set_log_level(self, level):
        self.m_log_level = level
        
    def INFO_LOG(self, buf, filename, lineno):
        if self.m_log_level & G_LOG_INFO  == G_LOG_INFO:
            self.__write_log__("INFO", buf, filename, lineno)
    def DEBUG_LOG(self,  buf, filename, lineno):
        if self.m_log_level & G_LOG_DEBUG  == G_LOG_DEBUG:
            self.__write_log__("DEBUG", buf, filename, lineno)
    def ERROR_LOG(self,  buf, filename, lineno):
        if self.m_log_level & G_LOG_ERROR  == G_LOG_ERROR:
            self.__write_log__("ERROR", buf, filename, lineno)
            
    def INFO_LOG_LIST(self,  buf_list, filename, lineno):
        if self.m_log_level & G_LOG_INFO  == G_LOG_INFO:
            self.__write_log_list__("INFO", buf_list, filename, lineno)
    def DEBUG_LOG_LIST(self,  buf_list, filename, lineno):
        if self.m_log_level & G_LOG_DEBUG  == G_LOG_DEBUG:
            self.__write_log_list__("DEBUG", buf_list, filename, lineno)
    def ERROR_LOG_LIST(self,  buf_list, filename, lineno):
        if self.m_log_level & G_LOG_ERROR  == G_LOG_ERROR:
            self.__write_log_list__("ERROR", buf_list, filename, lineno)
        
def LOG_INFO(buf):
    Log().INFO_LOG(buf, os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_lineno)
def LOG_INFO_LIST(buf_list):
    Log().INFO_LOG_LIST(buf_list, os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_lineno)
def LOG_DEBUG(buf):
    Log().DEBUG_LOG(buf, os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_lineno)
def LOG_DEBUG_LIST(buf_list):
    Log().DEBUG_LOG_LIST(buf_list, os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_lineno)
def LOG_ERROR(buf):
    Log().ERROR_LOG(buf, os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_lineno)
def LOG_ERROR_LIST(buf_list):
    Log().ERROR_LOG_LIST(buf_list, os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_lineno)
def SET_LOG_NAME(filename, v_date=None, path=r"../resource/"):
    Log().set_log_name(filename, v_date, path)
def SET_LOG_LEVEL(level):
    Log().set_log_level(level)

if __name__ == '__main__':
   SET_LOG_NAME("XX")
   LOG_ERROR("xxx")

    