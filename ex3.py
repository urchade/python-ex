"""ex3.py
Author: Urchade Zaratiana
Matr.Nr.: k11932165
Exercise 3
"""

import glob
import os
import numpy as np
from PIL import Image


class ImageNormalizer():
    def __init__(self, input_dir):

        # store file paths
        paths = glob.glob(os.path.join(input_dir, '**/*.jpg'), recursive=True)

        # Create a dict of path, filename pairs and sort it by filename
        dict_path_name = {k: os.path.split(k)[-1] for k
                          in sorted(paths, key=lambda item: os.path.split(item)[-1])}

        self.file_names = [v for v in dict_path_name.values()]
        self.paths = [v for v in dict_path_name.keys()]

    def get_stats(self):
        means = np.zeros(shape=(len(self.file_names),))
        stds = np.zeros(shape=(len(self.file_names),))

        for i, file in enumerate(self.paths):
            image = np.array(Image.open(file), dtype=np.float64)
            means[i] = image.mean()
            stds[i] = image.std()

        return means, stds

    def get_images(self):
        for file in self.paths:
            image = np.array(Image.open(file), dtype=np.float32)
            yield (image - image.mean()) / image.std()