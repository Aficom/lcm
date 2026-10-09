def find_lcm(a, b):
    greater = max(a, b)
    while True:
        if (greater % a == 0) and (greater % b == 0):
            return greater
        greater += 1
first = int(input("Input first number: "))
second = int(input("Input second number: "))
print(find_lcm(first, second))