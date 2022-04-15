def tips_spread(arg):
    ret = []
    for i in arg:
        ret.extend(i) if isinstance(i, list) else ret.append(i)
    return ret

print(tips_spread([2, 4, 6, [1, 3, 5], [7], 8, 9]))


            
            