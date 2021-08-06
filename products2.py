import os #operating system

#讀取檔案
def read_file(filename): 
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue    #跳到下一個迴
			name, price = line.strip().split(',') 
			#strip()先把\n去掉，再利用,作為分割的字元，並且分別存入name與price
			products.append([name, price])
	return products #回傳products清單
		
#讓使用者輸入
def user_input(products):
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
	return products

#二維清單存取方法，例如： products[0][0]
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: #r：讀取 w:寫入 #加入編碼格式
		f.write('商品,價格\n') #寫入欄位名稱 
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在電腦中
		print('Good!')
		products = read_file(filename)
	else:
		print('Cannot fine the file!')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()



