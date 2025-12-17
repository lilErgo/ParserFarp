# Universal_methods.py
class UM:
    def __init__(self):
        pass

    def complicated_file(self, content: str):
        """
        Process content and organize into groups separated by empty lines
        """
        storage = []
        current_group = []
        
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if line == '':
                if current_group:  # If we have accumulated lines
                    storage.append(current_group)
                    current_group = []
            else:
                current_group.append(line)
        
        # Add the last group if exists
        if current_group:
            storage.append(current_group)
            
        return storage

    @classmethod
    def time_now(cls):
        import time
        """
            Format: "%Hh-%Mm-%Ss %b_%d_%Yy"
        """
        return time.strftime("%Hh-%Mm-%Ss %b_%d_%Yy")
    
    def filer (file:str,mode:str,text = None,encoding = 'utf-8') -> list[str] | None:
        """
            Accepting only 2 modes 'r' or 'w'
            --------------------------------
                if readig return -> list[str]

                    if writing file return none and creating or writing file(if file not exist creating and writing inside him)
        """
        try:
            if mode == 'r':
                with open(file=file,mode = mode,encoding = encoding) as file1:
                    print(f'Reading file file={file} is complite')
                    return file1.readlines()
            elif mode == 'w':
                if text:
                    with open(file=file,mode = mode,encoding = encoding) as file1:
                        print(f'Writing in  file={file} is end ...')
                        return file1.writelines(text)
                else:
                    print('укажите файл')
        except Exception as e:
            print(e)
    def converter_to_csv(list_of_data,headers:list,encoding='ANSI'):
        import csv
        from Universal_methods import UM
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
