def get_target(answer_list):
    h = 0 # Clearly I do not follow my own advice on variable naming here.
    for a in answer_list:
        h = (h * 31 + a) % (10**9 + 7)
    return h

print(get_target([1, 4, 7, 2, 2, 3, 1, 4, 1, 2]))