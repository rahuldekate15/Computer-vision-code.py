import cv2
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import exposure
image_path = "Earth.jpg"
#image_path = "EileenCollins.jpg"
#image_path = "Bird.jpg"
image = cv2.imread(image_path)
if image is None:
raise ValueError("Image not found, chek image parth")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 2. Apply HOG Feature Extraction
features, hog_image = hog(
gray,
orientations = 9,
pixels_per_cell = (8, 8),
cells_per_block = (2, 2),
block_norm = 'L2-Hys',
visualize=True
)
# Rescale HOG image for better visualization
hog_image_rescaled = exposure.rescale_intensity(hog_image, 
in_range=(0,10))
# 3. Display Results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")
plt.subplot(1,2,2)
plt.title("Hog Feature Visualization")
plt.imshow(hog_image_rescaled, cmap='gray')
plt.axis("off")
plt.tight_layout()
plt.show()
#4.Print Feature Vector Size
print("Hog Feature vector length: ", len(features))
MATLAB Code:
img = imread("Bird.jpg");
[featureVector, hogVisualization] = extractHOGFeatures(img);
figure;
imshow(img)
hold on;
plot(hogVisualization);
