from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import re
import csv
from typing import Dict, List, Any
import pytest
from contextlib import contextmanager

class Parser:
    def __init__(self):
        self.driver = None
        
        self.response = None
    # def driver(self):
    #     browser_driver = webdriver.Firefox()

    #     yield browser_driver

   
    def setup_driver(self):
        self.driver = webdriver.Firefox()
        time.sleep(5)
       
    def open_url(self, url):
        self.driver.get(url)

    
    def finder_information(self, by: By, selector: str):
        """Find an element given a By strategy and locator.

        Parameters:
        -----------
        by : selenium.webdriver.common.by.By
            The locating strategy to use. Default is `By.ID`. Supported values include:
            - By.ID: Locate by element ID.
            - By.NAME: Locate by the `name` attribute.
            - By.XPATH: Locate by an XPath expression.
            - By.CSS_SELECTOR: Locate by a CSS selector.
            - By.CLASS_NAME: Locate by the `class` attribute.
            - By.TAG_NAME: Locate by the tag name (e.g., "input", "button").
            - By.LINK_TEXT: Locate a link element by its exact text.
            - By.PARTIAL_LINK_TEXT: Locate a link element by partial text match.
            - RelativeBy: Locate elements relative to a specified root element.

        Example:
        --------
        element = driver.find_element(By.ID, 'foo')

        Returns:
        -------
        WebElement
            The first matching `WebElement` found on the page.
        """
        if not self.driver:
            raise RuntimeError("Драйвер не инициализирован")
        self.response = self.driver.find_element(by, selector)
        return self.response
    
    def time_now(self):
        """
            Формат:
            ------

                "%Hh-%Mm-%Ss %b_%d_%Yy
        """
        import time 
        
        row = time.strftime("%Hh-%Mm-%Ss %b_%d_%Yy")
        return row

    def saver(self):
        with open(f'.\input_text\{self.time_now()}.txt','w',encoding='utf-8') as file:
            file.write(self.response.text)

    def reader(self):
        with open('input_text\\16h-48m-42s Dec_07_2025y.txt','r',encoding='utf-8') as file:
            return file.readlines()
    
    def sorter(self):
        import re       
        
        result = []

        
        for i in self.reader():
            row = i.strip()
            if re.search(r'^\d+$', row):
                row += '\n'
                result.append(row)
            else:
                result.append(row)
        return  '\n'.join(result)
               
    def saver_out(self):
        with open(f'.\sorted_text\{self.time_now()}.txt','w',encoding='utf-8') as file:
            file.write(self.sorter())

    def reader(self):
        with open('.\sorted_text\\21h-32m-20s Dec_08_2025y.txt','r',encoding='utf-8') as file:
            return file.readlines()

    def sorter_text(self):
        fro
        for i 
        
        
              
        
        
            

    

    def append_to_dict(self):
        import re
        

        dict_of_headers = {
            'ruble' : [],
            'other': []
        }

        reader = self.reader()
        
        for lines in reader:
            
            start = re.search(pattern=r"[0-9 ]+₽$",string=lines)
            if start:
                changed_line = lines.replace('\n','')
                dict_of_headers['ruble'].append(changed_line)
                continue
            if not start:
                
                dict_of_headers['other'].append(lines)
            end = re.search(pattern=r'^\d+$',string=lines)
            if end:
                dict_of_headers['other'].append('\n')
                continue
            if len(lines) < 0:
                break
            
        return dict_of_headers
    
    
                
    

        
        


   
        
        

parser = Parser()
# parser.time_now()
# parser.saver()
# parser.setup_driver()
# parser.open_url('https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=privatePerson#\
#                  center=131.9280759110047%2C43.145646306445585&zoom=13.564544025632976')
# parser.finder_information(By.CLASS_NAME,'native')
# parser.saver()
# parser.reader()
parser.sorter()
parser.saver_out()
# parser.saver_after_sorter()
# parser.append_to_dict()
# parser.information_convert_to_csv()





















    # def opener(self, file_for_open: str, mode: str):
    #     """Proper file opener that returns file object or content based on mode"""
    #     if 'r' in mode:
    #         with open(file_for_open, mode, encoding='utf-8') as file:
    #             return file.read() if mode == 'r' else file
    #     else:
    #         return open(file_for_open, mode, encoding='utf-8')
    
    # def site_parser(self):
    #     driver = webdriver.Firefox()
    #     url = 'https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=privatePerson#center=131.93457102696428%2C43.09301744760717&zoom=10.364544025632991'

    #     driver.get(url)
    #     time.sleep(10)

    #     static = driver.find_element(By.CLASS_NAME, "native")
    #     a = str(static.text)
    #     print(a)
        
    #     with open('log.txt', 'w', encoding='utf-8') as file:
    #         file.write(str(static.text))

    #     driver.quit()

    # def sort_for_4_rows(self):
    #     content = self.opener('log.txt', 'r')
    #     if isinstance(content, str):
    #         rows = content.split('\n')
    #     else:
    #         rows = content.readlines()
    #         content.close()

    #     result = []
    #     for row in rows:
    #         result.append(row.rstrip())
    #         if re.findall(pattern=r'^\d+$', string=row):
    #             result.append("")

    #     with open('log.txt', 'w', encoding='utf-8') as file:
    #         file.write('\n'.join(result))




    # def import_to_csv(self):
    #     import csv
        
    #     with open(f'{self.time_now()}.csv', 'w')  as csv_file:
    #         writer = csv.writer(csv_file)
            

    # def time_now(self):
    #     import time 
    #     timer_now = time.ctime(time.time())
    #     row = timer_now[4:19] + timer_now[22:25]
    #     row = row + ' year'
    #     row_time = row.replace(' ','_')
    #     return row_time


# parser.sort_for_4_rows()
# parser.setup_url('https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=privatePerson#center=131.93457102696428%2C43.09301744760717&zoom=10.364544025632991')

