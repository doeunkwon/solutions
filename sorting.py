# link to the problem: https://edabit.com/challenge/fRZMqCpyxpSgmriQ6

def sorting(s):
    c = 0
    str_list = []
    int_list = []
    for i in s:
        if ord(i) in list(range(65,122)):
            str_list.append(i)
        else:
            int_list.append(int(i))
    for j in str_list:
        lowest = j
        c += 1
        rest = str_list[c:]
        for k in rest:
            if lowest.isupper():
                if lowest.lower() in rest:
                    if k < lowest.lower():
                        lowest = k
                    else:
                        lowest = lowest.lower()
                else:
                    if k.upper() < lowest:
                        lowest = k
            else:
                if k.lower() < lowest:
                    lowest = k
        ind_j = str_list.index(j)
        ind_low = str_list.index(lowest)
        str_list[ind_j], str_list[ind_low] = str_list[ind_low], str_list[ind_j]
    int_list.sort()
    stringed_str = "".join(str_list)
    int_to_str = [str(int) for int in int_list]
    stringed_int = "".join(int_to_str)
    return stringed_str + stringed_int

# tests
print(sorting("eA2a1E")) # "aAeE12"
print(sorting("Re4r")) # "erR4"
print(sorting("6jnM31Q")) # "jMnQ136"
print(sorting("f5Eex")) # "eEfx5"
print(sorting("846ZIbo")) # "bIoZ468"
print(sorting("2lZduOg1jB8SPXf5rakC37wIE094Qvm6Tnyh")) # "aBCdEfghIjklmnOPQrSTuvwXyZ0123456789"
