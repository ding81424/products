products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)
	#上面三行可以寫成：p = [name, price]
	products.append(p)
	#上面程式碼還能在濃縮寫成 products.append([name, price])
print(products)

#二維清單存取方法，例如： products[0][0]

for p in products:
	print(p[0], '的價格是', p[1])



with open('products.csv', 'w') as f: #r：讀取 w:寫入
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


