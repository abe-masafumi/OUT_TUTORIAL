import pyautogui
import time

# 操作したい座標と操作種別をここに設定
# (x, y, 操作種別, オプション..., 説明)
POSITIONS = [
    (160, 846, "click", None, "スタート"),      # 0
    (218, 846, "click", None, "同意"),         # 1
    (160, 823, "click", None, "次へ"),         # 2
    (223, 819, "click", None, "右手でクリック"),# 3
    (157, 994, "click", None, "決定"),         # 4
    (136, 880, "click", None, "名前入力欄クリック"), # 5
    (160, 846, "type", "a", "a入力"),          # 6
    (159, 993, "click", None, "決定"),         # 7
    (210, 992, "click", None, "はい"),         # 8
    (210, 992, "click", None, "クリック"),     # 9
    (210, 992, "click", None, "クリック"),     # 10
    (210, 992, "click", None, "クリック"),     # 11
    (210, 992, "click", None, "クリック"),     # 12
    (161, 853, "hold", 1.5, "クリック長押し"), # 13
    (158, 833, "swipedrag", (158, 800, 18.0), "8秒かけてゆっくりスワイプ"), # 14
    (158, 833, "click", None, "スワイプ後クリック"), # 15
    (158, 833, "swipedrag", (158, 800, 18.0), "8秒かけてゆっくりスワイプ"), # 16
    (158, 833, "swipedrag", (158, 800, 18.0), "8秒かけてゆっくりスワイプ"), # 17
    (270, 1002, "click", None, "#18 クリック"), # 18
    (228, 816, "click", None, "#19 クリック"), # 19
    (228, 816, "click", None, "#20 クリック"), # 20
    (158, 833, "swipedrag", (158, 800, 3.0), "8秒かけてゆっくりスワイプ"), # 21
    (270, 1002, "click", None, "#22 クリック"), # 22
    (228, 816, "click", None, "#23 クリック"), # 23
    (170, 859, "click", None, "#24 クリック"), # 24
    (222, 700, "click", None, "#25 クリック"), # 25
    (270, 1002, "click", None, "#26 クリック"), # 26
    (228, 816, "click", None, "#27 クリック"), # 27
    (228, 816, "click", None, "#28 クリック"), # 28
    (251, 859, "click", None, "#29 クリック"), # 29
    (251, 859, "click", None, "#30 クリック"), # 30
    (251, 859, "click", None, "#31 クリック"), # 31
    (170, 859, "click", None, "#32 クリック"), # 32
    (222, 700, "click", None, "#33 クリック"), # 33
    (222, 700, "click", None, "#34 クリック"), # 34
    (270, 1002, "click", None, "#35 クリック"), # 35
    (228, 816, "click", None, "#36 クリック"), # 36
    (270, 1002, "click", None, "#37 クリック"), # 37
    (228, 816, "click", None, "#38 クリック"), # 38
    (158, 833, "swipedrag", (158, 800, 2.0), "8秒かけてゆっくりスワイプ"), # 39
    (270, 1002, "click", None, "#40 クリック"), # 40
    (228, 816, "click", None, "#41 クリック"), # 41
    (251, 859, "click", None, "#42 クリック"), # 42
    (170, 859, "click", None, "#43 クリック"), # 43
    (222, 700, "click", None, "#44 クリック"), # 44
    (158, 833, "swipedrag", (158, 800, 4.0), "8秒かけてゆっくりスワイプ"), # 45
    (222, 700, "click", None, "#46 クリック"), # 46
    (222, 700, "click", None, "#47 クリック"), # 47
    (222, 700, "click", None, "#48 クリック"), # 48

]


# 1回の操作で待機する秒数
WAIT_SEC = 2
# 長押しする秒数
HOLD_SEC = 1
# 繰り返し回数（10分間なら調整）
REPEAT = 1  # テスト用に1回繰り返し

# 途中から実行したい場合はここを変更（0なら最初から、5なら6番目から）
START_INDEX = 1


print('3秒後に開始し、まず(160, 846)でウィンドウをアクティブ化します。')
time.sleep(3)
pyautogui.moveTo(160, 846, duration=0.2)
pyautogui.click()
time.sleep(1.0)

for i in range(REPEAT):
    print(f'{i+1}回目')
    for op in POSITIONS[START_INDEX:]:
        desc = op[4] if len(op) > 4 else ""
        if desc:
            print(f'操作: {desc}')
        time.sleep(1.0)
        if op[2] == "click":
            x, y = op[0], op[1]
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click()
            time.sleep(WAIT_SEC)
            if desc == "はい":
                print("10秒待機（はいの後）")
                time.sleep(10)
            # #32の後に8秒待機
            if desc == "#32 クリック":
                print("#32クリック後に8秒待機")
                time.sleep(8)
            # #36の後に2秒待機
            if desc == "#36 クリック":
                print("#36クリック後に2秒待機")
                time.sleep(2)
            # #46の後に10秒待機
            if desc == "#46 クリック":
                print("#46クリック後に10秒待機")
                time.sleep(10)
            # #47の後に8秒待機
            if desc == "#47 クリック":
                print("#47クリック後に8秒待機")
                time.sleep(10)
            # #48の後に10秒待機
            if desc == "#48 クリック":
                print("#48クリック後に10秒待機")
                time.sleep(10)
        elif op[2] == "type":
            # キーボード入力のみ
            _, _, _, text, *_ = op
            pyautogui.typewrite(text)
            time.sleep(WAIT_SEC)
        elif op[2] == "hold":
            x, y, _, hold_sec, *_ = op
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.mouseDown()
            time.sleep(hold_sec)
            pyautogui.mouseUp()
            time.sleep(WAIT_SEC)
        elif op[2] == "swipe":
            x1, y1, _, swipe_opts, *_ = op
            x2, y2, duration = swipe_opts
            pyautogui.moveTo(x1, y1, duration=0.2)
            pyautogui.mouseDown()
            pyautogui.moveTo(x2, y2, duration=duration)
            pyautogui.mouseUp()
            time.sleep(WAIT_SEC)
        elif op[2] == "swipedrag":
            x1, y1, _, drag_opts, *_ = op
            x2, y2, duration = drag_opts
            pyautogui.moveTo(x1, y1, duration=0.2)
            pyautogui.dragTo(x2, y2, duration=duration, button='left')
            time.sleep(WAIT_SEC)
            # #21だけ10秒待機、それ以外は5秒待機
            if desc == "8秒かけてゆっくりスワイプ":
                if op is POSITIONS[21]:
                    print("#21 swipedrag後に10秒待機")
                    time.sleep(10)
                else:
                    print("swipedrag後に5秒待機")
                    time.sleep(5)
print('完了しました')
