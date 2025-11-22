from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import re
import csv
from typing import Dict, List, Any

class Parser:
    def opener(self, file_for_open: str, mode: str):
        """Proper file opener that returns file object or content based on mode"""
        if 'r' in mode:
            with open(file_for_open, mode, encoding='utf-8') as file:
                return file.read() if mode == 'r' else file
        else:
            return open(file_for_open, mode, encoding='utf-8')
    
    def site_parser(self):
        driver = webdriver.Firefox()
        url = 'https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=privatePerson#center=131.93457102696428%2C43.09301744760717&zoom=10.364544025632991'

        driver.get(url)
        time.sleep(10)

        static = driver.find_element(By.CLASS_NAME, "native")
        a = str(static.text)
        print(a)
        
        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write(str(static.text))

        driver.quit()

    def sort_for_4_rows(self):
        content = self.opener('log.txt', 'r')
        if isinstance(content, str):
            rows = content.split('\n')
        else:
            rows = content.readlines()
            content.close()

        result = []
        for row in rows:
            result.append(row.rstrip())
            if re.findall(pattern=r'^\d+$', string=row):
                result.append("")

        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(result))

    def remover_clean_rows(self, path_to_file: str) -> List[str]:
        """Read file and return cleaned lines without empty rows"""
        content = self.opener(path_to_file, 'r')
        if isinstance(content, str):
            lines = content.split('\n')
        else:
            lines = content.readlines()
            content.close()
        
        # Clean and filter lines
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return cleaned_lines
    
    def 
   
parser = Parser()
parser.sort_for_4_rows()