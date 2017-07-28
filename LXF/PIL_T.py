'''
    PIL只支持2.x, Pillow在PIL的基础上新添加了更多特性,支持3.x
'''

from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random


'''
=========图片压缩===========
'''
# 打开图片
img = Image.open('p1.jpg')
# 获取尺寸
w, h = img.size
print("Origin picture size:%s x %s"%(w,h))
# 缩放到50%
img.thumbnail((w // 2, h // 2))
print("Resize picture size:%s x %s"%(img.size))
# 保存新图片
img.save('p_thumb.jpg', 'jpeg')

'''
===========模糊图像===========
'''
img1 = Image.open('p2.jpg')
img1 = img1.filter(ImageFilter.BLUR)
img1.save('blur.jpg','jpeg')


'''
============绘图\字母验证码(ImageDraw\ImageFont)================
'''

# 随机字母
def randomChar():
    return  chr(random.randint(65,90))

#随机颜色1.
def randomColor1():

    rgb = random.randint(64, 255)
    return (rgb,rgb,rgb)

def randomColor2():
    rgb = random.randint(32, 127)
    return (rgb,rgb,rgb)

# 320 x 60
width = 80 * 4
height = 80
image = Image.new('RGB',(width, height),(255,255,255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for i in range(width):
    for j in range(height):
        draw.point((i,j), fill=randomColor1())

for temp in range(4):
    draw.text((80 * temp + 10, 10), randomChar(), font=font, fill=randomColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')










