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

	while (true) {
		IplImage* img = cvQueryFrame(cap);

		cvShowImage("ImageWindow1", img);

		int key = cvWaitKey(10);

		if (key == 27)
			break;
	}

	cvReleaseCapture(&cap);
	
	return 0;
}


