
#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main(void)
{
	IplImage* img = cvLoadImage("01.jpg");

	if (!img) {
		printf("Image can NOT Load!!!\n");
	}
		
	for (int j = 0; j < img->height / 2; j++) {
		for (int i = 0; i < img->width / 2; i++) {
			img->imageData[j*img->widthStep + i * 3 + 0] = 0;	// B
			img->imageData[j*img->widthStep + i * 3 + 1] = 0;	// G
			img->imageData[j*img->widthStep + i * 3 + 2] = 0;	// R
		}
	}

	cvNamedWindow("ImageWindow1");

	while (true) {
		cvShowImage("ImageWindow1", img);

		int key = cvWaitKey(10);

		if (key == 27)
			break;
	}

	cvReleaseImage(&img);
	
	return 0;
}


