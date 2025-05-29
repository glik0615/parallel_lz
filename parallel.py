from PIL import Image, ImageFilter
import threading
import time

def process_image(path):
    img = Image.open(path)
    img = img.filter(ImageFilter.GaussianBlur(4))
    img.save(f"processed_{path}")
    print(f"Processed{path}")


 #Обычная запись 
    start = time.time()
    for i in range (4):
        process_image(f"Файл №{i}")
    delta = time.time() - start
    print(f"simple time of writing {i+1} files is:{delta}")



    # Многопоточная запись
    start = time.time()
    threads = []
    for i in range (10):
        thread = threading.Thread(target=process_image, args=(f"simple_file{i}.txt","Hello! I'm file №{i}"))
        thread.start()
        threads.append(thread)
    
    for t in threads:
        t.join()

    delta = time.time() - start
    print(f"Время выполнения для файла {i + 1}: {delta}")




if __name__ == '__main__':
    t1 = threading.Thread(target=process_image, args=('img/1.jpg',), daemon=True)
    t2 = threading.Thread(target=process_image, args=('img/2.jpg',), daemon=True)
    t3 = threading.Thread(target=process_image, args=('img/3.jpg',), daemon=True)
    t4 = threading.Thread(target=process_image, args=('img/4.jpg',), daemon=True)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
