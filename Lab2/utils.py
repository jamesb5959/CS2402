# Author: Jose G. Perez (jperez50@miners.utep.du)
# Last Date Modified: 09/22/2021 (v2)
# Lab utilities and functions for students to use in their labs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pt
from PIL import Image
from pathlib import Path

# ******************** PROVIDED FUNCTIONS (DON'T CHANGE THIS!) ********************
def draw_list_bst(T, title='', filename=None):
    # Draws a list-based BST from Lab 2 using matplotlib figures
    if T == None:
        print('Empty tree, nothing to draw')
    else:
        dx ={}
        set_xy(T, dx)
        fig, ax = plt.subplots()
        draw_(T, ax, dx)
        ax.axis('off')
        fig.suptitle(title, fontsize=14)
        plt.show()

        if filename is not None:
            output_dir = Path('./figures')
            if not output_dir.exists():
                output_dir.mkdir()
            plt.savefig(output_dir / filename)

def draw_(T, ax, dx):
    # Auxiliary function used by the drawing function
    if T != None:
        # T is not empty, so let's use 3 different variables to make our lives easier
        # Remember, you can't do this unless you check that T is not None
        left_subtree = T[0]
        key = T[1]
        right_subtree = T[2]

        px, py = dx[key]
        for child in [left_subtree, right_subtree]:
            if child != None:
                cx,cy = dx[child[1]]
                ax.plot([px,cx],[py,cy],linewidth=1,color='k')
                draw_(child, ax,dx)
        ax.text(px,py, str(key), size=12,ha="center", va="center",bbox=dict(facecolor='w',boxstyle="circle"))

def set_xy(T,dx,x=0,y=0):
    # Auxiliary function used by the drawing function
    # Finds the image coordinates to draw the tree's nodes
    if T != None:
        # T is not empty, so let's use 3 different variables to make our lives easier
        # Remember, you can't do this unless you check that T is not None
        left_subtree = T[0]
        key = T[1]
        right_subtree = T[2]

        next_x = set_xy(left_subtree, dx,x,y-1)
        dx[key] = (next_x, y)
        x = set_xy(right_subtree, dx,next_x+1,y-1)
    return x

def read_image_from_file(filename):
    # Read an image from a given filename
    # Check that the file actually exists
    assert Path(filename).exists(), f'{filename} does not exist'

    # Read the raw image using the imaging library
    raw_image = Image.open(filename)

    # Convert that image into an array with values from 0 to 255
    im_array = np.asarray(raw_image, dtype=np.uint8)
    return im_array


def plot_image(im, title='', filename=None):
    # Plot a single image to the screen
    return plot_image_grid([im], 1, 1, title, titles=[''], filename=filename)


def plot_image_with_rectangle(im, rect_row, rect_col, rw, rh, title='', filename=None):
    # Plots a single image to the screen with a rectangle embedded in it
    fig, ax = plot_image(im, title, filename)
    ax.add_patch(pt.Rectangle((rect_row, rect_col), rh, rw, fill=False, edgecolor='red', lw=1))
    plt.tight_layout()

    if filename is not None:
        output_dir = Path('./figures')
        if not output_dir.exists():
            output_dir.mkdir()
        plt.savefig(output_dir / filename)

def plot_image_grid(images, nrows, ncols, figure_title, titles=[], filename=None):
    # Plot multiple images in a grid
    fig, ax = plt.subplots(nrows, ncols)
    fig.suptitle(f'{figure_title}', fontsize='medium', weight='bold')
    for axi in fig.get_axes():
        # Remove plot ticks
        axi.set_yticks([])
        axi.set_xticks([])
        # Remove outline around plot
        axi.spines['top'].set_visible(False)
        axi.spines['right'].set_visible(False)
        axi.spines['left'].set_visible(False)
        axi.spines['bottom'].set_visible(False)

    for idx, im in enumerate(images):
        r = idx % nrows
        c = idx // nrows

        if len(images) == 1:
            axi = ax
        elif nrows == 1 or ncols == 1:
            axi = ax[idx]
        else:
            axi = ax[r, c]

        axi.set_title(titles[idx])

        # Check if the image is grayscale to display the colors correctly
        if len(im.shape) == 2:
            axi.imshow(im, cmap='gray')
        else:
            axi.imshow(im)

    plt.tight_layout()
    plt.show()

    if filename is not None:
        output_dir = Path('./figures')
        if not output_dir.exists():
            output_dir.mkdir()
        plt.savefig(output_dir / filename)

    return fig, ax