import numpy as np
import h5py
import os
import scipy.misc
from tqdm import tqdm

def read_db():
    # data path
    path_to_depth = './nyu_depth_v2_labeled.mat'

    # read mat file
    image_db = h5py.File(path_to_depth)
    print('Loaded NYU mat')
    return image_db
    

def extract_ds(image_db):
    # [3, 480, 640]
    data_dir = 'data/training/rgb/'
    gt_dir = 'data/training/depth/'

    if not(os.path.exists(data_dir)):
        os.makedirs(data_dir)
        print('Extracting RGB...')
        for i in tqdm(list(range(image_db['images'].shape[0]))):
            img = image_db['images'][i]
            # transfer channels and transpose
            img_ = np.empty([480, 640, 3])
            img_[:,:,0] = img[0,:,:].T
            img_[:,:,1] = img[1,:,:].T
            img_[:,:,2] = img[2,:,:].T
            scipy.misc.imsave(data_dir + str(i) + '.jpg', img_)
            pass
        print('Done')
    else:
        print("RGB Directory exists. Not extracting")
    
    if not(os.path.exists(gt_dir)):
        os.makedirs(gt_dir)
        print('Extracting Normalized Depths...')
        for i in tqdm(list(range(image_db['depths'].shape[0]))):
            depth = image_db['depths'][i]
            depth_ = np.empty([480, 640, 3])
            depth_[:,:,0] = depth[:,:].T
            depth_[:,:,1] = depth[:,:].T
            depth_[:,:,2] = depth[:,:].T

            depth_norm = depth_/4.0
            scipy.misc.imsave(gt_dir + str(i) + '.png', depth_norm)
            pass
        print('Done')
    else:
        print("Depth Directory exists. Not extracting")
        
    

    
  
# def create_depth_index(image_db):
#     depth = f['depths'][index]

#     # reshape for imshow
#     depth_ = np.empty([480, 640, 3])
#     depth_[:,:,0] = depth[:,:].T
#     depth_[:,:,1] = depth[:,:].T
#     depth_[:,:,2] = depth[:,:].T

#     depth_norm = depth_/4.0
#     return depth_norm