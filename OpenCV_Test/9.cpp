#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main()
{
	CvCapture* cap = cvCaptureFromCAM(0);

	if (!cap) {
		printf("Can NOT Find Camera!!!\n");
	}

	cvNamedWindow("ImageWindow1");
	cvNamedWindow("ImageWindow2");

	while (true) {
		IplImage* img = cvQueryFrame(cap);

		IplImage* grey_img = cvCreateImage(cvSize(img->width, img->height),
			                               IPL_DEPTH_8U, 1);

		for (int j = 0; j < img->height; j++) {
			for (int i = 0; i < img->width; i++) {
				unsigned char b = img->imageData[j * img->widthStep + i * 3 + 0];
				unsigned char g = img->imageData[j * img->widthStep + i * 3 + 1];
				unsigned char r = img->imageData[j * img->widthStep + i * 3 + 2];

				grey_img->imageData[j * grey_img->widthStep + i]
					= (unsigned char)((int(b) + int(g) + int(r)) / 3);
			}
		}

		cvShowImage("ImageWindow1", img);
		cvShowImage("ImageWindow2", grey_img);

		cvReleaseImage(&grey_img);

		int key = cvWaitKey(10);

		if (key == 27)
			break;
	}

	cvReleaseCapture(&cap);
	
	return 0;
}


