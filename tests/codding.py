import re



with open('tests\\re.txt','r',encoding='utf-8') as file:
    readed_file = file.readlines()

for line in readed_file:
    line = line.rstrip('\n')

    find = re.findall(r'^\d+$',line)
    if find:
        line += '\n999\n'

    money = re.search(r'₽',line)
    if money:
        a = line[:money.span()[1]] + '\n' 
        b = line[money.span()[1]:]
        line = a + b
    
        
        
        
    
    
        
            
    print(line)