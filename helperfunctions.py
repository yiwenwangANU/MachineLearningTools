import zipfile


def unzip_data(filename):
    """
    Unzip filename into the current directory

    :param filename: a file path to a target file that need to be unzipped
    :return: None
    """
    zip_ref = zipfile.ZipFile(filename, "r")
    zip_ref.extractall()
    zip_ref.close()


import os


def walk_through_dir(dir_path):
    """
    Walk though the dir_path and returns its sub-dirs and files

    :param dir_path: a directory path that need to be walk through
    :return: None
    """
    for dirpath, dirnames, filenames in os.walk(dir_path):
        print(f"Current directory: {dirpath}, number of sub-directories: {len(dirnames)}, "
              f"number of files: {len(filenames)}")


import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def plot_random_image(dir_path, num=3):
    """
    Plot random image within training set or test set with their label

    :param dir_path: a directory path that contains labeled images
    :param num: number of images that going to be plotted, default value is 3
    :return: None
    """
    plt.figure(figsize=(7 * num, 14))
    for i in range(num):
        plt.subplot(1, num, i + 1)
        class_name = random.sample(os.listdir(dir_path), 1)[0]
        img_name = random.sample(os.listdir(os.path.join(dir_path, class_name)), 1)[0]
        img_path = os.path.join(dir_path, class_name, img_name)
        img = mpimg.imread(img_path)
        plt.imshow(img)
        plt.title(class_name)
        plt.axis("off")


import datetime
import tensorflow as tf


def create_tensorboard_callback(dir_name, experiment_name):
    """
    Create the callback of the tensorboard, the experiment callback will be stored
    under the path of dir_name + experiment_name + datetime

    :param dir_name: a directory path that used to store all tensorbaard callbacks
    :param experiment_name: the name of one experiment
    :return: log file of tensorboard callback
    """

    log_dir = dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=log_dir)
    print(f"Saving TensorBoard log files to: {log_dir}")
    return tensorboard_callback

import numpy as np

def plot_loss_curve(history):
    """
    plot the loss curve and accuracy curve during the model training

    :param history: a history file that records loss, val_loss, accuracy and val_accuracy during the model training
    :return: None
    """
    plt.figure(figsize=(20, 7))
    plt.subplot(1, 2, 1)
    plt.plot(np.arange(len(history.history) + 1), history.history["loss"], label="loss")
    plt.plot(np.arange(len(history.history) + 1), history.history["val_loss"], label="val_loss")
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(np.arange(len(history.history) + 1), history.history["accuracy"], label="accuracy")
    plt.plot(np.arange(len(history.history) + 1), history.history["val_accuracy"], label="val_accuracy")
    plt.legend()
