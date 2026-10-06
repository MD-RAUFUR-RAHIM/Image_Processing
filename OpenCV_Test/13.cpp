#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main(void)
{
	IplImage *img = cvLoadImage("03.jpg");

	if (!img) {
		printf("Image can NOT Load!!!\n");
	}

	float filter[9] = {1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0};
	
	IplImage *grey_img = cvCreateImage(cvSize(img->width, img->height), IPL_DEPTH_8U, 1);
	
	for (int j = 0; j < img->height; j++) {
		for (int i = 0; i < img->width; i++) {
			unsigned char b = img->imageData[j * img->widthStep + i * 3 + 0];
			unsigned char g = img->imageData[j * img->widthStep + i * 3 + 1];
			unsigned char r = img->imageData[j * img->widthStep + i * 3 + 2];

			grey_img->imageData[j * grey_img->widthStep + i] = (unsigned char)((int(b) + int(g) + int(r)) / 3);
		}
	}

	IplImage* img_filtered = cvCreateImage(cvSize(grey_img->width-2, grey_img->height-2), IPL_DEPTH_8U, 1);
	

	cvNamedWindow("ImageWindow1");
	cvNamedWindow("ImageWindow2");

	while (true) {
		cvShowImage("ImageWindow1", grey_img);
		cvShowImage("ImageWindow2", img_filtered);

		int key = cvWaitKey(10);

		if (key == 27)
			break;
	}

	cvReleaseImage(&img);
	cvReleaseImage(&grey_img);
	cvReleaseImage(&img_filtered);

	return 0;
}
