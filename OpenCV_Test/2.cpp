#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main(void)
{
	IplImage* img = cvLoadImage("Anup.png");

	if (!img) {
		printf("Image can NOT Load!!!\n");
		return 0;
	}

	printf("width: %d\n", img->width);
	printf("Origin: %d\n", img->origin);
	printf("widthStep: %d\n", img->widthStep);
	printf("height: %d\n", img->height);

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