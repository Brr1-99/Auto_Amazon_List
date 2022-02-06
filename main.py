import requests
from bs4 import BeautifulSoup
import smtplib
from interface import WISH_LIST

# Headers to avoid bot protection
headers=({
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
	'Accept-Language': 'en-US, en;q=0.5'
})

def checkPrice():

	data = []

	# Looping through all your wished products
	for product in WISH_LIST:
		
		#Fetch amazon link
		page = requests.get(product['url'], headers=headers)

		soup = BeautifulSoup(page.content, 'html.parser')

		#Fecth for the title of the product
		title = soup.find('span', id='productTitle').get_text().strip()

		#Fetch for its current price
		price = float(soup.find('span', class_='a-offscreen').get_text().strip()[:-1].replace(',','.'))


		#Checking if it suits your budget  
		if price < product['price']:
			product['price'] = price
			data.append(product)
	
	if len(data) > 0 :
	   sendMail(data)

def sendMail(products):

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('your@gmail.com', 'password')

	subject = 'Some of your items have reached your price!'

	body = 'Check the prices on this products: \n\n'

	for product in products:
		url = product['url']
		name = product['name']
		price = product['price']
		body+= f'"{name}" ahora cuesta {price} €. Haz click en el link para comprarlo.{url}\n'

	msg = f'Subject: {subject} \n\n {body}'

	server.sendmail('your@gmail.com','your@gmail.com', msg.encode('utf-8').strip() )

	print('Email Sent!')

	server.quit()

checkPrice()



