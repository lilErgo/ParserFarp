from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from Universal_methods import UM
import time
import re
import csv


class Parser:
    def __init__(self, url):
        self.url = url
        self.timer = UM().time_now()
      
    def inf(self):
        return print(self.timer)
    
    def inf1(self):
        import time
        time.sleep(2)
        a = self.timer
        a
        return print(a)
par = Parser('cust_url')


par.inf()
par.inf1()