# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def decimal2hex(hash_list):
    print(hash_list)
    hex_hash = ""
    count = 0
    for decimal in hash_list:
        i_hash = hex(decimal)[2:]
        count += 1
        if len(i_hash) < 2:
            i_hash = "0" + i_hash
        hex_hash += i_hash
    print(count)
    print(hex_hash)
    return hex_hash


def resize(image, width=256, height=256):
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
    return image


def convert_hash2rgb(hash_list):
    for i in range(len(hash_list) // 3):
        pixel = np.array([hash_list[3 * i], hash_list[3 * i + 1], hash_list[3 * i + 2]])
        print(pixel)


# def replace(image, words, hash):

def convert_char2rgb(char):
    char = ord(char)
    pixel = np.array([char * 2, char * 2, char * 2])
    return pixel


def replace_pixel(image, words, hash_list):
    for i in range(len(hash_list) // 2):
        location = [hash_list[2 * i], hash_list[2 * i + 1]]
        image[location[0]][location[1]] = convert_char2rgb(words[i])
    return image


def decimal2qua(hash_list):
    qua_hash = ""
    for decimal in hash_list:
        qua_hash += np.base_repr(decimal, base=4)
    return qua_hash


def adjust_y_position(char, qua_hash, dig_hash):
    # return y position offset for each char and given qua hash
    if qua_hash == 0:
        return ord(char) * (dig_hash % 2 * 2 - 1)
    elif qua_hash == 1:
        return 2 * ord(char) - dig_hash
    elif qua_hash == 2:
        return 2 * ord(char)
    elif qua_hash == 3:
        return ((ord(char) - 32) % 8 - 3) + 2 * ord(char)


def hash_hide(path):
    test = cv2.imread(path)
    test = resize(test)
    mh_hash = cv2.img_hash.MarrHildrethHash_create()
    hash_array = mh_hash.compute(test)[0]
    decimal2hex(hash_array)
    # convert_hash2rgb(hash_array)
    image = replace_pixel(test, "no body, not even the rain, has such small hands", hash_array)
    cv2.imshow("CRYPT", image)
    cv2.waitKey(0)


def hash_glitch(path):
    test = cv2.imread(path)

    # used as color
    # 72
    m_hash_func = cv2.img_hash.MarrHildrethHash_create()
    m_hash = m_hash_func.compute(test)[0]
    m_hash_hex = decimal2hex(m_hash)

    # used as qua offset
    # 32
    b_hash_func = cv2.img_hash.BlockMeanHash_create()
    b_hash = b_hash_func.compute(test)[0]
    b_hash_qua = decimal2qua(b_hash)

    # used as adj digit
    # 40
    r_hash_func = cv2.img_hash.RadialVarianceHash_create()
    r_hash = r_hash_func.compute(test)[0]

    # used as space offset
    # 8
    p_hash_func = cv2.img_hash.PHash_create()
    p_hash = p_hash_func.compute(test)[0]
    p_hash_hex = decimal2hex(p_hash)
    p_hash_ini = p_hash[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # hash_hide("Test8.png")
    test = cv2.imread("Test8.png")
    av_hash = cv2.img_hash.AverageHash_create()
    decimal2hex(av_hash.compute(test)[0])
    bm_hash = cv2.img_hash.BlockMeanHash_create()
    decimal2hex(bm_hash.compute(test)[0])
    cm_hash = cv2.img_hash.ColorMomentHash_create()
    print(cm_hash.compute(test))
    # mh_hash
    rv_hash = cv2.img_hash.RadialVarianceHash_create()
    decimal2hex(rv_hash.compute(test)[0])
    # p_hash = cv2.img_hash.PHash_create()
    # decimal2hex(p_hash.compute(test)[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
