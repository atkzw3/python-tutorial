# 変数宣言

num = 1
name = 'Mike'
is_ok = True

print(num)
print(name)
print(is_ok)

# type関数で型を確認
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 型変換
strNum = "1"
new_num = int(strNum)
print(new_num, type(new_num))
# 型変換できない場合はエラーになる
# new_num = int("Mike")
# print(new_num, type(new_num))
# ValueError: invalid literal for int() with base 10: 'Mike'

# 変数の型付け
# ver.3.6以降
num: int = 1
name: str = 'Mike'
is_ok: bool = True

# 変数のアンパック
num1, num2 = 1, 2
print(num1, num2)

# 変数の入れ替え
num1, num2 = num2, num1
print(num1, num2)

# 変数の最初に数字は使えない
# 1num = 1

