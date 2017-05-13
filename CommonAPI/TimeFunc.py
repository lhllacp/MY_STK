import  time                    
def low_time(src_time, dst_time):
    st = time.strftime(src_time)



if __name__ == "__main__":
    s = time.strptime("13:30:00", "%H:%M:%S")
    t = time.strptime("12:40:00", "%H:%M:%S")
    print(s > t)