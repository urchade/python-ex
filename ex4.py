import numpy as np


def ex4(image_array, crop_size, crop_center):
    if not isinstance(image_array, np.ndarray):
        raise ValueError
    if (len(crop_center) != 2) * (len(crop_center) != 2):
        raise ValueError
    if (crop_size[0] % 2 != 0) * (crop_size[1] % 2 != 0):
        raise ValueError

    x_start = int(crop_center[0] - crop_size[0] / 2)
    x_end = int(crop_center[0] + crop_size[0] / 2)
    y_start = int(crop_center[1] - crop_size[1] / 2)
    y_end = int(crop_center[1] + crop_size[1] / 2)

    if (x_start < 20) * (y_start < 20) * (image_array.shape[0] - x_end > 20) * (image_array.shape[1] - y_end > 20):
        raise ValueError

    target_array = image_array[x_start:x_end, y_start:y_end].copy()
    image_array[x_start:x_end, y_start:y_end] = np.zeros_like(target_array)
    crop_array = np.where(image_array != 0.0, image_array ** 0, image_array)

    return image_array, crop_array, target_array