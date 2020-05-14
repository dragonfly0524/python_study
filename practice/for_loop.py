#while

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New year!")

#例題1
band = ["Mr.children","spitz","sugashikao","super butter dog"]

for show in band:
    print(show)

#例題2
for i in range(25,51):
    print(i)

#例題3 enumerate関数
for i, name in enumerate(band):
    print(i,name)

#例題4 問題
correct = [1,14,31,55]
while True:
    ans = input("数字を入力するか、qで終了します")
    if ans == "q":
        break
    try:
        ans = int(ans)
    except ValueError:
        print("数字を入力するか、qで終了します")
    if ans in correct: 
        print("正解")
    else:
        print("不正解")
#例題5 入れ子のループ
list1 = [8,19,148,4]
list2 = [9,1,33,83]
added =[]
for i in list1:
    for j in list2:
        added.append(i * j)
print(added)
