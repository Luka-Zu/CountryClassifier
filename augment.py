import os
from PIL import Image
import random
import re
import sys

data_path = 'compressed_dataset/' # change this according to where you put your data

def random_crop(image):
    width, height = image.size
    left = random.randint(0, width // 2)
    top = random.randint(0, height // 2)
    right = random.randint(width // 2 + 300, width)
    bottom = random.randint(height // 2 + 300, height)
    return image.crop((left, top, right, bottom))

def augment_images():
    new_data_count = 0
    for country in os.listdir(data_path):
        country_path = os.path.join(data_path, country)
        if len(os.listdir(country_path)) < 100:
            images = []
            for img in os.listdir(country_path):
                img_path = os.path.join(country_path, img)
                base = Image.open(img_path)
                images.append(base)
            
            for base in images:
                flipped = base.transpose(Image.FLIP_LEFT_RIGHT)
                flipped.save(country_path + '/' + str(new_data_count) + '.jpg')
                new_data_count += 1

                for i in range(4):
                    cropped = random_crop(base)
                    cropped_flipped = random_crop(flipped)
                    cropped.save(country_path + '/' + str(new_data_count) + '.jpg')
                    new_data_count += 1
                    cropped_flipped.save(country_path + '/' + str(new_data_count) + '.jpg')
                    new_data_count += 1

    print('finished augmenting data. Generated', new_data_count, 'new images')

augment_images()
