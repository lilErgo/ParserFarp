from typing import Dict, Tuple, List, Any

def remover_clean_rows(self, path_to_file:str):
    with open(f'{path_to_file}', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
    return lines

def converter_from_txt_to_csv(self, dict_of_patterns_and_headers:dict , path_to_file:str):
    import csv
    import re
    """
        Конвертирует данные из txt в CSV с указанными заголовками
        
        Args:
            *headers: переменное количество аргументов - названия колонок в порядке их следования
    """
        # Убираем пустые строки
    vacancies = []
    nonlocal vacancies
    
    i = 0
    lines = remover_clean_rows(f'{path_to_file}')
    while i < len(lines):
        line = lines[i]
        vacancy = {i:None for i in headers}
        # Ищем строку с зарплатой (содержит паттерн)
        if re.search(pattern=[pattern for pattern in patterns_for_headers],string=line):
            # Создаем словарь для вакансии
    headers = []
    for header, paterns in dict_of_patterns_and_header:
        headers.append(header)
        
    writer_to_csv(headers)
                


                
                
                
def writer_to_csv(self,headers):
        import csv
        nonlocal vacancies
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


