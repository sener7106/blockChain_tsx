# 問題　00000 - 0000 = 33333
# となるように、１から９までの数字を一回ずつ用いた数字の組み合わせを求めよ。
from itertools import *
# 順列を使うために必要なパイソンパッケージ

ans = 33333
x = [1, 2, 3, 5, 6, 7, 8, 9]

ls = []
count = 0
# ｘは1～9までをセーブするリスト、ｌｓは解答のリスト、countは正解が出た回数
printList = list(permutations(x, 8))
#　まず、変数にpermutations関数を利用し、１～９までの組み合わせをした順列をセーブする　（実行してみると確認可能）
# まず０００００の一番最初のAの部分は４出ないと３３３３３の解答がでないため、４に設定する。
# tupleでセーブされてづるデータをforを利用して、一個ずつ確認する。
for i in printList:
    # 各 iには組み合わせに値する数字が記録されていて、list comprehension (リスト参照)で各数字をnumber, number2にそれぞれ４ｘｘｘｘ(number)－ｘｘｘｘ(number2)としてセーブする

    print(i[0:4], i[4:8])

    number = 40000 + (i[0] * 1000) + (i[1] * 100) + (i[2] * 10) + i[3]
    number2 = (i[4] * 1000) + (i[5] * 100) + (i[6] * 10) + i[7]

    # もし０００００－００００の結果が正解だった場合、出力してカウント変数を一個増やす。ではなかった場合は無視して続ける
    if(number - number2 == ans):
        ls.append(str(number) + "-" + str(number2))
        count += 1
    else:
        continue

print(ls, count)
