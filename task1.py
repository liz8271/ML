from math import inf
from typing import List
def hello(name=None)->str:
    if name==None or name=='': 
        return 'Hello!'
    else:
        return 'Hello, ' + name +  '!'

def int_to_roman(num: int)->str:
   ret = ''
   for arab, roman in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
       while num >= arab:
           ret += roman
           num -= arab
   return ret

def longest_common_prefix(strs_input: List[str]) -> str:
    if len(strs_input) == 0:
        return ''
    copy = list(map(lambda word: word.lstrip(), strs_input))
    s = copy[0]
    for i in range(1, len(copy)):
        while copy[i].find(s) != 0 :
            s = s[:-1]
    return s

def primes() -> int:
    n=2
    while(True):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n
        n += 1

class BankCard:
    def __init__(self, total_sum: int, balance_limit = inf):
        self.total_sum=total_sum
        self.balance_limit=balance_limit
    def __repr__(self):
        return "To learn the balance call balance." 
    def __call__(self, spend_sum: int):
        if self.total_sum>=spend_sum:
            self.total_sum-=spend_sum
            print("You spent " +str (spend_sum)+ " dollars.")
            return (self.total_sum)
        else:
            print("Not enough money to spend "+ str(spend_sum) +" dollars.")
            raise ValueError
    def __add__(self, other): 
        return BankCard(self.total_sum + other.total_sum, max(self.balance_limit,other.balance_limit))
    @property
    def balance(self):
        if self.balance_limit>0:
            self.balance_limit-=1
            return self.total_sum
        else:
            print("Balance check limits exceeded.")
            raise ValueError
    def put(self, put_sum: int):
        self.total_sum+=put_sum
        print( "You put " + str(put_sum) + " dollars.")
    def print_balance(self):
        print( "To learn the balance call balance.")
    