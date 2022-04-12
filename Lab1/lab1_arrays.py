#CS 2302
#Bradley Beltran
#Lab 1
#Instructor: Olac Fuentes
#Teaching Assistant: Jose Perez
#Instructional Assistant: David Dominguez
#Edit pictures in diffrent ways using for loops or slicing.
import numpy as np
from utils import read_image_from_file, plot_image_grid, plot_image


# The image file to use when running this lab
IMAGE_FILENAME = 'coke.png'

# Set this to True to display every single problem in the homework as its own separate figure
# This is great when you have completed the lab but you might want to set it to False
# When debugging so you don't have 15 figures open at the same time
DISPLAY_INDIVIDUAL_PLOTS = True


# ******************** LAB PROBLEMS (WRITE YOUR CODE HERE) ********************


def get_color_channels(im):
    # Extract the red, green, and blue channels of the color image separately
    im_red = im[:,:,0]
    im_green = im[:,:,1]
    im_blue = im[:,:,2]
    return im_red, im_green, im_blue


def subsampled(im):
    # Compute a subsampled version of the image that only includes the even rows and odd columns
    return im[1::2, ::2]


def grayscale(im):
    # Convert a color image to grayscale by taking its red, green, and blue channels and combining them with the formula
    return 0.299*im_red+0.587*im_green+0.114*im_blue


def negative_grayscale(im):
    # Compute the negative of the grayscale version of the color image
    im_gray = -grayscale(im)
    return im_gray


def upside_down(im):
    # Flip the colored image upside down
    return im[::-1]


def mirrored(im):
    # Mirror the colored image
    return im[::1,::-1]


def crop(im, top_left_row, top_left_col, crop_w, crop_h):
    # Crop a part of the image given the top-left coordinates of the crop (top_left_row, top_left_col) as well as the width and height of the crop (crop_w, crop_h)
    return im[top_left_row:crop_h, top_left_col:crop_w]


def horizontal_edges(im):
    # EXTRA CREDIT: Horizontal Edges
    im_gray = grayscale(im)
    return im_gray


def vertical_edges(im):
    # EXTRA CREDIT: Vertical Edges
    im_gray = grayscale(im)
    return im_gray


# ******************** LAB RESULTS DISPLAY (DON'T CHANGE THIS!) ************************
if __name__ == '__main__':
    # Compute the image arrays for the first part based on this image
    im1 = read_image_from_file(IMAGE_FILENAME)

    im_red, im_green, im_blue = get_color_channels(im1)
    im_subsampled = subsampled(im1)
    im_gray = grayscale(im1)
    im_ngray = negative_grayscale(im1)
    im_upside_down = upside_down(im1)
    im_mirrored = mirrored(im1)
    im_crop = crop(im1, 25, 40, 175, 100)
    im_horizontal = horizontal_edges(im1)
    im_vertical = vertical_edges(im1)

    # Plot the images to the screen
    images = [im_red, im_green, im_blue, im_subsampled,
              im_gray, im_ngray, im_upside_down, im_mirrored, im_crop, im_horizontal, im_vertical]

    titles = ['Red Channel', 'Green Channel', 'Blue Channel', 'Subsampled Image', 'Grayscale Image',
              'Negative Grayscale Image', 'Upside Down Image', 'Mirrored Image', 'Cropped Image', 'Horizontal Edges', 'Vertical Edges']

    filenames = ['fig_red', 'fig_green', 'fig_blue', 'fig_subsample', 'fig_grayscale',
                 'fig_negative_grayscale', 'fig_upside_down', 'fig_mirrored', 'fig_crop', 'fig_horizontal', 'fig_vertical']

    if DISPLAY_INDIVIDUAL_PLOTS:
        for image, title, filename in zip(images, titles, filenames):
            plot_image(image, title, filename + '.png')

    # Plot all the arrays in one figure for easier visualization
    plot_image_grid([im1] + images,
                    nrows=4,
                    ncols=3,
                    figure_title='Summary of all image array problems',
                    titles=['Original'] + titles,
                    filename='fig_part1_summary.png')
