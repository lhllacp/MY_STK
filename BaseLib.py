import os
import platform
FILE_MAX_LINE_NUM=1048576
FILE_LINE_LENGTH=256
def code_to_symbol(code):
        if len(code) == 6 :
            return 'sh%s'%code if code[:1] in ['5', '6', '9'] else 'sz%s'%code 
        else:
            return ""
 
def get_slash():
    sys_str=platform.system()
    if sys_str == "Windows":
        return "\\"
    else:
        return "/"
 
    
def store_data(dir_str, data_list):
    file_num=len(os.listdir(dir_str))
    if file_num != 0:
        file_index=file_num -1
        file_name="%s%s%d" %(dir_str, get_slash(), file_index)
        file_size=os.path.getsize(file_name)
        file_lines= file_size / FILE_LINE_LENGTH
        if file_lines < FILE_MAX_LINE_NUM:
            pass
        elif file_lines == FILE_MAX_LINE_NUM:
            file_index = file_index + 1
            file_lines=0
        else:
            assert(0)
        file_name="%s%s%d" %(dir_str, get_slash(), file_index)
        hd=open(file_name, "ab+")
        for line in data_list:
            hd.write("%-255s\n"%line)
            file_lines=file_lines+1
            if file_lines == FILE_MAX_LINE_NUM:
                hd.close()
                file_index=file_index+1
                file_lines=0
                file_name="%s%s%d" %(dir_str, get_slash(), file_index)
                hd=open(file_name, "ab+")
        hd.close()
    else:
        file_index=0
       
        file_lines=0
        file_hd=None
        for line in data_list:
            if file_hd == None:
                file_name="%s%s%d" %(dir_str, get_slash(), file_index)
                hd=open(file_name, "ab+") 
            hd.write("%-255s\n"%line)
            file_lines=file_lines+1
            if file_lines == FILE_MAX_LINE_NUM:
                hd.close()
                file_index=file_index+1
                file_lines=0
        hd.close()
def read_data(dir_str, line=-1):
    data_str=""
    file_num=len(os.listdir(dir_str))
    if file_num == 0:
        return data_str
    else:
        file_index=file_num -1
        file_name="%s%s%d" %(dir_str, get_slash(), file_index)
        file_size = os.path.getsize(file_name)
        file_offset=0
        if line == -1:
            file_offset=file_size - FILE_LINE_LENGTH            
        else:
            file_lines=file_index * FILE_MAX_LINE_NUM + file_size / FILE_LINE_LENGTH
            if line <= file_lines:
                file_index=(line-1) /  FILE_MAX_LINE_NUM;
                file_line = (line -1) % FILE_MAX_LINE_NUM
                file_offset = file_line *  FILE_LINE_LENGTH
                file_name="%s%s%d" %(dir_str, get_slash(), file_index)
        file_hd = open(file_name, "r")
        file_hd.seek(file_offset)
        data_str=file_hd.readline().strip("\n").strip()
        file_hd.close()    
    return data_str               
if __name__ == "__main__":
    data_list=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
    
    