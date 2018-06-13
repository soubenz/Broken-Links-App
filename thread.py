#!/usr/bin/env python
from __future__ import print_function       #should be on the top
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(10)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"
        
        
        
class WebCrawler(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(10)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"