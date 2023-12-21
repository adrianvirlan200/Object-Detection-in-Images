# Object Detection in Images

1. Image Generation using Stable Diffusion Model:
Generate a series of images based on a given prompt using the Stable Diffusion model in keras-cv.
Each student will have a specific object and color assigned (from the "ASIGNARE.pdf" resource).
Experiment with prompt formation to accurately represent the assigned object and color.

2.Image Saving with Specific Compression:
Save the generated images in a compression format assigned to each student (from the "ASIGNARE.pdf" resource).

3. Object Detection using YOLOv5:
Detect objects in the generated images using the YOLOv5 object detection network.
Run YOLOv5 using less complex models for faster detection and save the detection results in text files containing object positions in Darknet annotation format.

4. Cropping Detected Objects:
Crop the sections containing the assigned object from the generated images, using the text files created in the previous step.
Save the cropped images in the same format as in step 2.

5. Applying Color Masks and Converting Color Spaces:
Apply a mask to the cropped images to select only the assigned color.
Save the masked image in the same format as in step 2.
Convert the cropped image to a different color space (as assigned in the "ASIGNARE.pdf" resource) and save this image.

6. Transparency Conversion:
Convert the color mask to an image with transparency, making only the masked section of the object visible.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Color space represents a method of representing colors in a 3D system. The most well-known color space is RGB (Red, Green, Blue), an additive color space that represents the primary colors from which all other colors can be generated.

HSL (for Hue, Saturation, Lightness) is an alternative representation of the RGB color model. In this model, the colors of each hue are arranged in a radial slice around a central axis of neutral colors that varies from black at the bottom to white at the top.

In the program created, to convert the image from BGR space to HSL space, I used the cv2.cvtColor function, which takes as a parameter the initial image (RGB) and cv2.COLOR_BGR2HLS, and returns the image in the new color spectrum.

The color mask helped in extracting the pixels from the image that have a color within certain fixed values. To achieve this, the upper and lower limits were first defined. Then, a binary mask was created: if a pixel is between the previously defined limits, then the corresponding pixel in the mask becomes white, otherwise black. The final step involved applying the mask to the original image, using the bitwise ‘AND’ operation, leaving only those pixels visible whose corresponding pixels in the mask are white (white pixels in the mask are 255, which means 8 ones in binary, resulting in the bit from the image being preserved in the ‘AND’ operation; on the other hand, 0 AND x = 0 => the black pixels in the mask will cause the corresponding pixels in the image to become black).

To remove the black background from the image on which the mask was applied, I started by converting the image from BGR to grayscale. This way, an image with a single channel was obtained. The next step involved creating an alpha channel mask (transparency channel) -> all pixels of 0 take the maximum transparency value (255). The final stage corresponds to merging the alpha channel with the existing three channels (RGB), thus creating an image with 4 channels/transparency.
