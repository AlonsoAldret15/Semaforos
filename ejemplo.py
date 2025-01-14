import threading
import time

#crear un semáforo con un contador inicial de 2 
semaphore = threading.semaphore(2)

def tarea(id)
    print(f"Tarea {id} intentando acceder al recurso")
    with semaphore:
        print(f"Tarea {id} ha adquirido el semáforo")
        time.sleep(2)
        print(f"Tarea {id} ha liberado el semáforo")
        
# Crear múltiples hilos que ejecuten la función `tarea`
threads = []
for i in range(5):
    thread = threading.Thread(target = tarea, args=(i,))
    threads.appened(thread)
    thread.start()
#Esperar a que todos los hilos terminen 
for thread in threads:
    thread.join()
