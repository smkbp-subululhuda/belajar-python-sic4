import threading
import time

def print_with_dynamic_sleep(total_iteration):
    # Fungsi berikut akan melakukan print command dengan interval berbeda-beda
    for x in range(total_iteration):
        print("Hello from dynamic-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(x)
def print_with_static_sleep(total_iteration):
    for x in range(total_iteration):
        print("Hello from static-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(2) # fungsi akan berhenti selama 2 detik

if __name__ == "__main__" :
    # membuat thread
    t1 = threading.Thread(target=print_with_dynamic_sleep, args=(5,))
    t2 = threading.Thread(target=print_with_static_sleep, args=(5,))

    # Thread pertama
    t1.start()
    # Memulai thread kedua
    t2.start()
    # tunggu sampai thread 1 dilaksanakan
    t1.join()
    # tunggu sampai thread 2 dilaksanakan
    t2.join()
    # thread selesai
    print("Selesai")