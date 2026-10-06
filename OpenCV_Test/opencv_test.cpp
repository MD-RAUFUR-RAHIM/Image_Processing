
#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main(void) 
{
	IplImage* img = cvLoadImage("01.jpg");

	if (!img) {
		printf("Image can NOT Load!!!\n");
	}

	cvNamedWindow("ImageWindow1");

	while(1) {
		cvShowImage("ImageWindow1", img);
	
		int key = cvWaitKey(10);

		if(key == 27)
			break;
	}

	cvReleaseImage(&img);
	
	return 0;
}

