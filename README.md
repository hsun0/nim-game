# Nim Game

這是一款玩家與電腦輪流拿石頭的遊戲，提供簡單、中等與困難三種難度。

## 遊戲規則

- 玩家先手，接著與電腦輪流行動。
- 每回合可以拿走 1～3 顆石頭，但不能超過場上剩餘的數量。
- 拿走最後一顆石頭的人獲勝。

## 安裝

本專案使用 uv 管理。

```bash
uv sync
```

## 執行

```bash
uv run game.py
```

## 字體來源

遊戲使用教育部提供的[教育部隸書字形檔](https://language.moe.gov.tw/result.aspx?classify_sn=23&subclassify_sn=436&content_sn=47)。
