# drone_japan_course2 課題提出

## 提出課題の概要
- キー入力でドローンを操作する
- ドローンのテレメトリを取得しターミナル上に表示する

**表示されるテレメトリの例**
```
 System status: STANDBY
 Is Armable?: True
 Armed: False
 Mode: LAND
 Global Location: LocationGlobal:lat=-35.339333,lon=149.1621416,alt=568.36
 pitch yaw roll: Attitude:pitch=-0.00780999520794,yaw=-0.184492304921,roll=-0.00790476892143
 valtage current level: Battery:voltage=12.587,current=0.0,level=0
```

## 利用するファイル
上記2点を同一フォルダに格納
1. key_ctrl.py
2. kbhit.py

## 動作確認の手順
1. sitlの起動:
```
sim_vehicle.py -v ArduCopter
```
2. 新しいターミナルを起動
vscodeのターミナル右上の`+`をクリック
![ターミナルの画像](https://github.com/yoppii12/drone_japan_course2/blob/master/%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%88%202020-07-18%20015206.jpg)


3. 「利用するファイル」2点を設置いただいたディレクトリに移動
```
cd hogehoge
```

4. 提出課題の実行
```
python key_ctrl.py
```

上記1-4で提出課題のプログラムが実行されます。

## 操作方法
キーボードからコマンド入力で操作します。
1. `g`を入力：guidedモードに切り替え
2. `a`を入力：armedされる
3. `t`を入力：離陸する

以降、順不同  
`1`を入力:柏の葉キャンパス交番上空30mへ移動します。  
`2`を入力:三井ガーデンホテル上空50mへ移動します。  
`l`を入力:着陸します。  
`r`を入力:RTHします。  
  
以上




