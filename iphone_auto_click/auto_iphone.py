import pyautogui
import time

# 操作したい座標と操作種別をここに設定
# (x, y, 操作種別, オプション...)
POSITIONS = [
    (160, 846, "click"),      # スタート
    (218, 846, "click"),      # 同意
    (160, 823, "click"),      # 次へ
    (223, 819, "click"),      # 右手でクリック
    (160, 9960, "click"),     # 決定
    (136, 8785, "click"),     # 名前入力欄クリック
    (160, 846, "type", "a"),  # a入力
    (159, 9917, "click"),     # 決定
    (210, 9927, "click"),     # はい
    (210, 9927, "click"),     # クリック
    (210, 9927, "click"),     # クリック
    (210, 9927, "click"),     # クリック
    (210, 9927, "click"),     # クリック
    (161, 8537, "hold", 1.5), # クリック長押し
    (158, 8337, "swipe", 158, 8000, 0.8), # スワイプで歩行
]

# 1回の操作で待機する秒数
WAIT_SEC = 2
# 長押しする秒数
HOLD_SEC = 1
# 繰り返し回数（10分間なら調整）
REPEAT = 5  # テスト用に5回繰り返し

print('3秒後に開始し、まず(160, 846)でウィンドウをアクティブ化します。')
time.sleep(3)
pyautogui.moveTo(160, 846, duration=0.2)
pyautogui.click()
time.sleep(1.0)

for i in range(REPEAT):
    print(f'{i+1}回目')
    for op in POSITIONS:
        time.sleep(1.0)
        if op[2] == "click":
            x, y = op[0], op[1]
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click()
            time.sleep(WAIT_SEC)
        elif op[2] == "type":
            x, y, _, text = op
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click()
            time.sleep(0.3)
            pyautogui.typewrite(text)
            time.sleep(WAIT_SEC)
        elif op[2] == "hold":
            x, y, _, hold_sec = op
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.mouseDown()
            time.sleep(hold_sec)
            pyautogui.mouseUp()
            time.sleep(WAIT_SEC)
        elif op[2] == "swipe":
            x1, y1, _, x2, y2, duration = op
            pyautogui.moveTo(x1, y1, duration=0.2)
            pyautogui.mouseDown()
            pyautogui.moveTo(x2, y2, duration=duration)
            pyautogui.mouseUp()
            time.sleep(WAIT_SEC)
print('完了しました')
