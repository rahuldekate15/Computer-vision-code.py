import cv2
import numpy as np
from matplotlib import pyplot as plt
# Read input image
image = cv2.imread('nature.jpg')
if image is None:
print("Error: Image not found!")
exit()
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)
print("Number of keypoints detected:", len(keypoints))
output = cv2.drawKeypoints(image, keypoints, None,
flags=cv2.DRAW_MATCHES_FLAGS_DRAW_
RICH_KEYPOINTS)
# Display the result
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("SIFT Keypoints")
plt.axis("off")
plt.show()
