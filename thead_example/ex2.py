import threading
import time


def counting(n):
    for i in range(n):
        time.sleep(0.2)
        print(i)

try:
    t = threading.Thread(target=counting, kwargs=dict(n=10))
    t.start()
    t.join()
    print('Thread finish')
except Exception as e:
    print(e.__str__())
