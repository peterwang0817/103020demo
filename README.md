# 103020demo
Welcome! These files are free for you to view and use. These go along with my presentation, showcasing yfinance and PTX.

PTX

這裡面有一個檔案timetable.py，可以顯示台鐵某車站的動態時刻表，檔案中有變數stationID，可以設為你想查的台鐵車站代號，預設是3360彰化，可以上網查詢這些代號(1000台北，3300台中)。該程式所用到的API可參見https://ptx.transportdata.tw/MOTC?t=Rail&v=3#!/TRA/StationLiveBoardApiController_Get_1


yfinance

我在這裡放了兩個示範程式：cross.py及ichimoku.py
cross.py中有一個變數名稱為filename，可以在這裡輸入一個文字檔的名稱，該資料夾中有兩個現成的檔案可以用：top100.txt涵蓋了台股加權指數權重前百名的股票代號與名稱，volume300.txt涵蓋了2019年某日成交量前300的股票。
cross.py會去分析每檔股的20日均線，當該均線與股價交叉時，會形成一個買進或賣出的訊號，該程式會顯示"多"或"空"。如果沒有訊號(代表當天沒有交叉)，則不會有顯示 (可參見https://en.wikipedia.org/wiki/Moving_average_crossover )。
ichimoku.py則是接受一個股票代號stockid，然後使用"一幕均衡表"(一種技術分析的方式，請參見https://zh.wikipedia.org/wiki/%E4%B8%80%E7%9B%AE%E5%9D%87%E8%A1%A1%E8%A1%A8),
然後會使用過去五年的資料，進行模擬交易，並最後輸出賺了多少錢 (或賠多少錢，說實話絕大多數的時候是賠錢啦)
