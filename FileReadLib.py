import os
import numpy as np


def get_array(filename):

    npy_version_exists = os.path.isfile(filename + ".npy")
    if not npy_version_exists:
        txt_to_npy(filename)

    return np.load(filename + ".npy")


def txt_to_npy(filename):

    filepath = os.getcwd() + "\\" + filename + ".txt"
    file_array = open(filepath)

    raw_lines = [x[:-1].split(" ") for x in file_array.readlines()]

    edges = np.array([(int(x),int(y), int(z)) for x, y, z in raw_lines[1:]])

    file_array.close()
    np.save(filename, edges)

