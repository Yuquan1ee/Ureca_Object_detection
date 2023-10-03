## create_json.py 
is used to create a json file which contains all path of the images. I used this file to create the json file for the images in the test and train image files. In total there are 2 JSON files.


## dataset.py (Nothing Done, same as original)
is used to create a class called listdataset. This class gives the property of the dataset used for the model. E.g. len(dataset)

## image.py (Nothing Done, same as original)
this code is a data preprocessing function used to load and prepare image and density map data for a computer vision task, with optional data augmentation for training. It appears to be part of a data preparation pipeline for a machine learning project.

## make_dataset.py 
is used to create the map density files using the .mat file and create the HDF5 files. I used this file to create the HDF5 file for both test and train images.

## model.py (Nothing Done, same as original)
contains the architecture of the neural network

## test.py


## train.py
args.train_json: Replace with the path to your training dataset JSON file.


args.val_json: Replace with the path to your validation dataset JSON file.


args.lr: You can adjust the learning rate if needed.


args.batch_size: Set your desired batch size.


args.epochs: Set the number of training epochs.


args.workers: Set the number of data loader workers.


transforms.Normalize: You can adjust the mean and standard deviation values in the normalization transformation to match your dataset statistics.


Paths to your training and validation images: Modify the paths in img_folder_train and img_folder_test to point to the directories containing your training and validation images.


Model architecture: If you want to use a different model architecture, replace CANNet with your desired model.


Loss function: If you want to use a different loss function, replace nn.MSELoss with your desired loss function.

## utils.py (Nothing Done, same as original)
contains the checkpoint functions to store the latest weights of the model and also load and save the neuralnet