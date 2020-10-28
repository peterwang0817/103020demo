import yfinance as yf
import numpy as np

stockid = "2353.TW"
i = yf.Ticker(stockid)
hist = i.history(period="5y")
dates = hist["Open"].index
total = len(dates)
timeline = range(total)

list_close = hist["Close"]
list_kenkan = []
list_kijun = []
list_senkou_a = []
list_senkou_b = []
list_chikou = []

def ma(stockhistory,n,offset,datatype):
    #hist: history of stockid
    #n: number of days for moving average
    #offset: offset by how many days, default is 0
    #datatype: "open","close","high","low"
    values = stockhistory[datatype]
    value = 0
    for i in range(n):
        value += values[len(values)-i-1-offset]
    return round(value/n,2)

def phpl(stockhistory,date,n):  #just a common average used for solving lines
    highs = stockhistory["High"]
    lows = stockhistory["Low"]
    high = 0
    low = 1000000
    for i in range(n):
        if highs[date-n+1+i] > high:
            high = highs[date-n+1+i]
        if lows[date-n+1+i] < low:
            low = lows[date-n+1+i]
    if date < n-1: return 0
    return round((high+low)/2,2)

def calc_kenkan(stockhistory,date):
    return phpl(stockhistory,date,9)

def calc_kijun(stockhistory,date):
    return phpl(stockhistory,date,26)

def calc_senkou_b(stockhistory,date):
    return phpl(stockhistory,date,52)

for i in timeline:  #calculate the five lines
    kenkan = calc_kenkan(hist,i)
    kijun = calc_kijun(hist,i)
    senkou_a = 0
    senkou_b = 0
    chikou = 0
    if i-26 >= 0:
        senkou_a = round((list_kenkan[i-26]+list_kijun[i-26])/2,2)
        senkou_b = calc_senkou_b(hist,i-26)
    if i+26 <= total-1:
        chikou = round(list_close[i+26],2)
    
    list_kenkan.append(kenkan)
    list_kijun.append(kijun)
    list_senkou_a.append(senkou_a)
    list_senkou_b.append(senkou_b)
    list_chikou.append(chikou)
print("Successfully calculated Ichimoku lines")

#checks
def cloud(date):
    senkou_a = list_senkou_a[date]
    senkou_b = list_senkou_b[date]
    price = list_close[date]

    if price > senkou_a and price > senkou_b: return "above"
    if price < senkou_a and price < senkou_b: return "below"
    return False
        
def cross(date):
    if date == 0: return False
    kenkan = list_kenkan[date]
    kijun = list_kijun[date]
    if list_kenkan[date-1] < list_kijun[date-1]:  #kenkan passes above kijun
        if list_kenkan[date] > list_kijun[date]: return "long"
    if list_kenkan[date-1] > list_kijun[date-1]:  #kenkan passes below kijun
        if list_kenkan[date] < list_kijun[date]: return "short"
    return False

#scan all history for all entry signals
counter = 0
signals = []
longsignals = []
shortsignals = []

buysell = []

for i in timeline:
    check_cloud = cloud(i)
    check_cross = cross(i)
    if check_cloud == "above" and check_cross == "long":
        signals.append("longentry"+str(i))
        longsignals.append(i)
        buysell.append(1)
        counter += 1
    elif check_cloud == "below" and check_cross == "short":
        signals.append("shortentry"+str(i))
        shortsignals.append(i)
        buysell.append(-1)
        counter += 1
    else:
        signals.append("")
        buysell.append(0)
print("Found "+str(counter)+" signals")

#for each entry point, find exit point
for i in longsignals:
    for j in range(i,total):
        if (list_kenkan[j]-list_close[j])*(list_kenkan[j-1]-list_close[j-1])<0 and i!=j:
            signals[j]+=("longexit"+str(i))
            buysell[j]+=-1
            break
for i in shortsignals:
    for j in range(i,total):
        if (list_kenkan[j]-list_close[j])*(list_kenkan[j-1]-list_close[j-1])<0 and i!=j:
            signals[j]+=("shortexit"+str(i))
            buysell[j]+=1
            break

balance = 0
transactions = 0

print("---------------------------------------")
for i in timeline:
    if buysell[i] > 0:
        print("Bought 1000 shares for $" + str(1000*list_close[i]))
    if buysell[i] < 0 and transactions > 0:
        print("Sold 1000 shares for $" + str(1000*list_close[i]))
    transactions += buysell[i]
    balance += buysell[i]*list_close[i]*-1000
    if buysell[i] != 0:
        print("Balance is now $"+str(balance))
        print("You own "+str(transactions)+" shares")
        print(dates[i])
        print("---------------------------------------")
