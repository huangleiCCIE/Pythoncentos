# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @author   : thomas_liu
# @motto    : life is short , i use python.

from difflib import *

def diff_file(file1, file2):
    txt1 = open(file1, 'r').readline()
    txt2 = open(file2, 'r').readline()
    result = Differ().compare(txt1, txt2)
    return_result = '\r\n'.join(list(result))
    return return_result

def diff_txt(txt1,txt2):
    txt1_list = txt1.split('\r\n')
    txt2_list = txt2.split('\r\n')
    result = Differ().compare(txt1_list, txt2_list)
    return_result =  '\r\n'.join(list(result))
    return return_result

if __name__ == "__main__":
    txt_1 = "\r\n123456"
    txt_2 = "\r\n123465789"
    print(diff_txt(txt_1,txt_2))


