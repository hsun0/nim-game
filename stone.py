import random
from terminal_ui import show_rules, select_difficulty

class Stone:
    def __init__(self, n, difficulty):
        self.max_num = n
        self.current_num = n
        self.round = 0 # Current round number
        self.turn = "player" # 'computer' for computer's turn, 'player' for player's turn
        self.difficulty = difficulty # 'easy', 'medium', or 'hard'
    
    def is_end(self):
        if self.current_num == 0:
            return True
        return False
    
    def next_turn(self):
        self.turn = "computer" if self.turn == "player" else "player"

    def translate(self, x):
        if x == "player":
            return "玩家"
        else:
            return "電腦"
    
    def print_status(self):
        print(f"輪次: {self.round}, 剩餘石頭數量: {self.current_num}, 輪到: {self.translate(self.turn)}")
        print("●" * self.current_num)
        print()
    
    def run(self):
        while not self.is_end():
            if self.turn == "player":
                self.round += 1
                self.print_status()

                player_take = int(input(f"你要拿幾顆石頭？(1~3): "))
                if player_take < 1 or player_take > 3:
                    print("請輸入1到3之間的數字。")
                    continue
                if player_take > self.current_num:
                    print(f"不能拿超過剩餘的石頭數量 ({self.current_num})。")
                    continue

                self.current_num -= player_take


                self.print_status()
            else:
                self.print_status()
                
                if self.difficulty == "easy": # Computer plays optimally only if there are 3 or fewer stones left
                    if self.current_num <= 3:
                        self.current_num = 0
                    else:
                        self.current_num -= random.randint(1, 3)

                elif self.difficulty == "medium": # Computer plays optimally only if there are 6 or fewer stones left
                    if self.current_num <= 6:
                        if self.current_num % 4 == 0:
                            computer_take = random.randint(1, 2)
                        else:
                            computer_take = self.current_num % 4
                    else:
                        computer_take = random.randint(1, 3)

                    self.current_num -= computer_take

                else:
                    # Hard mode: Computer plays optimally
                    if self.current_num % 4 == 0:
                        computer_take = 1
                    else:
                        computer_take = self.current_num % 4

                    self.current_num -= computer_take

                self.print_status()

            # Update the round and switch turns
            self.next_turn()

        # Game over
        self.next_turn()
        print(f"遊戲結束！{self.translate(self.turn)}獲勝！")

def main():
    show_rules()
    n = int(input("請輸入石頭的初始數量: "))
    difficulty = select_difficulty()
    
    if difficulty is None:
        print("已取消遊戲。")
        return
    
    game = Stone(n, difficulty)
    game.run()

if __name__ == "__main__":
    main()
