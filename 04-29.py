total = 0
score = int(input("score=(若輸入完畢，請入-1)"))
while score>=0:
    total = total + score
    score = int(input("score="))
print("總分是：", total)