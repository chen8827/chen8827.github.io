# [Taipei Bar Map](https://tpe-bar-god.herokuapp.com/)

* Using SQLite, asyncio, pandas, pyquery, requests to build a crawler and deploy on Heroku with connected to Line ChatBot.
* 這是一個用 Flask, Bootstrap, SQLite, D3.js 架設並部署在 Azure 的 Ptt 爬蟲資料視覺化網站
* 使用者登入功能(Flask-login)
* 響應式(RWD)網站設計
* 目前DB共有五個板名，HatePolitics(政黑板)、Beauty(表特板)、Soft_Job(軟體板)、NBA、Stock(股票板)、Tech_Job(科技板)
* 選擇其中一個板名，按下查詢，從後台SQLite資料庫查詢
* 列出各個欄位，ex: 編號、文章ID、推噓數量、作者、標題、日期、內文...
* 換頁功能與跳轉頁碼(Flask-Paginate)
* 將各板的推噓數量級距做資料視覺化(D3.js)
* 部署到 Azure web services (目前因金錢原因取消部署)
* Jieba斷詞與文字雲(wordcloud)顯示 (因速度效能遇到障礙而取消)

## Built With
* python
  - csv
  - numpy
  - pandas
* CSS
* Folium
* Dash
* Flask
* Heroku

## Getting Started

* 尚未有帳號密碼，所以導至登入頁面
<img src='./static/img/1.PNG' width='750px'>
![demo](./static/img/4.gif)

* 登入成功後，進到首頁
<img src='./static/img/2.PNG' width='750px'>

* 選擇板名，並按下搜尋，列出DB爬蟲的資料
<img src='./static/img/3.PNG' width='750px'>

* 點選上方導覽列的 `DATA VISUALIZATION`，看到各板推噓數量的級距分配圖
<img src='./static/img/4.gif' width='750px'>
