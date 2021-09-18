# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:49:11 2021

@author: ridvan.ozdemir

v2:new code is way much shorter
v3:looks nicer
"""

import os
import glob

path = "E:/ridvan_2021/05_PhD/tik_ler/tik_4/R_F_D_v4/"

number_of_pruducts={}

labels = ["sleeper","bolt","head_check","fastening","rail_crack","fastening_rotated_deformed","corrugation","squat","surface_defect"]
# set all object number's value to zero 
 
i=0 
for l in labels:
    number_of_pruducts[l]=0

# read all YOLOv4 format labeling text files in the dataset folder and count object's number    
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(filename, 'r') as f: # open in readonly mode
       for satır in f:
           sinif = satır.split(' ')[0]
           print(sinif)
           i+=1
           number_of_pruducts[labels[int(sinif)]]+=1
    
print(i, "number of total object")
