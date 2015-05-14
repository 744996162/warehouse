from PIL import Image
import pytesseract
import PIL.Image

# print pytesseract.image_to_string(Image.open('test.png'))
# im=Image.open('1.jpg')
im_sh=Image.open('sh.jpg')
# new_image_L=im.convert('L')
# new_image_L.save('output_L.jpg')
# new_image_1=im.convert('1')
# new_image_1.save('output_1.jpg')

new_image_sh=im_sh.convert('L')
new_image_sh.save('output_sh.jpg')

# print pytesseract.image_to_string(Image.open('output_L.jpg'))
print pytesseract.image_to_string(Image.open('output_sh.jpg'))