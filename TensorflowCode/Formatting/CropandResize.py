from os import listdir
from os.path import isfile, join
import os
from PIL import Image  # Python pillow image library

from Other.RESIZE import resize_contain

def resizeImage(img, dim=500):
    img = resize_contain(img, [dim,
                               dim])  # resizes images to a width of 500 pixels whilst keeping aspect ratio - eases computing power for crop analysis
    background = Image.new("RGB", img.size, (0, 0, 0))
    background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
    # img.show()
    return background

def cropImageByColorDetection(file):
    TOLERANCE = 20  # Tolerance for colour change detection

    if type(file) == str:
        image = Image.open(file)
    else:
        image = file
    # Print out some file information
    image_width = image.size[0]  # get width
    image_height = image.size[1]  # get height

    # Sample background color
    def rgb_tuple_to_str(tuple):
        return 'rgb(' + str(tuple[0]) + ', ' + str(tuple[1]) + ', ' + str(tuple[2]) + ')'

    def is_like_bg_color(color):
        # Setting base values
        color_r, color_g, color_b = color[0], color[1], color[2]  # grab rgb value
        bg_r, bg_g, bg_b = bg_color[0], bg_color[1], bg_color[2]  # Grab background rgb value
        r_similar, g_similar, b_similar = False, False, False  # tracking if the colour is simmilar

        # checking if the colours are simmilar to the background or different
        if color_r in range(bg_r - TOLERANCE, bg_r + TOLERANCE):
            r_similar = True

        if color_g in range(bg_g - TOLERANCE, bg_g + TOLERANCE):
            g_similar = True

        if color_b in range(bg_b - TOLERANCE, bg_b + TOLERANCE):
            b_similar = True

        return r_similar and g_similar and b_similar

    # Sampling the background colour
    pixel_map = image.load()  # load in the image

    x_offset = image_width * 0.05
    y_offset = image_height * 0.05

    # sampling the corners of the image for the background colour
    ul_color = pixel_map[x_offset, y_offset]
    ur_color = pixel_map[image_width - x_offset, y_offset]
    ll_color = pixel_map[x_offset, image_height - y_offset]
    lr_color = pixel_map[image_width - x_offset, image_height - y_offset]
    bg_color = ()

    # checking if we have the background colour or not
    # if ul_color == ur_color or ur_color == ll_color or ll_color == lr_color:
    bg_color = ul_color
    # print("Sampled background color: " + rgb_tuple_to_str(ul_color))

    ##Searching for the crop coordinates

    # Search for top edge
    top_edge_coords = []

    for i in range(0, image_width, int(image_width / 10)):  # cycle through the cols
        for y in range(0, image_height - 1):  # cycle through the rows
            if not is_like_bg_color(pixel_map[i, y]):  # check if bg colour is not simmilar
                top_edge_coords.append(y)  # add it to the list of top level crop coords
                break

    top_edge_coord = top_edge_coords[0]
    for c in top_edge_coords:
        if c < top_edge_coord:
            top_edge_coord = c

    # Search for bottom edge

    bottom_edge_coords = []

    for i in range(0, image_width, int(image_width / 10)):
        for y in range(image_height - 1, 0, -1):
            if not is_like_bg_color(pixel_map[i, y]):
                bottom_edge_coords.append(y)
                break

    bottom_edge_coord = bottom_edge_coords[0]
    for c in bottom_edge_coords:
        if c > bottom_edge_coord:
            bottom_edge_coord = c

    # Search for left edge

    left_edge_coords = []

    for i in range(0, image_height, int(image_height / 10)):
        for x in range(0, image_width - 1):
            if not is_like_bg_color(pixel_map[x, i]):
                left_edge_coords.append(x)
                break

    left_edge_coord = left_edge_coords[0]
    for c in left_edge_coords:
        if c < left_edge_coord:
            left_edge_coord = c

    # Search for right edge

    right_edge_coords = []

    for i in range(0, image_height, int(image_height / 10)):
        for x in range(image_width - 1, 0, -1):
            try:
                if not is_like_bg_color(pixel_map[x, i]):
                    right_edge_coords.append(x)
                    break
            except IndexError:
                pass

    right_edge_coord = right_edge_coords[0]
    for c in right_edge_coords:
        if c > right_edge_coord:
            right_edge_coord = c

    # Crop the image

    cropped_image = image.crop((left_edge_coord, top_edge_coord, right_edge_coord, bottom_edge_coord))
    # image.show()
    # cropped_image.show()
    return cropped_image


def formatFilesInFolder(path):
    mypath = path

    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(files)

    for i in files:
        try:
            x = resizeImage(cropImageByColorDetection(fr"{mypath}\{i}"),dim = 512).save(fr"{mypath}\{i}")
            print(f"Done with {i}")
        except Exception as e:
            os.remove(fr"{mypath}\{i}")
            print(f"Deleted a file")


if __name__ == "__main__":
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\1")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\2")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\3")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\4")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\5")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\6")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\7")
    formatFilesInFolder(r"C:\Users\rajib\Documents\OBNewDataset\SORTED\8")