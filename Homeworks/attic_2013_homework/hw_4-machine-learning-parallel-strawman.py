#!/usr/bin/env python
"""
AY 250 - Scientific Research Computing with Python
Homework Assignment 4 - Parallel Feature Extraction Example
Author: Christopher Klein, Joshua Bloom
"""
from os import listdir
from multiprocessing import Pool, cpu_count
from pylab import imread
from time import time

## CHANGE THIS NEXT LINE!
MYDIRECTORY = "/Users/jbloom/Classes/ay250-py4sci/week4/50_categories"

# FUNCTION DEFINITIONS
# Quick function to divide up a large list into multiple small lists, 
# attempting to keep them all the same size. 
def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
            newseq.append(seq[int(round(i*splitsize)):
                int(round((i+1)*splitsize))])
        return newseq
# Our simple feature extraction function. It takes in a list of image paths, 
# does some measurement on each image, then returns a list of the image paths
# paired with the results of the feature measurement.
def extract_features(image_path_list):
    feature_list = []
    for image_path in image_path_list:
        image_array = imread(image_path)
        feature = image_array.size # This feature is simple. You can modify this
        # code to produce more complicated features and to produce multiple
        # features in one function call.
        feature_list.append([image_path, feature])
    return feature_list



### Main program starts here ###################################################
# We first collect all the local paths to all the images in one list
image_paths = []
categories = listdir(MYDIRECTORY)
for category in categories:
    image_names = listdir(MYDIRECTORY  + "/" + category)
    for name in image_names:
        image_paths.append(MYDIRECTORY + "/" + category + "/" + name)

print ("There should be 4244 images, actual number is " + 
    str(len(image_paths)) + ".")

# Then, we run the feature extraction function using multiprocessing.Pool so 
# so that we can parallelize the process and run it much faster.
numprocessors = cpu_count() # To see results of parallelizing, set numprocessors
                            # to less than cpu_count().
# numprocessors = 1

# We have to cut up the image_paths list into the number of processes we want to
# run. 
split_image_paths = split_seq(image_paths, numprocessors)

# Ok, this block is where the parallel code runs. We time it so we can get a 
# feel for the speed up.
start_time = time()
p = Pool(numprocessors)
result = p.map_async(extract_features, split_image_paths)
poolresult = result.get()
end_time = time()

# All done, print timing results.
print ("Finished extracting features. Total time: " + 
    str(round(end_time-start_time, 3)) + " s, or " + 
    str( round( (end_time-start_time)/len(image_paths), 5 ) ) + " s/image.")
# This took about 10-11 seconds on my 2.2 GHz, Core i7 MacBook Pro. It may also
# be affected by hard disk read speeds.

# To tidy-up a bit, we loop through the poolresult to create a final list of
# the feature extraction results for all images.
combined_result = []
for single_proc_result in poolresult:
    for single_image_result in single_proc_result:
        combined_result.append(single_image_result)
