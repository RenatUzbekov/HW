from time import sleep
import threading
from threading import Lock
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):

        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            transfer = randint(50, 500)
            self.balance += transfer
            print(f'Пополнение{transfer}. Баланс{self.balance}')

            sleep(0.001)

    def take(self):

        for i in range(100):
            transfer = randint(50, 500)
            print(f'Запрос на {transfer}')
            if transfer >= self.balance:
                self.balance -= transfer
                print(f'Снятие {transfer}. Баланс {self.balance}')
            else:
                print(f'Запрос отклонен , недостаточно средств')
                self.lock.acquire()
            sleep(0.001)




bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
