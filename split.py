import glob
import os
current_dir = r"images"  # PATH TO IMAGE DIRECTORY

# Percentage of images to be used for the valid set
val_split = 10
num_img = len([name for name in os.listdir(
    current_dir) if os.path.isfile(os.path.join(current_dir, name))])

# Create train.txt and valid.txt
file_train = open('train.txt', 'w')
file_test = open('valid.txt', 'w')

# Populate train.txt and valid.txt
split = round(num_img / val_split)
counter = 1

for file in glob.iglob(os.path.join(current_dir, '*.jpg')):
    title, ext = os.path.splitext(os.path.basename(file))
    if counter <= split:
        counter += 1
        file_test.write("yolo-mobil/" + current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write("yolo-mobil/" + current_dir + "/" + title + '.jpg' + "\n")