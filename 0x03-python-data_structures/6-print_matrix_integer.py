#!/usr/bin/pythong3
def print_matrix_integer(matrix=[[]]):
    def print_row(row):
        for num in row:
            print("{:d}".format(num), end=' ')
        print('$')

    for row in matrix:
        print_row(row)
    print('--$')
