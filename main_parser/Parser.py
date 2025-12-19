
        

def settings():
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=developerSingleOffer&agentType%5B%5D=privatePerson&flatType%5B%5D=3&flatType%5B%5D=4&flatType%5B%5D=5&flatType%5B%5D=6&flatType%5B%5D=room&flatType%5B%5D=share&price_min=10#center=131.60544974410524%2C43.35096183327793&zoom=7.807221638306754')
    set_page = driver.find_element(By.CSS_SELECTOR,'.tabsSearchForm.viewport-padding-collapse')
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
    waiter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'price_min')))
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


    
    
    

print(settings())