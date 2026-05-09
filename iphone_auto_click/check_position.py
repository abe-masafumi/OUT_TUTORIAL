import pyautogui
import time

print('Ctrl+Cで終了します')
try:
    while True:
        x, y = pyautogui.position()
        print(f'現在のマウス座標: x={x}, y={y}', end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\n終了しました')
