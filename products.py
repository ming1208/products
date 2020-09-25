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
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0]+ ','+ str(p[1])+'\n')