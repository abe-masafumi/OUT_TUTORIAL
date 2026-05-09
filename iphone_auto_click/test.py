import pyautogui
import time

# 操作したい座標をここに設定（例: x=500, y=300）
POSITIONS = [
    (160, 846),  # スタート
]

# 1回の操作で待機する秒数
WAIT_SEC = 2
# 長押しする秒数
HOLD_SEC = 1
# 繰り返し回数（10分間なら調整）
REPEAT = 1  # テスト用に5回繰り返し


print('3秒後に開始し、まず(160, 846)でウィンドウをアクティブ化します。')
time.sleep(3)
pyautogui.moveTo(160, 846, duration=0.2)
pyautogui.click()
time.sleep(0.5)

for i in range(REPEAT):
    print(f'{i+1}回目')
    for x, y in POSITIONS:
        time.sleep(0.5)  # 各クリック前に0.5秒待機
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(HOLD_SEC)
        pyautogui.mouseUp()
        time.sleep(WAIT_SEC)
print('完了しました')
