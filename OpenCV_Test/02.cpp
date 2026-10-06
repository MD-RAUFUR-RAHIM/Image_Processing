#include<stdio.h>
#include<opencv/cv.h>
#include<opencv/highgui.h>

int main(void){
	IplImage* img = cvLoadImage("01.jpg");
	if(!img){
		printf("Image can not Load");
	}
	img->imageData[0] = 0;
	img->imageData[1] = 0;
	img->imageData[2] = 255;
	
	img->imageData[3] = 0;
	img->imageData[4] = 0;
	img->imageData[5] = 255;
	
	img->imageData[6] = 0;
	img->imageData[7] = 0;
	img->imageData[8] = 255;
	
	cvNamedWindow("ImageWindow1");
	while(true){
		cvShowImage("ImageWindow1", img);
		int key = cvWaitKey(10);
		
		if (key == 27)
			break;
	}
	cvReleaseImage(&img);
	return 0;
}