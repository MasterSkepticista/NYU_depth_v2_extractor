# NYU_depth_v2_extractor
## Instructions

Two files: sketch.py (run this), and helper.py

1. Download the NYU Depth V2 labeled '.mat' file and place in this root directory.
2. Run sketch.py, it will create one dir with two sub dirs of <rgb_image>.jpg and <depth>.png
  
## Note

RGB Images are 'as-is' from the dataset, but the Depth images are 'normalized' by factor of 4. This is because Depth maps drawn from Kinect have pixel values 0-4, 4 representing maximum distance in meters. You can turn off normalization in helper.py, but keep in mind, the images may look black.

## Requirements/Dependencies
```python
from tqdm import tqdm # For progressbar ;)
import h5py           # For .mat files
import helper         # Accompanying file in root directory
