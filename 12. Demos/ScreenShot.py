# pip install pyscreenshot
import pyscreenshot
image = pyscreenshot.grab()
# to display the captured screenshot
image.show()
# to save the screenshot
image.save("code.png")



# program for partial screenshot
import pyscreenshot
# im = pyscreenshot.grab(bbox=(x1, x2, y1, y2))
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))
# to view the screenshot
image.show()
# to save the screenshot
image.save("code.png")



