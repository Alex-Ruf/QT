import  logging

log= logging.getLogger('server')

class Port():
    def __set__(self, instance, value):
        if not 1023 < value< 65536:
            log.critical(f"Ошибка ввода порта {value}, порт не должен быть меньше 1024 и больше 65535 ")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name