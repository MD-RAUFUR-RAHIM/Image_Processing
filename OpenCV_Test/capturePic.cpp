#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

int main()
{
    CvCapture* cap = cvCaptureFromCAM(0);

    if (!cap) {
        printf("Can NOT Find Camera!!!\n");
        return -1; // exit if no camera
    }

    cvNamedWindow("ImageWindow1");

    while (true) {
        IplImage* img = cvQueryFrame(cap);

        cvShowImage("ImageWindow1", img);

        int key = cvWaitKey(10);

        if (key == 27)  // ESC to quit
            break;

        if (key == 's') {  // 's' key to save
            cvSaveImage("captured_photo.jpg", img, 0);
            printf("Photo saved!\n");
        }
    }

    cvReleaseCapture(&cap);
    cvDestroyWindow("ImageWindow1");

    return 0;
}
