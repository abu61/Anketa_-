a = input('Как вас зовут? ') 
b = int(input('Сколько вам лет? ')) 
print('Здравствуйте,',a,'.Ваш возраст',b) 
c = int(input('Ваш любимый цвет? ' '1 - красный ' ' 2 - зеленый ' ' 3 - синий ' )) 
print(c) 
d = int(input('Ваша любимая музыка? ' '1 - классика ' ' 2 - поп-музыка ' ' 3 - рок ' )) 
print(d) 
v = int(input('Ваше любимое время года? ' '1 - осень ' ' 2 - зима ' ' 3 - весна ' ' 4 - лето ')) 
print(v) 
h = int(input('Ваша любимая марка авто? ' '1 - BMW ' ' 2 - АвтоВАЗ ' ' 3 - Мерседес ' )) 
print(h) 
j = int(input('Ваш любимый напиток? ' '1 - кола ' ' 2 - сок ' ' 3 - чай ' )) 
print(j) 
s = int(input('Ваша любимая погода? ' '1 - Солнечная ' ' 2 - Дождливая ' ' 3 - Средняя ' )) 
print(s) 
l = int(input('Ваша любимая ОП ? ' '1 - macOS ' ' 2 - Windows ' ' 3 - Linux ' )) 
print(l)  
f = int(input('Ваш любимый магазин? ' '1 - пятерочка ' ' 2 - Дикси' ' 3 - магнит ' )) 
print(f) 
if c == 2 or c == 1 and d == 1 or 2 and v == 2 or v == 4: 
    print('Мы с вами подружимся') 
elif c == 2 or c == 1 and d == 1 or 2 and v == 2 or v == 4 and h == 1 or h == 2 and j != 1 or j == 3 and s != 2 or s == 3 and l != 1 or l == 2 and f != 1 or f == 2:
    print('Мы может быть подружимся')
else: 
    print('Мы с вами не подружимся')
