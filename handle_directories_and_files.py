import os


def CreateDirectory(path):
    if not str(path):
        raise Exception('Please enter path of directory')

    # Create directory if not exist
    if not os.path.isdir(path):
        os.mkdir(path)
    # if not os.path.isdir(path+"/temp"):
    #     os.mkdir(path+"/temp")
