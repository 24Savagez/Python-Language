import urllib.request
import datetime


def get_stock_quote(stock):
    # https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1609200000&period2=1609632000&interval=1d&events=history&includeAdjustedClose=true
    # https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1609200000&period2=1609632000&interval=1d&events=history&includeAdjustedClose=true
    param = "{}?period1=1609200000&period2=1609632000&interval=1d&events=history&includeAdjustedClose=true".format(
        stock
    )
    link = "https://query1.finance.yahoo.com/v7/finance/download/" + param
    with urllib.request.urlopen(link) as f:
        # s = f.read()  # bytes sequence
        s = []
        for i, line in enumerate(f):
            if i == 0:
                s.append("{},{}".format("stock", line.decode("utf8")))
            else:
                s.append("{},{}".format(stock, line.decode("utf8")))
    return "".join(s)
    # print(s)
    # print(s.decode("utf8"))
    # write string
    # with open("stock.csv", "w") as fw:
    #     fw.write(s.decode("utf8"))
    # write binary
    # with open("stock2.csv", "wb") as fw:
    #     fw.write(s)

    # return s


def write_stock_csv(filename, data):
    with open(filename, "w") as f:
        f.write(data)


symbols = ["scc.bk", "bbl.bk", "bh.bk"]
for symbol in symbols:
    q = get_stock_quote(symbol)
    write_stock_csv(symbol + ".csv", q)
