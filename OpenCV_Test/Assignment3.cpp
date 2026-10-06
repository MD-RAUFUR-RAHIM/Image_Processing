#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main(void)
{
	IplImage *img = cvLoadImage("wolf2.png");

	if (!img) {
		printf("Image can NOT Load!!!\n");
	}

	IplImage* img_large_1 = cvCreateImage(cvSize(img->width*2, img->height*2), img->depth, img->nChannels);
	IplImage* img_large_2 = cvCreateImage(cvSize(img->width*2, img->height*2), img->depth, img->nChannels);
	IplImage* img_large_3 = cvCreateImage(cvSize(img->width*2, img->height*2), img->depth, img->nChannels);
	IplImage* img_large_4 = cvCreateImage(cvSize(img->width*2, img->height*2), img->depth, img->nChannels);
	
	cvResize(img, img_large_1, CV_INTER_NN);
	cvResize(img, img_large_2, CV_INTER_LINEAR);
	cvResize(img, img_large_3, CV_INTER_CUBIC);
	cvResize(img, img_large_4, CV_INTER_AREA);
	    
	cvNamedWindow("ImageWindow1");
	cvNamedWindow("ImageWindow2");
	cvNamedWindow("ImageWindow3");
	cvNamedWindow("ImageWindow4");
	cvNamedWindow("ImageWindow5");

	while (true) {
		cvShowImage("ImageWindow1", img);
		cvShowImage("ImageWindow2", img_large_1);
		cvShowImage("ImageWindow3", img_large_2);
		cvShowImage("ImageWindow4", img_large_3);
		cvShowImage("ImageWindow5", img_large_4);

		int key = cvWaitKey(10);

		if (key == 27)
			break;
	}

	cvReleaseImage(&img);
	cvReleaseImage(&img_large_1);
	cvReleaseImage(&img_large_2);
	cvReleaseImage(&img_large_3);
	cvReleaseImage(&img_large_4);

	return 0;
}
