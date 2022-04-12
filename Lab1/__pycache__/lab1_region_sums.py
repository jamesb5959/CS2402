#CS 2302
#Bradley Beltran
#Lab 1
#Instructor: Olac Fuentes
#Teaching Assistant: Jose Perez
#Instructional Assistant: David Dominguez
#Find the brightest pixel and region
import numpy as np
from timeit import default_timer as timer
from utils import read_image_from_file, plot_image_grid, plot_image, plot_image_with_rectangle


# The image file to use when running this lab
IMAGE_FILENAME = 'sun1.jpg'

# The region sizes the naive algorithm will use. The sizes are stored as "[rows, columns]"
# Be careful when changing these, if the number is too big it will take a long time to run your program
NAIVE_REGION_SIZES = [
    [20, 20], 
    [30, 30], 
    [30, 60], 
]

# The region sizes the integral image algorithm will use. The sizes are stored as "[rows, columns]"
# Note that the NAIVE_REGION_SIZES are also included in this list
INTEGRAL_REGION_SIZES = \
    NAIVE_REGION_SIZES + [
    [60, 60],
    [60, 100],
    [160, 160],
]

# Whether to run the naive algorithm for evaluation or not
# Set this to False when you want to skip it to test your integral image algorithm
RUN_NAIVE = True

# ******************** LAB PROBLEMS (WRITE YOUR CODE HERE) ********************


def brightest_pixel(im):
    # Find the single brightest pixel of an image and return the coordinates of it
    brightest_pixel_row = 0
    brightest_pixel_col = 0
    brightest = im[0,0]
    for i in range(len(im)):
        for j in range(len(im[i])):
            if im[i,j] > brightest:
                brightest = im[i,j]
                brightest_pixel_row = i
                brightest_pixel_col = j
    return brightest_pixel_row, brightest_pixel_col


def brightest_region_naive(im, rw, rh):
    # Find the brightest region of size "rw" by "rh" in an image using a naive approach
    # rw = region width, rh = region height
    # You should return the top-left coordinate of the brightest region found
    result_row = 0
    result_col = 0
    sum = 0
    brightest = 0
    for row in range(len(im)-rh):
        for col in range(len(im[row])-rw):
            for h in range(rh):
                for w in range(rw):
                    sum+=im[row+h,col+w]
                    if brightest<sum:
                        brightest = sum
                        result_row = row
                        result_col = col
    print(result_row, result_col)
    return result_row, result_col


def brightest_region_integral_image(im, rw, rh):
    # Find the brightest region of size "rw" by "rh" in an image using the Integral Image algorithm
    # You should return the top-left coordinate of the brightest region found
    result_row = 0
    result_col = 0
    brightest = 0
    sum = np.zeros((im.shape, im[0].shape))
    for i in range(1, len(im)):
        for j in range(1, len(im[i])):
            sum[i,j]=im[i,j]+ sum[i-1,j]+sum[i,j-1]-sum[i-1,j-1]
            if sum[i,j]>brightest:
                brightest = sum[i,j]
                result_row = i
                result_col = j
    print(result_row, result_col)
    return result_row, result_col


# ******************** LAB RESULTS DISPLAY (DON'T CHANGE THIS!) ************************
if __name__ == '__main__':
    im1 = read_image_from_file(IMAGE_FILENAME)
    if len(im1.shape) == 3:
        im1 = im1.mean(axis=2)

    # Brightest Pixel
    bpr, bpc = brightest_pixel(im1)
    plot_image_with_rectangle(im1, bpr, bpc, 1, 1, 'Brightest Pixel', 'fig_brightest_pixel.png')

    # Naive
    if RUN_NAIVE:
        for nrows, ncols in NAIVE_REGION_SIZES:
            start_time = timer()
            brow, bcol = brightest_region_naive(im1, nrows, ncols)
            end_time = timer()

            print(f'Brightest region for size {nrows}x{ncols} using naive algorithm took {end_time-start_time:.3f} seconds to compute')
            plot_image_with_rectangle(im1, brow, bcol, nrows, ncols, f'Brightest {nrows}x{ncols} Region (Naive)', f'fig_brightest_naive_{nrows}_{ncols}.png')
        
    # Integral Image
    for nrows, ncols in INTEGRAL_REGION_SIZES:
        start_time = timer()
        brow, bcol = brightest_region_integral_image(im1, nrows, ncols)
        end_time = timer()

        print(f'Brightest region for size {nrows}x{ncols} using integral image algorithm took {end_time-start_time:.3f} seconds to compute')
        plot_image_with_rectangle(im1, brow, bcol, nrows, ncols, f'Brightest {nrows}x{ncols} Region (Integral Image)', f'fig_brightest_integral_{nrows}_{ncols}.png')