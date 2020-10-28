# 103020demo
Welcome! These files are free for you to view and use. These go along with my presentation, showcasing yfinance and PTX.

yfinance

我在這裡放了兩個示範程式：cross.py及ichimoku.py
cross.py中有一個變數名稱為filename，可以在這裡輸入一個文字檔的名稱，該資料夾中有兩個現成的檔案可以用：top100.txt涵蓋了台股加權指數權重前百名的股票代號與名稱，volume300.txt涵蓋了2019年某日成交量前300的股票。cross.py會去分析每檔股的20日均線，當該均線與股價交叉時，會形成一個買進或賣出的訊號，該程式會顯示"多"或"空"。如果沒有訊號(代表當天沒有交叉)，則不會有顯示。
ichimoku.py則是接受一個股票代號stockid，然後使用"一幕均衡表"(一種技術分析的方式，請參見)，然後會使用過去五年的資料，進行模擬交易，並最後輸出賺了多少錢 (或賠多少錢，說實話絕大多數的時候是賠錢啦)
