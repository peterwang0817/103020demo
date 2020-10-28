import yfinance as yf

filename = "volume300.txt"
file = open(filename,"r",encoding="utf8")
lines = file.readlines()
portfolio = []
notable = []
for line in lines:
    if line[0] != "#":
        portfolio.append(line[0:4]+".TW")
        

def ma(n,delay,hist):
    #n is the amount of days for moving average
    #delay is how many days ago
    closeprices = hist["Close"]
    value = 0
    for i in range(n):
        value += closeprices[len(closeprices)-i-1-delay]
    return round(value/n,2)

def cross(stock):
    hist = stock.history(period="3mo")
    today, yesterday = 0, 0
    buysell = "－"
    if ma(1,0,hist) > ma(20,0,hist): today = 1
    if ma(1,1,hist) > ma(20,1,hist): yesterday = 1
    if today == 0 and yesterday == 1:
        buysell = "空"
    if today == 1 and yesterday == 0:
        buysell = "多"
    if buysell != "－－":
        notable.append(buysell + " " + i.info["symbol"][:-3] + " " + stock.info["longName"])
    return buysell

def info(stock):
    return stock.info

for stock in portfolio:
    i = yf.Ticker(stock)
    print(cross(i) + " " + i.info["symbol"][:-3] + " " + i.info["longName"])

print("--------------------交叉股--------------------")
for i in notable:
    print(i)
