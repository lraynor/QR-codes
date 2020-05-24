Author:     Lynne Raynor
-----------

1. How far did you get with the challenge? How much time did it take?
    I was able to get parts 1 and 2 working on 3/4 of the images 
    provided, but some debugging is needed. For part 3, I wasn't able to 
    look into how to rotate the QR codes, but after that I would have been
    able to read a standard, whole QR code pretty easily. I spent about 8 hours
    between research and working on the challenge.

2. Please provide a brief description of the way that you have organized your code.

I worked on this problem non-sequentially as I learned which tools were useful
for which steps. I believe that this solution would work, if fully implemented.

Planned Process: 

    Locating: 
        Convert image to grayscale
        Use Harris Corner detection, which is strongly clustered around code
        Crop near median corner, roughly isolating QR Code
        
    Extracting: 
        Use Canny Edge detection to find 4 corner points **
        Perform perspective transform to get flat, isolated image **
        Thresh to binary image
        Find contours
        Use contours to rotate image to correct orientation ***
        
    Reading: 
        Stitch 4 images together ***
        Read QR code image
    
** = works in some cases
*** = TODO

3. Please provide instructions on how to run your code.
    
    Run interpret.py. I used several images to demostrate my progress. The
    output will write intermediate images so that you can see the steps 
    being used. interpret.py writes the following images to the output folder:
    
        Parts 1 & 2
        Input: 1.jpg, 2.jpg, 3.jpg, 4.jpg: 4 sample photos provided
        Output: Canny Edge and Extracted images
            Canny Edge photos have circled points indicating which 4 corners
            were used for the perspective transform
            
        
        Part 3
        Input: complete.png: the whole QR image provided in the challenge write-up
        Output: threshold.png: the whole QR code as a binary image
                contour.png: contours are outlined in gray
            
           
        Input: frame.png: a generic sample QR code with data = 1234    
        Output: data is read and printed to the console
    