#ハングマン定義
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
    print("ハングマンへようこそ")

#ループ処理
while wrong < len(stages) - 1:
	