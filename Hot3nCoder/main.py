import getopt
import re
import shutil
import os
import sys
from pathlib import Path

import src_process
import config_process
import math_process


def main(argv):
    inputfile = ''
    inputsymbol = ''
    try:
        opts, args = getopt.getopt(argv, "hi:s:", ["ifile=", "isymbol="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -s <inputsymbol')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <inputfile> -s <inputsymbol')
            print('space between each symbol')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

        elif opt in ("-s", "--isymbol"):
            inputsymbol = arg

    with open('config.txt', 'w', encoding='utf-8') as f:
        f.write(inputsymbol)


    # 先處理src # 內容
    shutil.copyfile(inputfile, "temp.cpp")
    src_process.hashtag_predeal("temp.cpp")
    # 取得正規化list
    normalized_src = src_process.normalize("temp.cpp")

    # check config if >=2
    config_process.adjust_size()

    # 生成符號 dic
    nsset = set(re.split(' |\n', normalized_src))
    emojilen = math_process.get_encode_slen(len(nsset), config_process.get_emoji_size())
    emojils = config_process.get_rand_emoji(emojilen)
    var_dict = math_process.generate_dic(nsset, emojils)

    map_src = re.split(' |\n', normalized_src)

    # define string
    definlines = []
    for i in var_dict:
        if var_dict[i] == '':
            continue
        definlines.append(f"#define {var_dict[i]} {i}")

    # writing HotE3coder.cpp
    ipfile_dic = str(Path(inputfile).parent.resolve())
    with open(ipfile_dic+'\Hot3nCoder.cpp', 'a', encoding='utf-8') as f:
        for line in definlines:
            f.write(line+'\n')

        linespsrc = normalized_src.splitlines()
        for line in linespsrc:
            stringsp = line.split(' ')
            for key in stringsp:
                f.write(var_dict[key]+' ')

            f.write('\n')

        f.write('\n/*Created by Jasoff*/')

    os.remove("temp.cpp")
    os.remove("config.txt")


if __name__ == '__main__':
    main(sys.argv[1:])
