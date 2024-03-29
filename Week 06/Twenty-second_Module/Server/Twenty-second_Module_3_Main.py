""" object processor """


import glob
import shutil
import os

from matplotlib.widgets import EllipseSelector


source_path = "../Source/*"
destination_path = "../Destination"

postfix = [1, 2, 3]

while True:
    source_object = glob.glob(source_path)
    # print(source_object)

    if len(source_object) > 0:
        object_path = source_object[0]
        shutil.copy(object_path, ".")

        object_name = object_path.split("/")[-1].split(".")
        prefix = object_name[0]
        postfix = object_name[1]
        # print(object_name)
        # print(type(object_name))

        for item in range(len(postfix)):
            filename = f"{prefix}_{str(item)}.{postfix}"
            print(filename)
            shutil.copy(object_path, f"{destination_path}/{filename}")

        os.remove(object_path)
        os.remove(object_path.split("/")[-1])
