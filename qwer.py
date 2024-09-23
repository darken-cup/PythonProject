import cv2
import numpy as np
import matplotlib.pyplot as plt


def passImg():
    img1 = cv2.imread('junren.jpg', 1)  # 读取彩色图像（BGR格式）
    h, w = img1.shape[:2]

    # 生成密码，加密
    key_img = np.random.randint(0, 256, size=(h, w, 3), dtype=np.uint8)  # 生成随机数，指定宽高和通道
    img_bit_add = cv2.bitwise_xor(img1, key_img)
    print(key_img.shape, img1.shape)

    # 解密
    img_bit_sum = cv2.bitwise_xor(key_img, img_bit_add)

    # 将 BGR 转换为 RGB
    img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    key_img_rgb = cv2.cvtColor(key_img, cv2.COLOR_BGR2RGB)
    img_bit_add_rgb = cv2.cvtColor(img_bit_add, cv2.COLOR_BGR2RGB)
    img_bit_sum_rgb = cv2.cvtColor(img_bit_sum, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(2, 2, 1), plt.title('img'), plt.imshow(img1_rgb)
    plt.subplot(2, 2, 2), plt.title('key'), plt.imshow(key_img_rgb)
    plt.subplot(2, 2, 3), plt.title('bird'), plt.imshow(img_bit_add_rgb)
    plt.subplot(2, 2, 4), plt.title('bird_sum'), plt.imshow(img_bit_sum_rgb)
    plt.show()


if __name__ == '__main__':
    passImg()

# import cv2
# import matplotlib.pyplot as plt
#
# # 读取图片，默认以BGR格式读取
# image = cv2.imread('junren.jpg')
#
# # 将BGR转换为RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# # 显示图片
# plt.imshow(image_rgb)
# plt.title('Image in RGB')
# plt.axis('off')  # 不显示坐标轴
# plt.show()
