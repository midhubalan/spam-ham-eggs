"""import demo"""
import readport
# from tutorial import readport as rp
# import tutorial.readport as rp

def portfolio_cost(filename):
    portfolio = readport.read_portfolio(filename)
    return sum(count * price for _, count, price in portfolio)

def main(argv):
    if len(argv) == 1:
        filename = input("Enter filename:")
    elif len(argv) ==2:
        filename = argv[1]
    else:
        raise SystemExit(f'Usage {argv[0]} filename')
    port = portfolio_cost(filename)
    if (port != 0):
        print(f'Total cost of portfolio: {port:0.2f}')

if __name__ =="__main__":
    import sys
    main(sys.argv)


