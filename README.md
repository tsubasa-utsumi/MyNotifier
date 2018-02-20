# MyNotifier
ツイッターで色々通知してくれるようになるはず。

# キンドルのセール情報取得
- 30%以上をセールと見なしてます

## 使い方
```
import kindleCheck

kindleCheck.getSaleInfo(URL)
```

## 戻り値一覧
|戻り値|意味|
-|-
|30以上|割引率|
|0|セールと見なさない|
|-1|なんか失敗した|

# ツイッターで呟く
## 使い方
```
#coding: UTF-8
import tweet

tweet.tweet("テストだオラァ")
```

## 呟くための準備
- `./config` にツイッターのAPIキー等を設定する必要がある
  - configSAMPLEを見て設定すること
