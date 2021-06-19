# esjzone 小說更新通知
## 爬蟲方法
從json檔中讀入小說id，進行爬蟲，與存在json中最新話的id進行比對

若id不同，則將連結存進html檔中

## 郵件

寄信的動作使用 dawidd6/action-send-mail

用於寄信的google帳戶需要:

1. 安全性較低的應用程式存取權限 開啟
2. 解除人機驗證  https://accounts.google.com/b/0/DisplayUnlockCaptcha 
3. 開啟兩步驟驗證，取得應用程式密碼

寄信內文選擇html，檔案則選擇生成的html

## 判斷是否要寄信
如果沒更新，刪除html

因此當沒偵測到html，則不執行下面的動作

判斷是否有檔案使用 andstor/file-existence-action

## 更新最新話 id 

如果有最新話，更新json檔，在用git add和commit

之後用 ad-m/github-push-action 推回去

TOKEN 在設定->DEVELOPER 可以生成，權限全部開啟好

## 安全
信箱和蜜瑪，以及Github TOKEN 可以放在倉庫的 Secerts
就能在action中使用

## 小提醒
1. 檔案位置用相對路徑
2. requirements.txt 填上需要下載的模組就好了，上傳原先就有的會有警告
3. 不清楚為甚麼不能從 python 抓到環境變數
