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

			# If it does, it will send you an email
			sendMail(product['name'], title, price)

def sendMail(name, title, price):
	return name, title, price
