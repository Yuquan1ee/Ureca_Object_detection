import json
import os
import glob

if __name__ == '__main__':
    # Path to folder that contains train images
    root = "C:\\Pycharm project\\Ureca_Object_detection\\CAN (YU QUAN)\\SHANGHAITECH DATASET"
    img_folder_train = os.path.join(root, 'part_B', 'train_data', 'images')

    # Path to the final JSON file for train data
    output_json_train = os.path.join(root, 'part_B', 'train_data', 'img.json')

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_json_train), exist_ok=True)

    img_list_train = []

    for img_path in glob.glob(os.path.join(img_folder_train, '*.jpg')):
        img_list_train.append(img_path)

    with open(output_json_train, 'w') as f_train:
        json.dump(img_list_train, f_train)

    # Path to folder that contains test images
    img_folder_test = os.path.join(root, 'part_B', 'test_data', 'images')

    # Path to the final JSON file for test data
    output_json_test = os.path.join(root, 'part_B', 'test_data', 'img.json')

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_json_test), exist_ok=True)

    img_list_test = []

    for img_path in glob.glob(os.path.join(img_folder_test, '*.jpg')):
        img_list_test.append(img_path)

    with open(output_json_test, 'w') as f_test:
        json.dump(img_list_test, f_test)