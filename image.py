import random

import numpy as np
from PIL import Image


def make():
    rand = random.randint(0, 255)
    line_data = np.full(256, rand)

    hue = np.tile(
        line_data, (256, 1)
    )  # 255x255の2次元配列を生成 [0,1..,254,255],[0,1..,254,255]
    sat = np.transpose(hue)  # hueの配列の行と列を入れ替え [0 0],[1,1],[254,254],[255,255]

    sa = np.transpose(hue)  # hueの配列の行と列を入れ替え [0 0],[1,1],[254,254],[255,255]

    mat = np.stack([hue, sat, sa], 2)  # 3つの2次元配列を結合して3次元配列にする axisで結合の階層を指定
    im = Image.fromarray(np.uint8(mat), "HSV")

    im_rgb = im.convert("RGB")  # HSVからRGBに変換

    return im_rgb.save("static/images/out_color.png")
