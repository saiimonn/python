
def print_formatted(number):
    for i in range (1, number + 1):
        dec = i
        octal = format(i, 'o')
        hexa = format(i, 'X')
        bi = format(i, 'b')

        print(f"{dec:>2} {octal:>2} {hexa:>2} {bi:>2}")

n = int(input())
print_formatted(n)