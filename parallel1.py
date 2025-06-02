# Импортируем необходимые для работы библиотеки
from PIL import Image, ImageFilter
import threading
import time
import os

# Превратили папку с список
directory = 'assets'
photos = os.listdir(directory)

class Par1():
    pass
    def process_image(photos):
        for path in photos:
            img = Image.open(f"assets/{path}")
            img = img.filter(ImageFilter.GaussianBlur(4))
            img.save(f"assets/{path}")
            print(f"assets/{path}")

    #Обычная запись 
        start = time.time()
        for i in range (4):
            process_image(f"Фото №{i}")
        delta = time.time() - start
        print(f"Время для работы с фото{i+1}:{delta}")

    # Многопоточная запись
    start = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=process_image, args=(f"{i}.jpg"))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    thread_time = time.time() - start
    print(f"Многопоточная запись: {thread_time:.2f} сек")

def main():
    if __name__ == "__main__":
        main()




