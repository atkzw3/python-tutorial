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
print(word[1])
# y
print(word[-1])
# n
print(word[-2])
# o
print(word[0:4])
# pyth

a = word[2:]
print(a)
# thon

# 文字列のスライス
b = 'j' + word[1:]
print(b)
# jython

# 文字列の長さ
n = len(word)
print(n)
# 6

# 文字列のメソッド
s = 'My name is Mike. Hi Mike.'
print(s)
# My name is Mike. Hi Mike.

# 文字列の置換
print(s.replace('Mike', 'Nancy'))
# My name is Nancy. Hi Nancy.

# 文字列の検索
is_start = s.startswith('My')
print(is_start)
# True

is_start = s.startswith('X')
print(is_start)
# False

# 前からの順番を返す
print(s.find('Mike'))
# 11

# 後ろからの順番を返す
print(s.rfind('Mike'))
# 20

# 文字列のカウント
print(s.count('Mike'))
# 2

# 最初の文字を大文字にし、残りの文字を小文字に変換
print(s.capitalize())
# My name is mike. hi mike.

# 文字列内の各単語の最初の文字を大文字に変換し、残りの文字を小文字に変換
print(s.title())
# My Name Is Mike. Hi Mike.

# 全て大文字に変換
print(s.upper())
# MY NAME IS MIKE. HI MIKE.

# 全て小文字に変換
print(s.lower())
# my name is mike. hi mike.

# formatメソッド
print('a is {}'.format('a'))
# a is a

print('a is {} {} {}'.format(1, 2, 3))
# a is 1 2 3

print('a is {0} {1} {2}'.format(1, 2, 3))
# a is 1 2 3

print('a is {2} {0} {1}'.format(1, 2, 3))
# a is 3 1 2

# 変数で指定することも可能
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='Taro', family='Yamada'))
# My name is Taro Yamada. Watashi ha Yamada Taro

# str()関数
a = 1
b = str(a)
print(type(b))
# <class 'str'>

# f-string python3.6~ で使用可能
# .format()よりも簡単に書ける
name = 'Taro'
family = 'Yamada'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
# My name is Taro Yamada. Watashi ha Yamada Taro

# 文字列の分割
s = 'My name is Mike.'
print(s.split(' '))
# ['My', 'name', 'is', 'Mike.']

# 文字列の結合
print(' '.join(['My', 'name', 'is', 'Mike.']))
# My name is Mike.
