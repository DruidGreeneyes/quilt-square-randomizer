import random
import sys

def coord(x, num_rows, column_list):
    col, row = divmod(x, num_rows)
    row = row + 1
    col = column_list[col]
    return (row, col)
    
def main(args):
    l, h = 0, 0
    if len(args) > 1:
        l, h = int(args[0]), int(args[1])
    else:
        print('need both width and height arguments')
        exit()

    columns = []
    if h > 26:
        print('could not assign letters to column values -- too many columns')
        columns = [i + 1 for i in range(h)]
    else:
        a = ord('a')
        columns = [chr(i) for i in range(a, a + h)]

    random.seed()
    points = list(range(l * h))
    random.shuffle(points)

    for p in points:
        print(str(coord(p, l, columns)))

main(sys.argv[1:])
