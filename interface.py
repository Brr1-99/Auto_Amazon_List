# ┌────────────────────────
# │       INTERFACES
# └────────────────────────

WISH_LIST = []	

def product(name: str, url: str, price: int):
	return {
		'name': name,
		'url': url,
		'price': price
	}

WISH_LIST.append(product(name='Name of your product', 
	url='Url in Amazon',
	price='Desired price to look for'))