"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

import ipaddress
from subprocess import PIPE, Popen



def ip_address(ip4):
    subnet = ipaddress.ip_network(ip4)
    return list(subnet.hosts())



def host_ping(list_ip):
    dict_ip_addres = {'Узел доступен': "",'Узел недоступен': ""}
    for ip in list_ip:
        
        p = Popen(f"ping {ip} -n 1 -w 300", shell=False, stdout =PIPE)
        p.wait()

        if p.returncode==0:
            print(f"{ip} - Узел доступен")
            dict_ip_addres["Узел доступен"] += f"{str(ip)}\n"
        else:
            print(f"{ip} - Узел недоступен")
            dict_ip_addres["Узел недоступен"] += f"{str(ip)}\n"
        
    return dict_ip_addres
       

if __name__ =='__main__':

    addres = '192.168.0.0/24'
    host_ping(ip_address(addres))
