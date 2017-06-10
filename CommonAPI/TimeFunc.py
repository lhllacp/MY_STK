import  time
import datetime                
def lt_time(src_time, dst_time):
    return time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), src_time), "%Y:%m:%d:%H:%M:%S") < time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), dst_time), "%Y:%m:%d:%H:%M:%S")

def gt_time(src_time, dst_time):
    return time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), src_time), "%Y:%m:%d:%H:%M:%S") > time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), dst_time), "%Y:%m:%d:%H:%M:%S")

def equal_time(src_time, dst_time):
    return time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), src_time), "%Y:%m:%d:%H:%M:%S") == time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), dst_time), "%Y:%m:%d:%H:%M:%S")
def now_time_lt(dst_time):
    return time.localtime() < time.strptime("%s:%s"%(time.strftime("%Y:%m:%d"), dst_time), "%Y:%m:%d:%H:%M:%S")
def get_now_weekday():
    return datetime.datetime.now().weekday() #0-6
def get_now_time(format = "%Y_%m_%d"):
    return datetime.datetime.now().strftime(format)
if __name__ == "__main__":
    print(now_time_lt("16:45:00"))
    print(get_now_time())
    print(get_now_weekday())
    print(time.strftime("%A"))