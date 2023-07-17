# 文字列

# シングルクォーテーション or ダブルクォーテーションで囲む
print('hello')
# hello
print("hello")
# hello

# 文字列の中にシングルクォーテーションを含める場合
print("I can't speak English")
# I can't speak English

# 文字列の中にダブルクォーテーションを含める場合
print('I can"t speak English')
# I can"t speak English

# \でエスケープする
print('I can\'t speak English')
# I can't speak English

# ダブルクォーテーションで囲む場合
print("I can\"t speak English")
# I can"t speak English

# エスケープシーケンス
# \n 改行
print('hello \n world')
# hello
#  world 改行される

# \の後にn文字列がある場合
print('\name\name')
# ame 改行 ameと出力される

# r と先頭におけばエスケープシーケンスを無効化できる
print(r'\name\name')
# \name\name と出力される。pathなどで使える

# 複数行の文字列は"""\で囲む
print("""\
line1
line2
line3
line4\
""")
# line1 改行 line2 改行 line3 改行 line4 と出力される

# 文字列の連結
print('Hi.' * 3 + 'Mike.')
# Hi.Hi.Hi.Mike.

# 長文の場合は ()で囲む or \でまとめる
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
    'bbbbbb'
print(s)

# 文字列のインデックス
word = 'python'
print(word[0])
# p

