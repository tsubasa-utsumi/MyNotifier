# 特定のマンガのキンドル版のセール情報を取得する
```
#coding: UTF-8
import kindleCheck
import tweet

URL = "監視したい本のURL"
status = kindleCheck.getSaleInfo(URL)

if status >= 30:
  tweet.tweet("@自分 セール中だぞ！ " + URL)
```
一応サンプル : [sample.py](sample.py)

# キンドルのセール情報取得
[kindleCheck.py](kindleCheck.py) を使って下さい。
## 使い方
```
import kindleCheck

kindleCheck.getSaleInfo(URL)
```

## 戻り値一覧
|戻り値|意味|
-|-
|0以上|割引率|
|-1|割引が無いとかなんか失敗したとか|

# ツイッターで呟く
[tweet.py](tweet.py) を使って下さい。
## 使い方
```
#coding: UTF-8
import tweet

tweet.tweet("テストだオラァ")
```

## 呟くための準備
- `./config` にツイッターのAPIキー等を設定する必要がある
  - configSAMPLEを見て設定すること
