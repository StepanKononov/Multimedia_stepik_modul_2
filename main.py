from skimage.io import imread, imshow, imsave
from skimage import img_as_float
from matplotlib import pyplot as plp
import numpy as np


def border_cut(img, cut_procent):
    cut_procent = cut_procent / 100

    border_y = int(img.shape[0] * cut_procent)
    border_x = int(img.shape[1] * cut_procent)

    img = img[border_y: img.shape[0] - border_y, border_x: img.shape[1] - border_x]

    return img


original_img = imread("00.png")

imshow(original_img)
plp.show()

original_img_f = img_as_float(original_img)

# Обрезаем белую рамку.
#cropped_im = border_cut(original_img_f, 3)
cropped_im = original_img_f.copy()

# Разделяем на 3 канала.
channel_row_cut = int(cropped_im.shape[0] // 3)
b = cropped_im[: channel_row_cut, :]
g = cropped_im[channel_row_cut: 2 * channel_row_cut, :]
r = cropped_im[2 * channel_row_cut: 3 * channel_row_cut, :]

original_size = b.shape
print(b.shape)
print(r.shape)
print(g.shape)


# Обрезаем рамки.
b = border_cut(b, 5)
r = border_cut(r, 5)
g = border_cut(g, 5)

# Сдвигаем изображение.
shift_b = [0, 0, float('-inf')]
shift_r = [0, 0, float('-inf')]
shift_count = 25


def image_shift(img, shift_data, shift):
    for x in range(-shift, shift + 1):
        for y in range(-shift, shift + 1):
            temp = np.roll(img, x, axis=0).copy()
            temp = np.roll(temp, y, axis=1).copy()
            correlation = (temp * g).sum()

            if correlation > shift_data[2]:
                shift_data = [x, y, correlation]
    return shift_data


shift_b = image_shift(b, shift_b, shift_count)
shift_r = image_shift(r, shift_r, shift_count)

b = np.roll(b, shift_b[0], axis=0)
b = np.roll(b, shift_b[1], axis=1)

r = np.roll(r, shift_r[0], axis=0)
r = np.roll(r, shift_r[1], axis=1)

print(b.shape)
print(r.shape)
print(g.shape)

ans = np.dstack((r, g, b))
print(shift_b, shift_r)

imshow(ans)
imsave("ans.png", ans)

row_g, col_g = 508, 237

row_b = row_g - original_size[0] - shift_b[0]
col_b = col_g - shift_b[1]

row_r = original_size[0] * 2 + (row_g - original_size[0]) - shift_r[0]
col_r = col_g - shift_r[1]

print(row_b, col_b, row_r, col_r)

plp.show()
