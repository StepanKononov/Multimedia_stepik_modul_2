from skimage.io import imread, imshow, imsave
from skimage import img_as_float
from matplotlib import pyplot as plp
import numpy as np

original_img = imread("00.png")

imshow(original_img)
plp.show()

row_g, col_g = 508, 237

print(original_img[row_g,col_g])
original_img_f = img_as_float(original_img)

border_y = int(original_img_f.shape[0] * 0.03)
border_x = int(original_img_f.shape[1] * 0.03)

cropped_im = original_img_f[border_y:original_img_f.shape[0] - border_y, border_x:original_img_f.shape[1] - border_x]

channel_row_cut = int(cropped_im.shape[0] // 3)

b = cropped_im[: channel_row_cut, :]
g = cropped_im[channel_row_cut: 2 * channel_row_cut, :]
r = cropped_im[2 * channel_row_cut: 3 * channel_row_cut, :]

border_y_b = int(b.shape[0] * 0.03)
border_x_b = int(b.shape[1] * 0.03)

border_y_r = int(r.shape[0] * 0.03)
border_x_r = int(r.shape[1] * 0.03)

border_y_g = int(g.shape[0] * 0.03)
border_x_g = int(g.shape[1] * 0.03)

b = b[border_y_b: b.shape[0] - border_y_b, border_x_b:b.shape[1] - border_x_b]
r = r[border_y_r: r.shape[0] - border_y_r, border_x_r:r.shape[1] - border_x_r]
g = g[border_y_g: g.shape[0] - border_y_g, border_x_g:g.shape[1] - border_x_g]

shift_b = [0, 0, float('-inf')]
shift_r = [0, 0, float('-inf')]

shift = 20

for x in range(-shift, shift + 1):
    for y in range(-shift, shift + 1):
        t_b = np.roll(b, x, axis=0).copy()
        t_b = np.roll(t_b, y, axis=1).copy()
        correlation = (t_b * g).sum()

        if correlation > shift_b[2]:
            shift_b = [x, y, correlation]

for x in range(-shift, shift + 1):
    for y in range(-shift, shift + 1):
        t_r = np.roll(r, x, axis=0).copy()
        t_r = np.roll(t_r, y, axis=1).copy()
        correlation = (t_r * g).sum()

        if correlation > shift_r[2]:
            shift_r = [x, y, correlation]

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

plp.show()
