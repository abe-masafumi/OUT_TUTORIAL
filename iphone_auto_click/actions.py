import pyautogui
import time

def click_at(x, y, wait_sec=0.2):
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()
    time.sleep(wait_sec)

def swipe_drag(x1=158, y1=822, x2=158, y2=730, duration=16.0, wait_sec=0):
    pyautogui.moveTo(x1, y1, duration=0.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(x1, y1, duration=0)  # 念のため同じ位置に移動
    pyautogui.dragTo(x2, y2, duration=duration, button='left')
    pyautogui.mouseUp()
    time.sleep(wait_sec)

def type_text(text, wait_sec=0.2):
    pyautogui.typewrite(text)
    time.sleep(wait_sec)

def hold_click(x, y, hold_sec=1.0, wait_sec=0.2):
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.mouseDown()
    time.sleep(hold_sec)
    pyautogui.mouseUp()
    time.sleep(wait_sec)

def wait(sec):
    time.sleep(sec)
