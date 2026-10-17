import os

IMAGE_DIR = ""
MASK_DIR = "C:\\Users\\vivek chauhan\\OneDrive\\Downloads\\liverCTSegmentation\\archive (26).zip\\last_dataset\\masks"

image_files = os.listdir(IMAGE_DIR)
mask_files = os.listdir(MASK_DIR)

print("Number of CT images:", len(image_files))
print("Number of masks:", len(mask_files))