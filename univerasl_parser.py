from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import re
import csv

class Parser:
    def site_parser(self, url: str, name_of_class: str):
        """
            Parsing by class_name
        """
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(10)
        static = driver.find_element(By.CLASS_NAME, f'{name_of_class}')
        print(str(static.text))
        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write(str(static.text))

        driver.quit()

    def sort_for_4_rows(self):
        with open('log.txt', 'r', encoding='utf-8') as file:
            rows = file.readlines()  # Читаем все строки в список

        result = []
        for i, row in enumerate(rows, 1):
            result.append(row.rstrip())  # Убираем лишние переносы
            if re.findall(pattern=r'^\d+$', string=row):  # После каждой строки глазика (количество просмотров) добавляется пробел
                result.append("")  # Добавляем пустую строку

        # Записываем обратно в файл
        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(result)) # Каждой группе элементов в 'тут какая-нибудь инфа'  последобаляется переход на новую строку

    def converter_from_txt_to_csv(self, *headers):
        """
            Конвертирует данные из txt в CSV с указанными заголовками
            
            Args:
                *headers: переменное количество аргументов - названия колонок в порядке их следования
        """
        with open('log.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]  # Убираем пустые строки

        vacancies = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Ищем строку с зарплатой (содержит ₽)
            if '₽' in line:
                # Создаем словарь для вакансии
                vacancy = {}
                
                # Заполняем данные в порядке переданных заголовков
                for j, header in enumerate(headers):
                    if i + j < len(lines):
                        vacancy[header] = lines[i + j]
                    else:
                        vacancy[header] = ""  # Если данных не хватает
                
                vacancies.append(vacancy)
                i += len(headers)  # Переходим к следующей группе данных
            else:
                i += 1  # Пропускаем строки без зарплаты

        # Записываем в CSV
        with open('sorted_vacancies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            if headers:  # Если заголовки переданы
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(vacancies)
            else:  # Если заголовки не переданы, создаем автоматические
                if vacancies:
                    headers_auto = [f"Column_{i+1}" for i in range(len(vacancies[0]))]
                    writer = csv.DictWriter(csvfile, fieldnames=headers_auto)
                    writer.writeheader()
                    writer.writerows(vacancies)


# Сначала парсим данные
# Parser().site_parser("URL", "class_name")
# Parser().site_parser("https://www.farpost.ru/vladivostok/realty/sell_flats/?agentType%5B%5D=agencyFee&agentType%5B%5D=agencyNoFee&agentType%5B%5D=privatePerson#center=131.93457102696428%2C43.09301744760717&zoom=10.364544025632991", "native")
# Сортируем
Parser().sort_for_4_rows()

# Конвертируем в CSV с указанными заголовками в нужном порядке
Parser().converter_from_txt_to_csv("Price", "Price_for_meter", "Info","Location")

# Или с другим количеством заголовков:
# Parser().converter_from_txt_to_csv("Salary", "Position", "Location")
# Parser().converter_from_txt_to_csv("Salary", "Position")