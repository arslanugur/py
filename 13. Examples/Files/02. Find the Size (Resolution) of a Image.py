# Files Examples
# Example: to Find the Size (Resolution) of a Image
#          to find resolution of a jpeg image in this example without using external libraries


# the knowledge of the following Python programming topics:
#    Python Functions
#    Python User-defined Functions
#    Python File I/O

# JPEG (pronounced "jay-peg") stands for Joint Photographic Experts Group. 
# It is one of the most widely used compression techniques for image compression.

# Most of the file formats have headers (initial few bytes) which contain useful information about the file.

# For example, jpeg headers contain information like height, width, number of color (grayscale or RGB) etc. 
# In this program, we find the resolution of a jpeg image reading these headers, without using any external library.
# Source Code of Find Resolution of JPEG Image

def jpeg_res(filename):
   """"This function prints the resolution of the jpeg image file passed into it"""

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

       # height of image (in 2 bytes) is at 164th position
       img_file.seek(163)

       # read the 2 bytes
       a = img_file.read(2)

       # calculate height
       height = (a[0] << 8) + a[1]

       # next 2 bytes is width
       a = img_file.read(2)

       # calculate width
       width = (a[0] << 8) + a[1]

   print("The resolution of the image is",width,"x",height)

jpeg_res("img1.jpg")

# Output: The resolution of the image is 280 x 280

# In this program, we opened the image in binary mode. Non-text files must be open in this mode. 
# The height of the image is at 164th position followed by width of the image. Both are 2 bytes long.

# Note that this is true only for JPEG File Interchange Format (JFIF) standard. 
# If your image is encode using other standard (like EXIF), the code will not work.

# We convert the 2 bytes into a number using bitwise shifting operator <<. 
# Finally, the resolution is displayed.


