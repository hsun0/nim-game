import pygame
import sys
import random
from terminal_ui import show_rules, select_difficulty

show_rules()
print("初始石頭數量：15 顆\n")
difficulty = select_difficulty(medium_value="normal")
if difficulty is None:
    print("已取消遊戲。")
    sys.exit()

def show_text(text, x, y, color=(255, 255, 255), font=None):#專門顯示文字的方法，除了顯示文字還能指定顯示的位置和顏色
    if font is None:
        font = FONT
    text_surface = font.render(text, True, color)
    SCREEN.blit(text_surface, (x, y))
    return text_surface

# 遊戲參數
STONES_PER_ROW = 10
STONE_RADIUS = 15
STONE_MARGIN = 10

# 初始化 Pygame
pygame.init()

# 視窗設定
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("石頭遊戲")

# 字型設定
FONT = pygame.font.Font("edukai-5.0.ttf", 24)#本文主角
BTN_FONT = pygame.font.Font("edukai-5.0.ttf", 24)#按鈕字型

# 按鈕設定
BUTTONS = []
for i, text in enumerate(["取1顆", "取2顆", "取3顆"]):
    btn_rect = pygame.Rect(50 + i * 150, HEIGHT - 100, 120, 50)
    BUTTONS.append((btn_rect, text))

# 繪製按鈕
def draw_buttons():
    u = 0
    for rect, text in BUTTONS:
        pygame.draw.rect(SCREEN, (200, 200, 200), rect)
        # 計算文字置中位置
        text_surface = BTN_FONT.render(text, True, (0, 0, 0))
        text_x = rect.centerx - text_surface.get_width() // 2
        text_y = rect.centery - text_surface.get_height() // 2
        show_text(text, text_x, text_y, (0, 0, 0), BTN_FONT)

# 繪製石頭
def draw_stones(current_num):
    for i in range(current_num):
        row = i // STONES_PER_ROW
        col = i % STONES_PER_ROW
        x = 50 + col * (STONE_RADIUS * 2 + STONE_MARGIN)
        y = 50 + row * (STONE_RADIUS * 2 + STONE_MARGIN)
        pygame.draw.circle(SCREEN, (100, 100, 255), (x, y), STONE_RADIUS)

# 更新遊戲畫面
def update_game_display(current_num, turn):
    SCREEN.fill((255, 255, 255))
    draw_stones(current_num)
    draw_buttons()
    
    # 顯示狀態文字
    status_text = f"剩餘: {current_num} 顆，回合: {'玩家' if turn=='player' else '電腦'}"
    show_text(status_text, 50, HEIGHT - 150, (0, 0, 0))
    
    # 顯示難度在右上角
    difficulty_names = {'easy': '簡單', 'normal': '中等', 'hard': '困難'}
    difficulty_text = f"難度: {difficulty_names[difficulty]}"
    # 計算文字寬度，讓它靠右對齊
    difficulty_surface = FONT.render(difficulty_text, True, (0, 0, 0))
    difficulty_x = WIDTH - difficulty_surface.get_width() - 20  # 距離右邊界20像素
    show_text(difficulty_text, difficulty_x, 20, (0, 0, 0))

# 讀取初始設定
# n = int(input("請輸入石頭初始數量: "))
n = 15  # 固定石頭數量為15顆

current_num = n
turn = "player"
running = True
game_over = False
winner = None
clock = pygame.time.Clock()

# 遊戲主迴圈
while running:
    update_game_display(current_num, turn)

    # 遊戲結束畫面
    if game_over:
        msg = f"遊戲結束！{winner}獲勝！"
        # 計算置中位置
        bold_font = pygame.font.Font("edukai-5.0.ttf", 36)
        bold_font.set_bold(True)
        temp_surface = bold_font.render(msg, True, (255, 0, 0))
        text_x = (WIDTH - temp_surface.get_width()) // 2
        text_y = (HEIGHT - temp_surface.get_height()) // 2
        show_text(msg, text_x, text_y, (255, 0, 0), bold_font)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        continue

    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == "player":
            pos = event.pos
            for rect, text in BUTTONS:
                if rect.collidepoint(pos):
                    take = int(text[1])
                    if 1 <= take <= 3 and take <= current_num:
                        current_num -= take
                        turn = "computer"
                    break
    # 更新畫面
    update_game_display(current_num, turn)

    # 檢查結束條件
    if current_num == 0 and not game_over:
        game_over = True
        winner = "玩家" if turn == "computer" else "電腦"
    
    # 電腦回合
    if turn == "computer" and not game_over:
        pygame.display.flip()
        pygame.time.delay(2000)  # 暫停一秒
        # 策略選擇
        if difficulty == "easy":
            if current_num <= 3:
                take = current_num
            else:
                take = random.randint(1, 3)
        elif difficulty == "normal":
            if current_num <= 6:
                if current_num % 4 == 0:
                    take = random.randint(1, 3)
                else:
                    take = current_num % 4
            else:
                take = random.randint(1, 3)
        else:  # hard
            if current_num % 4 == 0:
                take = random.randint(1, 3)
            else:
                take = current_num % 4
        current_num -= take
        turn = "player"

    # 檢查結束條件
    if current_num == 0 and not game_over:
        game_over = True
        winner = "玩家" if turn == "computer" else "電腦"

    pygame.display.flip()
    clock.tick(30)

# 離開遊戲
pygame.quit()
sys.exit()
