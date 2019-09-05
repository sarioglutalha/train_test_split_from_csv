import pandas as pd
import numpy as np
import os
import random
import csv


CSV_DIR   = # INPUT CSV DIRECTORY
DATA_DIR  = # INPUT IMAGES DIRECTORY
TEST_DIR  = # INPUT TEST FOLDER DIRECTORY
TRAIN_DIR = # INPUT TRAIN FOLDER DIRECTORY

test = []
train = []

df = pd.read_csv(CSV_DIR)
test.append(df.columns)
train.append(df.columns)


for img in os.listdir(DATA_DIR):
	if random.random() < .2:
		os.rename(DATA_DIR + img, TEST_DIR + img)
	else:
		os.rename(DATA_DIR + img, TRAIN_DIR + img)
print("image test-train done.")


for row in df.values:
	TEST_IMAGE  = TEST_DIR  + row[0]
	TRAIN_IMAGE = TRAIN_DIR + row[0]

	if(os.path.isfile(TEST_IMAGE)):
		row[0] = TEST_IMAGE
		test.append(row[:])
	if(os.path.isfile(TRAIN_IMAGE)):
		row[0] = TRAIN_IMAGE
		train.append(row[:])
print("csv test-train done.")

print('Creating csv files.')
with open("test.csv", "w", newline="") as b:
	writer = csv.writer(b)
	writer.writerows(test)

with open("train.csv", "w", newline="") as b:
	writer = csv.writer(b)
	writer.writerows(train)

print('done.')
