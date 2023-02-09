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


def resize(image, width=256, height=256):
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
    return image


def convert_hash2rgb(hash_list):
    for i in range(len(hash_list) // 3):
        pixel = np.array([hash_list[3*i], hash_list[3*i+1], hash_list[3*i+2]])
        print(pixel)


# def replace(image, words, hash):

def convert_char2rgb(char):
    char = ord(char)
    pixel = np.array([char*2, char*2, char*2])
    return pixel


def replace_pixel(image, words, hash_list):
    for i in range(len(hash_list) // 2):
        location = [hash_list[2*i], hash_list[2*i+1]]
        image[location[0]][location[1]] = convert_char2rgb(words[i])
    return image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = cv2.imread("Test7.png")
    # av_hash = cv2.img_hash.AverageHash_create()
    # decimal2hex(av_hash.compute(test)[0])
    # bm_hash = cv2.img_hash.BlockMeanHash_create()
    # decimal2hex(bm_hash.compute(test)[0])
    # cm_hash = cv2.img_hash.ColorMomentHash_create()
    # print(cm_hash.compute(test))
    test = resize(test)
    mh_hash = cv2.img_hash.MarrHildrethHash_create()
    hash_array = mh_hash.compute(test)[0]
    decimal2hex(hash_array)
    convert_hash2rgb(hash_array)
    image = replace_pixel(test, "jkiueydhcnvwoxkemsdngdsjafdpaosgudas", hash_array)
    cv2.imshow("CRYPT", image)

    cv2.waitKey(0)

    # rv_hash = cv2.img_hash.RadialVarianceHash_create()
    # hash_list = rv_hash.compute(test)[0]
    # p_hash = cv2.img_hash.PHash_create()
    # decimal2hex(p_hash.compute(test)[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
