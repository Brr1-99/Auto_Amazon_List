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

WISH_LIST.append(product(name='Teclado Mecánico', 
	url='https://www.amazon.es/MARSGAMING-MK5BRES-Teclado-Mec%C3%A1nico-Espa%C3%B1ol/dp/B08BWK1RGL/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2L30FF0DRH6PU&keywords=teclado+mecanico&qid=1644144266&sprefix=teclado+me%2Caps%2C104&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXSENENFMzNFZEV1YmZW5jcnlwdGVkSWQ9QTEwMTc2MTcxMTRFU0s0VVlMS1ZGJmVuY3J5cHRlZEFkSWQ9QTA5MTA5NTIyRFY0RlJBNDhGR1M5JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==',
	price=50))