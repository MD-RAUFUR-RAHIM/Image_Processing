#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main(void) 
{
	IplImage* img = cvLoadImage("01.jpg");

	if (!img) {
		printf("Image can NOT Load!!!\n");
	}

	cvNamedWindow("EPCL_Window");

	while(1) {
		cvShowImage("EPCL_Window", img);
	
		int key = cvWaitKey(10);

		if(key == 27)
			break;
	}

	cvReleaseImage(&img);
	
	return 0;
}