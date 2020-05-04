# First task
result = [number for number in range(1, 1001) if '7' in str(number)]
# Second task
sentence = [word for word in 'Would it save you a lot of time if I just gave up and went mad now?' if
            word not in 'aeoiuyAEOUIY']
# Third task
phrase = "The ships hung in the sky in much the same way that bricks don't"
dict_result = {word:len(word) for word in phrase.split(' ')}
# Fourth task
max_result = [max([number for number in range(1, 10) if el % number == 0]) for el in range(1, 1001)]
# Fifth task
import re
def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None
last_result = [1]+[x for x in range(1001) if isprime(x)][4:] # list of all prime numbers except 3,5,7


if __name__=='__main__':
    print(result)
    print(sentence)
    print(dict_result)
    print(max_result)
    print(last_result)
