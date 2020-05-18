#ハングマン定義
import random
def hangman(word):
        wrong = 0
        stages = ["",
                "________        ",
                "|               ",
                "|        |      ",
                "|        0      ",
                "|       /|\     ",
                "|       / \     ",
                "|               "
                ]
        rletters = list(word)
        board = ["_"] * len(word)
        win = False
        print("hangmanへようこそ")
        while wrong < len(stages) - 1:
                print("\n")
                msg = "1文字を予想してね"
                char = input(msg)
                if char in rletters:
                        cind = rletters.index(char)
                        board[cind] = char
                        rletters[cind] ='$'
                else:
                        wrong += 1
                print(" ".join(board))
                e = wrong+1
                print("\n".join(stages[0:e]))
#勝ち
                if "_" not in board:
                        print("あなたの勝ち!")
                        print(" ".join(board))
                        win = True
                        break
#負け
        if not win:
                print("\n".join(stages[0:wrong+1]))
                print("あなたの負け!正解は{}.".format(word))
#答えランダム設定               
word_list = ['fire', 'water', 'tree']
ans = random.choice(word_list)
#実行
hangman(ans)
