from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

class Parser:
    def site_parser(self):

        driver = webdriver.Firefox()
        url = 'https://www.farpost.ru/vladivostok/rabota/vacansii/+/%D0%9C%D0%BE%D0%B9%D1%89%D0%B8%D0%BA/#center=131.9884223925729%2C43.16019500841343&zoom=11.530948807087961'

        driver.get(url)
        time.sleep(10)

        static = driver.find_element(By.CLASS_NAME, "native")

        a = str(static.text)
        print(a)
        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write(str(static.text))

        driver.quit()

    def sort_for_4_rows(self):
        import re
        with open('log.txt', 'r', encoding='utf-8') as file:
            rows = file.readlines()  # Читаем все строки в список

        result = []
        for i, row in enumerate(rows, 1):
            result.append(row.rstrip())  # Убираем лишние переносы
            if re.findall(pattern=r'^\d+$',string=row):  # После каждой строки глазика (количество просмотров) добавляется пробел
                result.append("")  # Добавляем пустую строку

        # Записываем обратно в файл
        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(result)) # Каждой группе элементов в 'тут какая-нибудь инфа'  последобаляется переход на новую строку

    def converter_from_txt_to_csv(self):
        import re
        import csv

        with open('log.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            i = 0
            
            vacancies = []
            while i < len(lines):
                line_pivot = lines[i]
                if re.search(pattern=r'[^a-zA-Z]\d₽',string=line_pivot):
                    salary = line_pivot
                    position = lines[i + 1] if i + 1 < len(lines) else ""
                    location = lines[i + 2] if i + 2 < len(lines) else ""
                    other_info = lines[i + 3] if i + 3 < len(lines) else ""

                    vacancy = {
                        'salary': salary,
                        'position': position,
                        'location': location,
                        'other_info': other_info
                    }
                    vacancies.append(vacancy)
                    i += 3

                else:
                    i += 1

        with open('sorted_vacancies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['salary', 'position', 'location', 'other_info']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for vacancy in vacancies:
                writer.writerow(vacancy)

Parser().site_parser()
Parser().sort_for_4_rows()
Parser().converter_from_txt_to_csv()