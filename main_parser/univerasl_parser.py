

class Parser:
    def __init__(self, url:str):
        self.url = url
        self.driver = None   

    def setUP(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
                
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)
        # self.driver.minimize_window()
        return self.driver
        
    def settings(self,setting_driver):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
    
        set_page = setting_driver.find_element(By.CSS_SELECTOR,'.tabsSearchForm.viewport-padding-collapse')
        # Поиск вкладки количество комнат и нажатие на неё 
        in_set_page = set_page.find_element(By.CSS_SELECTOR,'[data-url-label="kolichestvo-komnat"]')
        in_set_page.click()
        # Настройка - включение фильтров(Количество комнат)
        # Первая колонка
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'Гостинка')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'Студия')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'1-комнатная')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'2-комнатная')]").click()
        # Вторая колонка
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'3-комнатная')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'4-комнатная')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'5-комнатная')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'6 комнат и более')]").click()
        # Третья колонка
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'Доля')]").click()
        in_set_page.find_element(By.XPATH,"//a[contains(text(),'Комната')]").click()
        # Переход на вкладку - цена
        page_price= set_page.find_element(By.CSS_SELECTOR,'[data-url-label="cena"]')
        page_price.click()
        # Взаимодействие с окном - минимальная цена
        waiter = WebDriverWait(setting_driver, 10).until(EC.presence_of_element_located((By.ID, 'price_min')))
        waiter.click()
        waiter.clear()
        waiter.send_keys('12')
        # Переход на владку - продавца
        page_seller = set_page.find_element(By.CSS_SELECTOR,'[data-url-label="prodavec"]')
        page_seller.click()
        # Взаимодейсв с вкладкой - продавец
        page_seller.find_element(By.XPATH,"//a[contains(text(),'Собственник')]").click()
        page_seller.find_element(By.XPATH,"//a[contains(text(),'Агентство без комиссии')]").click()
        page_seller.find_element(By.XPATH,"//a[contains(text(),'Агентство с комиссией')]").click()
        page_seller.find_element(By.XPATH,"//a[contains(text(),'Застройщик')]").click()
        import time
        time.sleep(8)
        self.driver = setting_driver
        return setting_driver

    def start(self):
        from selenium.webdriver.common.by import By
        import re

        driver = self.driver
        
        elements = driver.find_elements(By.CSS_SELECTOR,'[data-source="actual"]')
        result = []
        for element in elements:
            
            location = element.find_element(By.CSS_SELECTOR,'[data-role="bulletin-link"]').text.replace('\n',' ')if element.find_element(By.CSS_SELECTOR,'[data-role="bulletin-link"]').text != None else 'не указанно'
            price = element.find_element(By.CSS_SELECTOR,'[data-role="price"]').text.replace('\n',' ').replace('₽',' руб')  if element.find_element(By.CSS_SELECTOR,'[data-role="price"]').text != None else 'не указанно'
            price_for_cubemetr = element.find_element(By.CLASS_NAME, 'bull-item__additional-price').text.replace('\n',' ').replace('₽',' руб')  if element.find_element(By.CLASS_NAME, 'bull-item__additional-price').text != None else 'не указанно'
            annotations = element.find_element(By.CLASS_NAME,"bull-item__annotation").text.replace('\n',' ').replace('₽',' руб')
            views = re.sub(r'сегодня в \d{1,2}:\d{2}\s*', '', element.find_element(By.CLASS_NAME,'ellipsis-text__right-side').text).strip() if '\n' in element.find_element(By.CLASS_NAME,'ellipsis-text__right-side').text else element.find_element(By.CLASS_NAME,'ellipsis-text__right-side').text     
                
            stack = [location,price,price_for_cubemetr,annotations,views]
            result.append(stack)
            assert not None in stack
        return result

    def converter_to_csv(self,list_of_data,headers:list,encoding='ANSI'):
        import csv
        from Universal_methods import UM
        import sys

        """
                can change encoding by default use ANSI for auto exel
            """

        with open(f'{UM.time_now()}.csv','w',encoding=encoding,newline='') as csv_file:
            """
                can change encoding by default use ANSI for auto exel
            """
            writter = csv.writer(csv_file)
            writter.writerow(headers)
            for row in list_of_data:
                writter.writerow(row)
        self.driver.close()
        sys.stdout.write('Задача выполнена')
        import time
        time.sleep(3)
        sys.exit(0)

    
par = Parser('https://www.farpost.ru/vladivostok/realty/sell_flats/#center=131.92590272211407%2C43.16087466658294&zoom=10.897218500958004')
par.settings(par.setUP())
par.converter_to_csv(par.start(),['Локация','Цена','Цена за кв\м','аннотация','просмотры'])

