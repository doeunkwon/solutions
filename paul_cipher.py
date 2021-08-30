# link to the problem: https://edabit.com/challenge/9fbbjaLt22Zfvjjau

def paul_cipher(txt):
    lst = list(txt)
    alp = []
    c = 0
    for i in lst:
        ind = lst.index(i)
        if i.isalpha() is False:
            pass
        else:
            alp.append(i)
            if c == 0:
                lst[ind] = i.upper()
            else:
                prev_alp = ord(alp[c - 1].upper()) - 64
                curr_alp = ord(alp[c].upper()) - 64
                new_alp = prev_alp + curr_alp
                if new_alp > 26:
                    new_alp -= 26
                lst[ind] = chr(new_alp + 64).upper()
            c += 1
    return "".join(lst)

# tests
print(paul_cipher("muBas41r")) # "MHWCT41K"
print(paul_cipher("A1rForce")) # "A1SXUGUH"
print(paul_cipher("p4K1St4n")) # "P4A1DM4H"
print(paul_cipher("MATT")) # "MNUN"
print(paul_cipher("4elen10ve")) # "4EQQS10JA"
print(paul_cipher("He1lo")) # "HM1QA"
print(paul_cipher(" The quick brown fox jumps over the lazy dog. ")) # " TBM VLDLN MTGLK TUM HEHCI HKAW LBM QMAY CSV. "
print(paul_cipher("5ddc4ddf-7a47-44d3-8eda-3171860dc938")) # "5DHG4GHJ-7G47-44E3-8IIE-3171860EG938"
