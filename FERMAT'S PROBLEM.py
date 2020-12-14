"""Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
an+ bn= cn
 for any values of n greater than 2
1. Write a function named check_fermat that takes four parameters a, b, c and n
- and checks to see if Fermat’s theorem holds. If n is greater than 2 and an +bn = cn
 the program should print, “Holy smokes, Fermat was wrong!”
Otherwise the program should print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n,
converts them to integers, and uses check_fermat to check whether they
violate Fermat’s theorem"""
def get_input():
    a = int(input('What value to use for a?\n'))
    b = int(input('What value to use for b?\n'))
    c = int(input('What value to use for c?\n'))
    n = int(input('What value to use for n?\n'))
    print(check_fermat(a, b, c, n))
def check_fermat(a, b, c, n):
    if n == 2:
        return 'Fermat got that one already.'
    elif n>2 and a**n + b**n == c**n:
        return 'Holy Smokes, Fermat was Wrong!'
    else:
        return "No, that doesn't work."
get_input()

