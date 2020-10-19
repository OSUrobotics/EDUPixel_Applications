import numpy as np
import cv2

image = "stop.jpg"

def color_detect(image_path, lower, upper):
	bounderies = [([0, 0, lower], [75, 75, upper])]
	# The color order is BGR, so it is 0 ,0, lower and 75, 75, upper
	image = cv2.imread(image_path)
	for (lower, upper) in bounderies:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
		cv2.imshow("Red Detection", np.hstack([image, output, ]))
		cv2.waitKey(0)

color_detect(image, 100, 250)

# # Find most common color code

# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from collections import Counter
# from skimage.color import rgb2lab, deltaE_cie76
# import os

# def RGB2HEX(color):
#     return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


# def get_image(image_path):
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     return image


# def get_colors(image, number_of_colors, show_chart):
    
#     modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
#     modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
#     clf = KMeans(n_clusters = number_of_colors)
#     labels = clf.fit_predict(modified_image)
    
#     counts = Counter(labels)
#     # sort to ensure correct color percentage
#     counts = dict(sorted(counts.items()))
    
#     center_colors = clf.cluster_centers_
#     # We get ordered colors by iterating through the keys
#     ordered_colors = [center_colors[i] for i in counts.keys()]
#     hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
#     rgb_colors = [ordered_colors[i] for i in counts.keys()]

#     if (show_chart):
#         plt.figure(figsize = (8, 6))
#         plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
		
#     return rgb_colors

# get_colors(get_image(image), 8, True)
# plt.show()