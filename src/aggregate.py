import os
from PIL import Image
import numpy as np
import pickle
import math


# Path of data folder
DATA_PATH = "TrainingDataset/TrainingDataset/TrainingData"
IMAGE_FOLDER = "Images"
TD_FOLDER = "TD_FixMaps"
ASD_FOLDER = "ASD_FixMaps"
IMAGE_PATH = os.path.join(DATA_PATH, IMAGE_FOLDER)
TD_PATH = os.path.join(DATA_PATH, TD_FOLDER)
ASD_PATH = os.path.join(DATA_PATH, ASD_FOLDER)

print("Getting image paths...", end=None)
# Get all image file paths
IMAGE_image_paths = [fn for fn in os.listdir(IMAGE_PATH)]
TD_image_paths = [fn.replace(".png", "_s.png") for fn in IMAGE_image_paths]
ASD_image_paths = TD_image_paths
print("Finished getting image paths.\r")

# Load data from fixmaps
def read_fixmap(impath):
	with Image.open(os.path.join(impath)) as im:
		return np.resize(np.array(im.getdata(band=0)), (im.size[1], im.size[0]))

print("Getting image data...", end=None)
# Load all the image data
IMAGE_images = [Image.open(os.path.join(IMAGE_PATH, fn)).convert("L").getdata(band=0) for fn in IMAGE_image_paths]
TD_images = [read_fixmap(os.path.join(TD_PATH, fn)) for fn in TD_image_paths]
ASD_images = [read_fixmap(os.path.join(ASD_PATH, fn)) for fn in ASD_image_paths]
print("Finished getting image data.\r")

# Average brightness calculator
# Assumes that the images are already converted to grayscale
def mean_brightness(image):
	return (sum(image) / len(image)) / 255

# Get weighted center of fix map
def weighted_center(image):
	center_X = 0
	center_Y = 0
	divisor = 0

	for y, row in enumerate(image):
		for x, col in enumerate(row):
			center_X += x * (image[y][x] / 255)
			center_Y += y * (image[y][x] / 255)
			divisor += image[y][x] / 255

	center_X /= divisor
	center_Y /= divisor

	return (center_X, center_Y)

# Get weighted variance of the fix map
def weighted_variance(image):
	mean = weighted_center(image)
	dist_var = 0
	divisor = 0

	for y, row in enumerate(image):
		for x, col in enumerate(row):
			dist_var += math.sqrt(((mean[1] - y) ** 2) + ((mean[0] - x) ** 2)) * (image[y][x] / 255)
			divisor += image[y][x] / 255

	dist_var /= divisor

	return dist_var

# Get variance of the brightness
# Assumes flat grayscale
def variance_brightness(image):
	return np.var(image)

print("Filtering image data...")
try:
	with open("image_data.bin", "rb") as f:
		image_data = pickle.load(f)
except:
	image_data = {}

if "im_brightness" not in image_data:
	image_data["im_brightness"] = [mean_brightness(im) for im in IMAGE_images]
	print("Finished im_brightness")
if "td_center" not in image_data:
	image_data["td_center"] = [weighted_center(im) for im in TD_images]
	print("Finished td_center")
if "asd_center" not in image_data:
	image_data["asd_center"] = [weighted_center(im) for im in ASD_images]
	print("Finished asd_center")
if "td_var" not in image_data:
	image_data["td_var"] = [weighted_variance(im) for im in TD_images]
	print("Finished td_var")
if "asd_var" not in image_data:
	image_data["asd_var"] = [weighted_variance(im) for im in ASD_images]
	print("Finished asd_var")
if "im_var" not in image_data:
	image_data["im_var"] = [variance_brightness(im) for im in IMAGE_images]
	print("Finished im_var")

print("Finished filtering image data.")

with open("image_data.bin", "wb") as f:
	pickle.dump(image_data, f)

print(image_data)
