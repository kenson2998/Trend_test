# 鑑於A = 5且B = 3，您的函數可能返回aabaabab。 請注意，abaabbaa也是一個正確的答案。 您的函數可能會返回任何正確答案。
# 寫一個函數解決方案，給定兩個整數A和B，返回一個包含完全A字母和B字母的字符串，沒有三個連續的字母是相同的（換句話說，返回的字符串中既不會出現aaa也不會出現）。
def elements_list(a, b, x):
    strings = ''
    strs = ['a' * a, 'b' * b]
    if x == 1:
        strs = ['b' * b, 'a' * a]
    return strings, strs


def solution(A, B):
    total = A + B
    times = 0
    checks = ''
    x = random.randint(0, 1)
    strings, strs = elements_list(A, B, x)
    while True:
        give_time = random.randint(1, 2)
        if times == 0:
            strings += strs[0][:give_time]
            strs[0] = strs[0][:-give_time]
            times = 1
        else:
            strings += strs[1][:give_time]
            strs[1] = strs[1][:-give_time]
            times = 0

        if strs == ['', '']:
            return strings
        if strings.endswith('aaa') or strings.endswith('bbb'):
            strings, strs = elements_list(A, B, x)

        if len(strs[0]) == 0 and len(strs[1]) > 2:
            strings, strs = elements_list(A, B, x)
        if len(strs[1]) == 0 and len(strs[0]) > 2:
            strings, strs = elements_list(A, B, x)
        checks = strings


import random

print(len(min(['aaaaa', 'bbb'])))
print(solution(6, 3))
