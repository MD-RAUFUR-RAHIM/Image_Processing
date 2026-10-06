#include <stdio.h>
#include <opencv/cv.h> 
#include <opencv/highgui.h>
int main(void)
{
	IplImage *img = cvCreateImage(cvSize(640,480), IPL_DEPTH_8U, 1);
	for(int j = 0; j < img->height / 4; j++){
		for (int i = 0; i < img->width / 4; i++) {
			img->imageData[j * img->widthStep + i] = 100;
		
		}
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