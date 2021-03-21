a = '123'
b = 12
c = ''
s = '%s 안녕하세요 %d ' %(a, b)+' {kkk} ' .format(kkk='곰돌이')+ f' {a} 반갑습니다.'

print(type(a))
print(a*12)
print(5/2)
print(s[0:6:2])



print(s)

print(','.join(['a','s','d','f']))

t = {'a':1, 'b':2, 'c':3}

for k, v in t.items():
    print(f'key : {k}')
    print(f'value : {v}')

if c:
    print(a)
else:
    print(b)