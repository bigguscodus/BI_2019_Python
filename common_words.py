def checkio(first, second):
    first=set(first.lower().split(','))
    second=set(second.lower().split(','))
    temp=sorted(list(first.intersection(second)))
    answer=""
    for word in temp:
        answer+=word+","
    return(answer[:-1])
