# MyNotifier

色々通知してくれるようになるはず。

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
