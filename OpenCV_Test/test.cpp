#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

// Function that waits specifically for the ESC key using recursion
void wait_for_esc(IplImage* img) {
    cvShowImage("EPCL_Window", img);
    
    int key = cvWaitKey(0); // Pauses and waits for ANY key press

    // If the key is NOT Esc (27), call this function again
    if (key != 27) {
        wait_for_esc(img);
    }
    // If key == 27, the function simply ends and returns
}

int main(void) 
{
    IplImage* img = cvLoadImage("01.jpg");

    if (!img) {
        printf("Image can NOT Load!!!\n");
        return -1; // Prevents crashing if image fails to load
    }

    cvNamedWindow("EPCL_Window");

    // Call our recursive function instead of a while loop
    wait_for_esc(img);

    cvReleaseImage(&img);
    
    return 0;
}