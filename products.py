#二維清單
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