from PIL import Image, ImageFilter
import multiprocessing
import time
import math
import os

# Превратили папку с список
directory = 'assets'
photos = os.listdir(directory)

def apply_filter(photos_list):
    for image_path in photos:
        img = Image.open(f"assets/{image_path}")
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        output_path = f"apply_filter_{image_path}"
        img.save(output_path)
        return output_path

if __name__ == "__main__": 
    photos = os.listdir(directory)
    # Синхронное вычисление
    start = time.time()
    result = apply_filter(photos)
    sync_time = time.time() - start
    print(f"Синхронное вычисление: {sync_time:.2f} сек")

    process = multiprocessing.Process(target= apply_filter)
    process.start()
    process.join()
    
    mp_time = time.time() - start
    print(f"Многопроцессорное вычисление: {mp_time:.2f} сек")