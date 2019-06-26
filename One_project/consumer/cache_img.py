"""
随机小数:

1.random.random() #0-1之内的随机小数

2.random.unifom(1,5) #范围之内的随机小数

随机整数

random.randint(1,2) #[1,2] 包括2在内的范围内随机取整数

random.randrange(1,2) #[1,2) 不包括2在内的范围内随机取整数

random.randrange(1,10,2) [1,10) 不包含10在内的范围内随机取奇数

 随机抽取

random.choice(lis) #随机抽取一个值

random.choice(lis,2) #随机抽取多个值 可以数量

打乱顺序(在原列表上打断)

random.shuffle(list)

"""
import os
import random
from io import BytesIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from One_project.settings import BASE_DIR


def get_cache_code_info():
    resule = ''
    list_info='qwertyupasdfghjkzxcvbnmQWERTYUPKMJNHBGVFCDXSZA123456789'
    for i in range(1 , 5):
        resule += random.choice(list_info)
    # 获取一个Image对象，参数分别是RGB模式。宽160，高30，随机颜色
    image = Image.new('RGB', (160, 30), (255 , 255 , 255))
    # 获取一个画笔对象，将图片对象传过去
    draw = ImageDraw.Draw(image)

    # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
    font = ImageFont.truetype(os.path.join(os.path.join(BASE_DIR, 'consumer'),'cerepf.ttf'),size=30)

    # 在图片上写东西,参数是：定位，字符串，颜色，字体
    draw.text((20, 0), resule, (0,0,0),font=font)

    # 保存到硬盘，名为test.png格式为png的图片
    image_io=BytesIO()
    image.save(image_io,'png')
    return image_io,resule

if __name__ == '__main__':
    print(get_cache_code_info())
