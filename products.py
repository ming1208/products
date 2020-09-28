import os
#讀取檔案
products = []
if os.path.isfile('products.csv') :
    print('檔案找到了, 水啦!')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '品名, 價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
else:
	print('檔案找不到,Q~Q!')
#讓使用者輸入產品與價錢
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	price = input('請輸入產品價錢: ')
	price = int(price)
	products.append([name,price])
print(products)
print('------------------------------------')
#列印產品購買紀錄
for p in products:
	print(p[0], '的價格為',p[1])
#寫入csv檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('品名, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')