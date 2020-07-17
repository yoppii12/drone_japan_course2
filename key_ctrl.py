#!usr/bin/env python
# -*- coding: utf-8 -*-
from signal import signal, SIGINT   # Ctrl+C(SIGINT)の送出のために必要
import time                         # ウェイト関数time.sleepを使うために必要
from dronekit import LocationGlobal, LocationGlobalRelative   # ウェイポイント移動に使いたいのでインポート
from dronekit import VehicleMode    # VehicleModeも使いたいのでインポート
from dronekit import connect        # connectを使いたいのでインポート
from kbhit import *                 # kbhitを使うために必要(同じフォルダにkbhit.pyを置くこと)
print("dronekitスタート")    # 開始メッセージ

# 必要なライブラリをインポート

# kbhit()を使うための「おまじない」を最初に２つ書く
atexit.register(set_normal_term)
set_curses_term()

#connection_stringの生成
connection_string = "127.0.0.1:14550"  # Raspberry Piのシリアル接続だとttyS0、ボーレートは57.6k

# フライトコントローラ(FC)へ接続
print("FCへ接続: %s" % (connection_string))    # 接続設定文字列を表示
vehicle = connect(connection_string, wait_ready=True)    # 接続

#Ctrl+cが押されるまでループ
try:
    while True:
        if kbhit():     # 何かキーが押されるのを待つ
            key = getch()   # 1文字取得

            # keyの中身に応じて分岐
            if key == 'g':                # guided
                vehicle.mode = VehicleMode('GUIDED')
            elif key == 'l':              # land
                vehicle.mode = VehicleMode('LAND')
            elif key == 'a':              # arm
                vehicle.armed = True
            elif key == 'd':              # disarm
                vehicle.armed = False
            elif key == 't':              # takeoff
                vehicle.simple_takeoff(alt=10)
            elif key == '1':              # simple_goto
                # 柏の葉キャンパス交番上空30mへ
                point = LocationGlobalRelative(35.893246, 139.954909, 30)
                vehicle.simple_goto(point)
            elif key == '2':              # simple_goto
                # 三井ガーデンホテル上空50mへ
                point = LocationGlobalRelative(35.895236, 139.952468, 50)
                vehicle.simple_goto(point)
            elif key == 'r':              # RTL
                vehicle.mode = VehicleMode('RTL')

        # ここはif文と同じインデントなので，キーに関係なく1秒に1回実行される
        # 現在の状態を表示
        print("--------------------------")
        print(" System status: %s" % vehicle.system_status.state)
        print(" Is Armable?: %s" % vehicle.is_armable)
        print(" Armed: %s" % vehicle.armed)
        print(" Mode: %s" % vehicle.mode.name)
        print(" Global Location: %s" % vehicle.location.global_frame)
        print(" pitch yaw roll: %s" % vehicle.attitude)
        print(" valtage current level: %s" % vehicle.battery)
        time.sleep(1)

except(KeyboardInterrupt, SystemExit):    # Ctrl+cが押されたら離脱
    print("SIGINTを検知")

# フライトコントローラとの接続を閉じる
vehicle.close()

time.sleep(1)   # 終了完了のために1秒待つ

print("終了．")    # 終了メッセージ
