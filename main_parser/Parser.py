from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import re
import csv
from typing import Dict, List, Any
import pytest
from contextlib import contextmanager
from Universal_methods import UM

class Parser:
    def __init__(self):
        self.driver = None
        self.time = UM().time_now()  # Create UM instance to call method
        self.response = None

    def setup_driver(self):
        self.driver = webdriver.Firefox()
        time.sleep(5)
       
    def open_url(self, url):
        if not self.driver:
            self.setup_driver()
        self.driver.get(url)

    def finder_information(self, by: By, selector: str):
        """Find an element given a By strategy and locator."""
        if not self.driver:
            raise RuntimeError("Драйвер не инициализирован")
        self.response = self.driver.find_element(by, selector)
        return self.response
    
    def saver(self):
        if not self.response:
            raise RuntimeError("Нет данных для сохранения")
            
        self.time = UM().time_now()  # Update time
        with open(f'./input_text/{self.time}.txt', 'w', encoding='utf-8') as file:
            file.write(self.response.text)

    def reader_input(self):
        """Read from input file"""
        with open(f'./input_text/{self.time}.txt', 'r', encoding='utf-8') as file:
            return file.readlines()
    
    def sorter(self):
        result = []
        
        for i in self.reader_input():
            row = i.strip()
            if re.search(r'^\d+', row):  # Fixed regex pattern
                result.append(row + '\n')  # Add newline for numbered rows
            else:
                result.append(row)
        return ''.join(result).strip()  # Join all lines and strip extra whitespace
               
    def saver_out(self):
        sorted_content = self.sorter()
        out_file = UM().complicated_file(sorted_content)  # Create UM instance
        
        with open(f'./sorted_text/{self.time}.txt', 'w', encoding='utf-8') as file:
            file.write(str(out_file))

    def reader_output(self):
        """Read from output file"""
        with open(f'./sorted_text/{self.time}.txt', 'r', encoding='utf-8') as file:
            return file.readlines()

    def close_driver(self):
        """Close the browser driver"""
        if self.driver:
            self.driver.quit()
            self.driver = None

    def __del__(self):
        """Cleanup when object is destroyed"""
        self.close_driver()
        

if __name__ == "__main__":
    parser = Parser()
    try:
        parser.setup_driver()
        parser.open_url('https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=privatePerson#center=131.9280759110047%2C43.145646306445585&zoom=13.564544025632976')
        parser.finder_information(By.CLASS_NAME, 'native')
        parser.saver()
        parser.saver_out()
        print("Парсинг завершен успешно!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        parser.close_driver()
