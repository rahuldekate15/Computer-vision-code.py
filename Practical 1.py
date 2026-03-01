img = imread("colorFlower.jpg");
% Display the grayscale image
grayImg = rgb2gray(img);
%Inverted Image
invertedImg = 255 - grayImg;
%Log Transfrormation
c = 1; % constant for log transformation
logImg = c * log(1 + double(grayImg));
%Power Law Transfrormation
gamma = 2.5; % gamma value for power law transformation
powerLawImg = c * (double(grayImg) .^ gamma);
%Display all images in single figure except original image
figure;
subplot(2, 2, 1), imshow(grayImg), title('Grayscale Image');
subplot(2, 2, 2), imshow(invertedImg), title('Inverted Image');
subplot(2, 2, 3), imshow(logImg, []), title('Log Transformation');
subplot(2, 2, 4), imshow(powerLawImg, []), title('Power Law 
Transformation');
