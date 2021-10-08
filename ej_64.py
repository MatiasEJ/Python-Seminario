def operaciones(a:int ,b:int)->tuple:
    if b == 0:
        res = None
    else:
        res = a/b
    return ((a+b),(a-b),(a*b),(res))


def main():
    print(operaciones(18,9))
    print(operaciones(18,0))
    a = operaciones(18,9)
    # a[0] = 4
    list = []
    for val in a:
        list.append(val)
    print(list)
    print(list[0])
    list[0] = 12
    print(list)

main()