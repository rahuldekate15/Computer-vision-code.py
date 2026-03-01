img = imread("colorFlower.jpg");
%Display original Image
figure;
imshow(img);
title('Original Image');
%Apply Gaussian Filter
smoothedImg2 = imgaussfilt(img, 2);
%Apply Gaussian Filter smooting by 4
smoothedImg4 = imgaussfilt(img, 4);
%Apply Gaussian Filter smooting by 8
smoothedImg8 = imgaussfilt(img, 8);
%Apply Gaussian Filter smooting by 16
smoothedImg16 = imgaussfilt(img, 16);
%Display all images in single figure except original image
figure;
subplot(2,2,1), imshow(smoothedImg2), title('Smoothed Image 
(Sigma = 2)');
subplot(2,2,2), imshow(smoothedImg4), title('Smoothed Image 
(Sigma = 4)');
subplot(2,2,3), imshow(smoothedImg8), title('Smoothed Image 
(Sigma = 8)');
subplot(2,2,4), imshow(smoothedImg16), title('Smoothed Image 
(Sigma = 16)');
