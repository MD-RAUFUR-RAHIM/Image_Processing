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
    cvNamedWindow("ImageWindow2");

    int brightness = 0;  

    while (true) {
        IplImage* img = cvQueryFrame(cap);

        if (!img) {
            printf("Failed to capture frame!\n");
            break;
        }

        IplImage* grey_img = cvCreateImage(cvSize(img->width, img->height),
                                           IPL_DEPTH_8U, 1);

        for (int j = 0; j < img->height; j++) {
            for (int i = 0; i < img->width; i++) {
                unsigned char b = img->imageData[j * img->widthStep + i * 3 + 0];
                unsigned char g = img->imageData[j * img->widthStep + i * 3 + 1];
                unsigned char r = img->imageData[j * img->widthStep + i * 3 + 2];

                int value = (int(b) + int(g) + int(r)) / 3 + brightness;

                // clamp to [0,255]
                if (value > 255) value = 255;
                if (value < 0) value = 0;

                grey_img->imageData[j * grey_img->widthStep + i] = (unsigned char)value;
            }
        }

        cvShowImage("ImageWindow1", img);
        cvShowImage("ImageWindow2", grey_img);

        cvReleaseImage(&grey_img);

        int key = cvWaitKey(10);

        if (key == 27)  
            break;

        if (key == '1') {  
            brightness += 10;
            printf("Brightness increased: %d\n", brightness);
        }

        if (key == '2') {  
            brightness -= 10;
            printf("Brightness decreased: %d\n", brightness);
        }
    }

    cvReleaseCapture(&cap);
    cvDestroyWindow("ImageWindow1");
    cvDestroyWindow("ImageWindow2");

    return 0;
}
