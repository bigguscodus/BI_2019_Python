def flat_list(array):
    flat = []
    for i in array:
        if type(i) == type(flat):
            flat.extend(flat_list(i))
        else:
            flat.append(i)
    return flat

