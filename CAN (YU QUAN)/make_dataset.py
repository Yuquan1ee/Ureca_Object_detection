import h5py
import scipy.io as io
import PIL.Image as Image
import numpy as np
import os
import glob
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter
from matplotlib import cm as CM
from image import *

# root is the path to ShanghaiTech dataset
root = "C:\\Pycharm project\\Ureca_Object_detection\\CAN (YU QUAN)\\SHANGHAITECH DATASET"

part_B_train = os.path.join(root, 'part_B', 'train_data', 'images')
part_B_test = os.path.join(root, 'part_B', 'test_data', 'images')
path_sets = [part_B_train, part_B_test]

img_paths = []
for path in path_sets:
    for img_path in glob.glob(os.path.join(path, '*.jpg')):
        img_paths.append(img_path)

for img_path in img_paths:
    print(img_path)
    mat_path = img_path.replace('.jpg', '.mat').replace('images', 'ground-truth').replace('IMG_', 'GT_IMG_')
    mat = io.loadmat(mat_path)
    img = plt.imread(img_path)
    k = np.zeros((img.shape[0], img.shape[1]))
    gt = mat["image_info"][0, 0][0, 0][0]
    for i in range(0, len(gt)):
        if int(gt[i][1]) < img.shape[0] and int(gt[i][0]) < img.shape[1]:
            k[int(gt[i][1]), int(gt[i][0])] = 1
    k = gaussian_filter(k, 15)
    h5_path = img_path.replace('.jpg', '.h5').replace('images', 'ground-truth')
    with h5py.File(h5_path, 'w') as hf:
        hf['density'] = k
