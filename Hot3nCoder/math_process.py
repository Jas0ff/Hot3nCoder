import math


def get_encode_slen(dicnum, emojinum):
    return math.ceil(math.log(dicnum, emojinum))


def generate_dic(var_set, emj_ls):
    var_dict = dict.fromkeys(var_set, '')
    count = 0
    for i in var_dict:
        if i == '':
            continue
        var_dict[i] = emj_ls[count]
        count += 1

    return var_dict
