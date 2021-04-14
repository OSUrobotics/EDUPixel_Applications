#
#  Use k-means clustering to find the most-common colors in an image
#
import cv2
import numpy as np
from sklearn.cluster import KMeans


def make_histogram(cluster):
    """
    Count the number of pixels in each cluster
    :param: KMeans cluster
    :return: numpy histogram
    """
    numLabels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    hist, _ = np.histogram(cluster.labels_, bins=numLabels)
    hist = hist.astype('float32')
    hist /= hist.sum()
    return hist


def make_bar(height, width, color):
    """
    Create an image of a given color
    :param: height of the image
    :param: width of the image
    :param: BGR pixel values of the color
    :return: tuple of bar, rgb values, and hsv values
    """
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    hsv_bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
    hue, sat, val = hsv_bar[0][0]
    return bar, (red, green, blue), (hue, sat, val)


# START HERE
img = cv2.imread('newImage.png')
height, width, _ = np.shape(img)

# reshape the image to be a simple list of RGB pixels
image = img.reshape((height * width, 3))

# we'll pick the 5 most common colors
num_clusters = 5
clusters = KMeans(n_clusters=num_clusters)
clusters.fit(image)

# count the dominant colors and put them in "buckets"
histogram = make_histogram(clusters)
# then sort them, most-common first
combined = zip(histogram, clusters.cluster_centers_)
combined = sorted(combined, key=lambda x: x[0], reverse=True)

# finally, we'll output a graphic showing the colors in order
bars = []
RGB = []
for index, rows in enumerate(combined):
    bar, rgb, hsv = make_bar(200, 200, rows[1])
    print(f'Bar {index + 1}')
    print(f'  RGB values: {rgb}')
    RGB.append(str(rgb))
    bars.append(bar)

img = np.hstack(bars)
for i in range(len(RGB)):
    img = cv2.putText(img, RGB[i], (5 + (i * 200), 20), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
cv2.imwrite("Common_Color.png", img)

cv2.imshow(f'{num_clusters} Most Common Colors', img)
cv2.waitKey(0)