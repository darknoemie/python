import threading
import time
import random


class ThreadCompteur(threading.Thread):
    def __init__(self, threadid, max_count):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = f"Toto-{self.threadID}"
        self.max_count = max_count

    def run(self):
        global threads_order
        print(f"{self.name} is starting to count until {self.max_count}")
        for current_count in range(self.max_count):
            # print(f"{self.name}: {current_count}")
            timing = random.random()
            time.sleep(timing)
        threads_order.append(self.name)
        order = len(threads_order)
        print(
            f"{self.name} has ending to count until {self.max_count} in {order} position"
        )


threads_order = []
threads_list = []

for nb_thread in range(5):
    # thread = threadCompteur(nb_thread, random.randint(0, 10)) # Random max counter
    thread = ThreadCompteur(nb_thread, 10)
    thread.start()
    threads_list.append(thread)

for t in threads_list:
    t.join()

print("End of all counter")
