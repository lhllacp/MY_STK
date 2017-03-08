import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *


class PromptMessage(QWidget):
    def __init__(self, parent = None):
        super(PromptMessage,self).__init__(parent)
        self.m_show_tm = QTimer()
        self.m_stay_tm = QTimer()
        self.m_close_tm = QTimer()
        self.m_point = QPoint()
        self.m_stay=2
        
    def set_stay(self, stay):
        self.m_stay = stay    
  
    def show_message(self, message_list):
        self.m_show_tm.timeout.connect(self.on_move)
        layout=QGridLayout()
        num=len(message_list)
        for i in range(num):
            label=QLabel()
            label.setText(message_list[i])
            layout.addWidget(label, i, 0)
        self.setLayout(layout)        

        self.adjustSize()
        rect = QApplication.desktop().availableGeometry()
        rect1 = QApplication.desktop().screenGeometry ()
        self.m_desktop_height=rect.height()
        self.setMaximumSize(rect.width() * 0.1, rect.height() * 0.1)
        self.setWindowFlags(Qt.FramelessWindowHint);
        self.m_point.setX(rect.width() - self.width())
        self.m_point.setY(rect.height() - self.height() - (rect1.height() - rect.height()))
        #self.move(self.m_point)
        self.setWindowOpacity(0.8)      
        self.show()
        self.m_show_tm.start(100)
    def on_move(self):
        self.m_desktop_height = self.m_desktop_height - 10
        self.move(self.m_point.x(), self.m_desktop_height)
        if self.m_desktop_height <= self.m_point.y():
            self.m_show_tm.stop()
            time.sleep(self.m_stay)
            self.close()
  
import sys  
def logs():  
    print(sys._getframe().f_code.co_name)
    print(sys._getframe().f_back.f_code.co_name)
    print(sys._getframe().f_back.f_lineno)
    print(sys._getframe().f_back.f_code.co_filename)
def get_cur_info() :  
    logs() #模拟写日志  
          
if __name__ == "__main__":
    from CommonAPI.Log import LOG_ERROR
    
      