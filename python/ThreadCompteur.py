'''
 Exercice 2 : 
'''
import threading
import time
import random

class threadCompteur (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 10)
      print ("Exiting " + self.name)

def print_time(threadName, counter):
    global position
    while counter:
        delay=random.randint(1,4)
        time.sleep(delay)
        print ("Le thread {0} compteur={1} et sleep={2}".format(threadName, counter,delay))
        counter -= 1
    position+=1    
    print("Le thread {0} termine a la position={1}".format(threadName, position))    
        
# position de fin des thread
position=0;        
# Liste de threads
threads = []
# Create new threads
thread1 = threadCompteur(1, "Thread-1")
thread2 = threadCompteur(2, "Thread-2")
thread3 = threadCompteur(3, "Thread-3")
thread4 = threadCompteur(4, "Thread-4")

# ajoute les threadd dans la liste
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

# Start new Threads
# Demarrer tous les threads .
for t in threads:
    t.start()

# Attendre que tous les threads soient termines.
for t in threads:
    t.join()

print ("Exiting Main Thread")