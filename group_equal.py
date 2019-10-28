def checkio(x):
    answer = [[el] for el in x]
    for el in range(len(answer) - 1):
        while answer[el] == answer[el + 1]:
            answer[el].extend(answer[el + 1])
            answer[el + 1].append('remove_flag')
    answer = [el for el in answer if 'remove_flag' not in el]
    for el in range(len(answer)):
        if el == 0:
            continue
        if answer[el][0] in answer[el - 1]:
            answer[el - 1].extend(answer[el])
            answer[el].append('remove_flag')
    answer = [el for el in answer if 'remove_flag' not in el]
    return answer
