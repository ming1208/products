products =[]
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	price = input('請輸入產品價錢: ')
	products.append([name,price])
print('------------------------------------')
print(products)
