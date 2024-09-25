import random

def roll_dice():
    """模拟投掷一个六面骰子"""
    return random.randint(1, 6)

def game(seed):
    """游戏主函数"""
    random.seed(seed)
    round_number = 1
    point = 0
    
    while True:
        print(f"\n第{round_number}轮投骰子：")
        dice1 = roll_dice()
        dice2 = roll_dice()
        sum_dice = dice1 + dice2
        print(f"你掷出了 {dice1} 和 {dice2}，和数为 {sum_dice}")

        if round_number == 1:
            if sum_dice in [7, 11]:
                print("恭喜你，第一轮就取得了胜利！")
                return "胜"
            elif sum_dice in [2, 3, 12]:
                print("很遗憾，第一轮你就输了。")
                return "负"
            else:
                point = sum_dice
                print(f"你的点数为：{point}")
        else:
            if sum_dice == point:
                print(f"恭喜你，和数等于点数，你取得了胜利！")
                return "胜"
            elif sum_dice == 7:
                print("很遗憾，你输了。")
                return "负"
        
        round_number += 1


seed = int(input("请输入一个无符号整数作为随机数种子："))
result = game(seed)
print(f"游戏结果：{result}")