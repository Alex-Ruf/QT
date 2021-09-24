"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

import ipaddress
from task_1 import host_ping

def host_range_ping():
    while True:
        try:
            ip_addres = input("Введите ip адрес:")
            octet = int(ip_addres.split('.')[3])
            break
        except Exception as e:
            print(e)
    
    while True:
        
        num = input(f"Введите количество адресов(max доступно - {254-octet}): ")

        if not num.isnumeric():
            print(f"Ошибка ввода, введено {num} не число! ")
        else:
            if( octet + int(num) )> 254:
                print("Превыщение адресов")
            else:
                break

    ip_list=[]

    for i in range(int(num)):
        ip_list.append(str(ipaddress.ip_address(ip_addres)+ int(i)))
        

    return ( host_ping(ip_list))
    

if __name__=='__main__':
    host_range_ping()

    