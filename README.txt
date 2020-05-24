Author:     Lynne Raynor
-----------

Process - WIP:
*** = TODO 

    Locating: 
        Convert image to grayscale
        Use Harris Corner detection, which is strongly clustered around code
        Crop near median corner, roughly isolating QR Code
        
    Extracting: 
        Use Canny Edge detection to find 4 corner points 
        Perform perspective transform to get flat, isolated image 
        Thresh to binary image
        Find contours
        Use contours to rotate image to correct orientation ***
        
    Reading: 
        Stitch 4 images together ***
        Read QR code image
    


To use the code: 
    
    Run interpret.py. There are several example images provided. The
    output will write intermediate images so that you can see the steps 
    being used. interpret.py writes the following images to the output folder:
    
        Location/Extraction: 
        Input: 1.jpg, 2.jpg, 3.jpg, 4.jpg: 4 sample photos provided of 
           quartered QR code
        Output: Canny Edge and Extracted images
            Canny Edge photos have circled points indicating which 4 corners
            were used for the perspective transform
            
        
        Stitching images (incomplete): 
        Input: complete.png: the whole QR image created from the 4 pieces
        Output: threshold.png: the whole QR code as a binary image
                contour.png: contours are outlined in gray
        
        ~TODO steps here will rotate the 4 pieces to create a valid QR code~
           
        Reading: 
        Input: frame.png: a generic sample QR code with data = 1234    
        Output: data is read and printed to the console
    