products =[]
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	price = input('請輸入產品價錢: ')
	price = int(price)
	products.append([name,price])
print('------------------------------------')
print(products)
print('------------------------------------')
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('品名, 價格\n')
	for p in products:
		f.write(p[0]+ ','+ str(p[1])+'\n')