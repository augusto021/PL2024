import re

# Somador on/off

# Somador on/off: criar o programa em Python
#     Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
#     Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
#     Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
#     Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.


file_path = "./somador.txt"
with open(file_path,'r') as file:
    text = file.read()


pattern = r'(?i)\b(?:on|off)\b|\d+|='

state_sum = False
sum = 0

for match in re.finditer(pattern,text):
    if match.group().lower() == "off":
        state_sum = False
        sum = 0
    
    elif match.group().lower() == "on":
        state_sum = True
        
    elif match.group() == "=" and state_sum:
        print("= {0}\n".format(sum))

        
    elif state_sum and match.group != "=":
        print('{0}'.format(match.group()))
        sum += int(match.group())