#создадим файл, который будет выводить слово в несколько потоков

from threading import Thread
#т.к. понадобится промежуток между выводами импорт слип
from time import sleep

def script(text, pause):
    # функция выводит text через определенные промежутки времени
    # чтобы не делать прерываний ограничим количество выводов циклом
    for i in range(10):
        print(text)
        sleep(pause)
#создадим многопоточность
thread1 = Thread(target=script, args=("first", 2)) #первый поток выводит текст first 1 раз в 2 сек
thread2 = Thread(target=script, args=("second", 3))

#запускаем поток
thread1.start()
thread2.start()

#закрыть поток по завершению
thread1.join()
thread2.join()