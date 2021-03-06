# Step 1: Import the packages
from keras.models import model_from_json
import cv2
import numpy as np
import os

def setup():
	json_file = open('./model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)

	loaded_model.load_weights("./model.h5")
	print("Loaded model from disk")

	loaded_model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics= ['accuracy'])

setup()

def predict(image):
	"""directory = '/Users/prajwalseth/Desktop/Programming/CNN/all3/test/'
	# Step 5: load the image you want to test
	for filename in os.listdir(directory):
		image = cv2.imread(str(directory+filename))
		image = cv2.resize(image, (50,50))
		image = image.reshape(1, 50, 50, 3)

		#cv2.imshow("Input Image", image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		# Step 6: Predict to which class your input image has been classified
		"""
		result = loaded_model.predict_classes(image)
		print(result)
