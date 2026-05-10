
from actions import click_at, swipe_drag, type_text, hold_click, wait
import sys

def scenario():
    return [
        # 0
        lambda: print('まず(160, 846)でウィンドウをアクティブ化します。'),
        # 1 アクティブ化
        lambda: click_at(160, 846, 0.5),
        # 2
        lambda: click_at(160, 846, 0.5),
        # 3 スタート
        lambda: click_at(218, 846, 1.5),
        # 4 同意
        lambda: click_at(160, 823, 2.0),
        # 5 次へ
        lambda: click_at(223, 819, 1.5),
        # 6 右手でクリック
        lambda: click_at(157, 994, 1.5),
        # 7 名前入力クリック
        lambda: click_at(136, 880, 1.5),
        # 8 a入力
        lambda: type_text("yau-zya", 1.5),
        # 9 決定
        lambda: click_at(159, 993, 1.0),
        # 10 適当クリック
        lambda: click_at(210, 992, 12.0),
        # 11 はい
        lambda: click_at(210, 992, 5.0),
        # 12 適当クリック
        lambda: click_at(210, 992, 15.0),
        # 13 移動
        lambda: swipe_drag(duration=12.0),
        # 14 モーダルクリック
        lambda: click_at(158, 833, 2.0),
        # 15 戦闘 少し移動 
        lambda: swipe_drag(duration=2.5, wait_sec=8.0),
        # 16 戦闘まで 移動 → 戦闘終了
        lambda: swipe_drag(duration=10.0, wait_sec=7.0),
        # 17 戦闘後移動
        lambda: swipe_drag(duration=10.0, wait_sec=7.0),
        # 18 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 19 スキップ はい
        lambda: click_at(228, 816, 5.0),
        # 20 モーダルクリック
        lambda: click_at(228, 816, 5.0),
        # 21 ボス戦 少し前に移動
        lambda: swipe_drag(duration=1.5, wait_sec=11.0),
        # 22 スキップ選択
        lambda: click_at(270, 1002, 2.0),
        # 23 スキップ はい
        lambda: click_at(228, 816, 2.0),
        # 24 閉じる
        lambda: click_at(170, 859, 2.0),
        # 25 スキル選択
        lambda: click_at(222, 700, 3.0),
        # 26 スキップ選択
        lambda: click_at(270, 1002, 2.0),
        # 27 スキップ はい
        lambda: click_at(228, 816, 2.0),
        # 28 モーダルクリック
        lambda: click_at(228, 816, 2.0),
        # 29 右矢印
        lambda: click_at(251, 859, 1.0),
        # 30 右矢印
        lambda: click_at(251, 860, 1.5),
        # 31 右矢印
        lambda: click_at(252, 859, 1.5),
        # 32 右矢印
        lambda: click_at(250, 859, 1.5),
        # 33 閉じる
        lambda: click_at(170, 859, 10),
        # 34 スキル選択
        lambda: click_at(222, 700, 1.0),
        # 35 スキル選択
        lambda: click_at(222, 700, 10.0),
        # 36 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 37 スキップ はい
        lambda: click_at(228, 816, 5),
        # 38 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 39 スキップ はい
        lambda: click_at(228, 816, 4.0),
        # 40 移動 アイテムオブジェまで移動
        lambda: swipe_drag(duration=2.5, wait_sec=2.0),
        # 41 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 42 スキップ はい
        lambda: click_at(228, 816, 1.0),
        # 43 右矢印
        lambda: click_at(251, 859, 1.0),
        # 44 右矢印
        lambda: click_at(252, 860, 1.0),
        # 45 閉じる
        lambda: click_at(170, 859, 2.0),
        # 46 スキル選択
        lambda: click_at(222, 700, 2.0),
        # 47 移動 戦闘完了まで
        lambda: swipe_drag(duration=3.5, wait_sec=9.0),
        # 48 スキル選択
        lambda: click_at(222, 700, 15),
        # 49 スキル選択
        lambda: click_at(222, 700, 15),
        # 50 スキル選択
        lambda: click_at(222, 700, 15),
        # 51 スキル選択
        lambda: click_at(222, 700, 10.0),
        # 52 移動 戦闘完了まで
        lambda: swipe_drag(duration=5.5, wait_sec=10.0),
        # 53 スキル選択
        lambda: click_at(222, 700, 10),
        # 54 スキル選択
        lambda: click_at(222, 700, 10),
        # 55 スキル選択
        lambda: click_at(222, 700, 0.5),
        # 56 移動 戦闘完了まで
        lambda: swipe_drag(duration=6.5, wait_sec=1.0),
        # 57 スキル選択
        lambda: click_at(222, 700, 0.5),
        # 58 移動 ボス戦闘まで
        lambda: swipe_drag(duration=5.0, wait_sec=2.0),
        # 59 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 60 スキップ はい
        lambda: click_at(228, 816, 84.0),
        # 61 モーダルクリック
        lambda: click_at(228, 816, 1.5),
        # 62 モーダルクリック
        lambda: click_at(228, 816, 1.5),
        # 63 モーダルクリック
        lambda: click_at(228, 816, 1.5),
        # 64 モーダルクリック
        lambda: click_at(228, 816, 1.5),
        # 65 モーダルクリック
        lambda: click_at(228, 816, 1.5),
        # 66 モーダルクリック
        lambda: click_at(228, 816, 7.5),
        # 67 モーダルクリック
        lambda: click_at(228, 816, 7.5),
        # 68 モーダルクリック
        lambda: click_at(228, 816, 7.5),
        # 69 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 70 スキップ はい
        lambda: click_at(228, 816, 90.0),
        # 71 モーダルクリック
        lambda: click_at(228, 816, 7.5),
        # 72 モーダルクリック
        lambda: click_at(228, 816, 7.5),
        # 73 ぼうけん
        lambda: click_at(87, 1009, 5.0),
        # 74 モーダルクリック
        lambda: click_at(228, 816, 7.5),
        # 75 モーダルクリック
        lambda: click_at(159, 808, 5.0),
        # 76 ステージ1
        lambda: click_at(159, 665, 2.0),
        # 77 モーダルクリック
        lambda: click_at(159, 808, 5.0),
        # 78 モーダルクリック
        lambda: click_at(160, 891, 3.0),
        # 79 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 80 スキップ はい
        lambda: click_at(228, 816, 5.0),
        # 81 移動 戦闘完了まで
        lambda: swipe_drag(duration=6.0, wait_sec=20.0),
        # 82 スキル選択
        lambda: click_at(222, 700, 0.5),
        # 83 移動-工夫
        lambda: swipe_drag(x2=226 ,duration=10.0, wait_sec=7.0),
        # 84 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 85 スキップ はい
        lambda: click_at(228, 816, 5.0),
        # 86 必殺技
        lambda: click_at(228, 816, 5.0),
        # 87 スキップ選択
        lambda: click_at(270, 1002, 1.0),
        # 88 スキップ はい
        lambda: click_at(228, 816, 5.0),
        # 89 完了
        lambda: print('完了しました'),
    ]

def main():
    # 実行したいインデックス番号のリスト（例: [12, 15, 20]）。Noneならstart引数で従来通り
    INDEXES = None # 例: [12, 15, 20]

    # コマンドライン引数で開始インデックス指定（デフォルト0）
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    actions = scenario()

    # 0,1は必ず実行（ウィンドウアクティブ化）
    print(f"[Step 0] 実行中...（ウィンドウアクティブ化 print）")
    actions[0]()
    print(f"[Step 1] 実行中...（ウィンドウアクティブ化 click）")
    actions[1]()

    # 2以降はINDEXESがあればそのみ、なければ従来通りstart以降
    if INDEXES is not None:
        for i in INDEXES:
            print(f"[Step {i}] 実行中...（INDEXES指定）")
            actions[i]()
    else:
        for i, action in enumerate(actions[max(2, start):], start=max(2, start)):
            print(f"[Step {i}] 実行中...")
            action()

if __name__ == "__main__":
    main()
