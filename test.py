import threading
import time


def download(id):
    current = threading.current_thread()
    print(f"thread #{current.name}: downloading file #{id}")
    time.sleep(1 * id)
    print(f"thread #{current.name}: finished downloading file #{id}")


t = threading.Thread(target=download, args=[1])
t2 = threading.Thread(target=download, args=[2])


t.start()
t2.start()
