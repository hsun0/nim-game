import questionary


def show_rules():
    print("\n=== 石頭遊戲 ===")
    print("玩家先手，與電腦輪流拿石頭。")
    print("每次可拿 1～3 顆，不能超過剩餘數量。")
    print("拿走最後一顆石頭的人獲勝！\n")


def select_difficulty(medium_value="medium"):
    return questionary.select(
        "請選擇難度：",
        choices=[
            questionary.Choice("簡單", value="easy"),
            questionary.Choice("中等", value=medium_value),
            questionary.Choice("困難", value="hard"),
        ],
        instruction="（使用 ↑↓ 選擇，按 Enter 確認）",
    ).ask()
