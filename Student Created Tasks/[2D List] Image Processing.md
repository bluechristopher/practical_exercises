# Task 1: Image Processing

You are provided with a text file `image.txt` containing the RGB values of a coloured image. The pixel data is stored in a 2D array format where each element represents a pixel's colour using a tuple of three integers (R, G, B). Your task is to read the pixel data, store it in a 2D list, and then perform image processing operations such as changing it to monochrome and applying Gaussian blur.

---

## Task 1.1

Write a Python function `read_pixels(filename)` to read the pixel data from the file `image.txt`. Each pixel's data is stored as an `(R, G, B)` tuple, and the pixels are arranged in rows.

Your function should:
- read the file `image.txt` containing the pixel data
- store the pixel data in a 2-dimensional list, where each element in a row is a tuple with integer RGB values.

Test your program by reading the pixel data and outputting the first 5 rows of the 2D list.

---

## Task 1.2

Write a Python function `monochrome(pixel_data)` that takes the 2-dimensional list of RGB pixel data as input and converts the image to monochrome. 



To convert to monochrome:
- for each pixel, calculate the average of the R, G, and B values
- replace the RGB tuple of each pixel with a single integer representing the grayscale value (the average).

Test your program by outputting the first 5 rows of the monochrome image.

For example, the **first** row should be:

`[85, 170, 140, 85, 85, 85, 216, 216, 170, 85, 85, 170, 85, 85, 85, 85, 85, 140, 170, 170]`

---

## Task 1.3

Write a Python function `blur(data)` to apply a simple Gaussian blur to the monochrome image. 

The function should:
- for each pixel in the image (except border pixels), calculate the average grayscale value of the pixel and its 8 immediate neighbors (surrounding pixels in a 3x3 grid)
- replace the pixel’s grayscale value with this average to achieve a blurring effect
- ensure that the border pixels remain unchanged.

Test your program by outputting the first 5 rows of the blurred image.

For example, the **first two rows** should be:

```
[85, 170, 140, 85, 85, 85, 216, 216, 170, 85, 85, 170, 85, 85, 85, 85, 85, 140, 170, 170]
[170, 147, 147, 119, 94, 123, 157, 182, 143, 125, 116, 128, 131, 116, 103, 100, 106, 130, 134, 170]
```
---

## Task 1.4

Write a procedure `write_monochrome(filename, data)` to save the processed 2D list of monochrome pixel values to a text file.
---

The monochrome pixel values should be separated by a single space.

Test your procedure by saving both the monochrome and blurred image data into `monochrome.txt` and `blurred.txt` respectively.

---
