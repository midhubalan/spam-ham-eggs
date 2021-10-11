"""read portfolio from csv file"""
import csv


def read_portfolio(filename):
    portfolio = []
    try:
        with open(filename, 'rt') as file:
            rows = csv.reader(file)
            for row in rows:
                try:
                    name = row[0]
                    count = int(row[1])
                    price = float(row[2])
                    holding = (name, count, price)
                    portfolio.append(holding)
                except ValueError as err:
                    print("Bad row: ", row)
                    print("Reason ", err)
    except FileNotFoundError as _:
        print(f"{filename} does not exist. Enter valid file name")
    return portfolio

def main(argv):
    if len(argv) == 1:
        filename = input("Enter filename: ")
    elif len(argv) == 2:
        filename = argv[1]
    else:
        raise SystemExit(f'Usage {argv[0]} filename')

    pf = read_portfolio(filename)

    for name, count, price in pf:
        print(f'{name:>10s} {count:10d} {price:10.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)

