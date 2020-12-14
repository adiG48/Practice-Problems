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

