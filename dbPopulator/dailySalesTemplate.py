#! /usr/bin/python3.7

import random
import sys
import datetime

DISHES = [
"Ceviche de pescado",
"Leche de tigre",
"Salchipapas",
"Aeropuerto",
"Pescado a lo macho",
"Anticuchos",
"Pollo a la brasa",
"Cuy asado",
"Arroz con mariscos",
"Causa rellena",
"Arroz chaufa",
"Lomo saltado",
"Tallarines saltados",
"Tiraditos",
"Carapulcra",
"Papa rellena",
"Ají de gallina",
"Seco de pollo",
"Chupe de camarones",
"Jalea de mariscos",
"Choros a la Chalaca",
"Rocoto relleno",
"Charquicán",
"Lechón al horno",
"Picante a la tacneña",
"Pollo en salsa de Huacatay",
"Ocopa",
"Chupe de pollo"
]

TEMPLATE_STR = """
{"productTyoe":"comida","productName":{:s},"price":{:.4f},"cost":{:.4f},"saleDate":{"$timestamp":{"t":1574649868,"i":1}}}
"""



def TimestampMillisec64(refDate):
	return int( (refDate - datetime.datetime(1970, 1, 1)).total_seconds() * 1000 ) 

def generateMenuTemplate():
	prices = [ ii for ii in range(10,31) if ii % 2 == 0 or ii % 5 == 0]
	return list(map(lambda x: list(x) + [int(x[1] * (1 - random.randrange(20,50) / 100.0))], list(zip(DISHES, [random.choice(prices) for ii in range(len(DISHES))]))))

def main():
	simulated_days = int(sys.argv[1])

	raw_date = sys.argv[2].split("-")

	year = int(raw_date[0])
	month = int(raw_date[1])
	day = int(raw_date[2])

	passed_days = 0
	currentMenu = generateMenuTemplate()
	while simulated_days > 0:
		if round(random.random(), 4 ) > 0.7:
			currentMenu = generateMenuTemplate()
		else:
			pass

		topen = datetime.datetime(year,month,day, 16, 20, 00) + datetime.timedelta(minutes=random.randint(3,20))
		tclose = datetime.datetime(year,month,day, 21, 00, 00) - datetime.timedelta(minutes=random.randint(20,50))

		daylap = int((tclose - topen).total_seconds()/60)
		for _ in range(random.randint(10, 200)):
			currentDish = random.choice(currentMenu)			
			currentTime = topen + datetime.timedelta(minutes=random.randint(0,daylap))
			currentTime = currentTime + datetime.timedelta(days=passed_days)

			TEMPLATE_STR = """{"productType":"comida","productName":\""""
			TEMPLATE_STR += str(currentDish[0]) 
			TEMPLATE_STR += """\","price":"""
			TEMPLATE_STR += str(currentDish[1])
			TEMPLATE_STR += ""","cost":"""
			TEMPLATE_STR += str(currentDish[2])
			TEMPLATE_STR += ""","saleDate":{"$date":{"$numberLong":\""""
			TEMPLATE_STR += str(TimestampMillisec64(currentTime))
			TEMPLATE_STR += """\"}}}"""

			print(TEMPLATE_STR)

		passed_days += 1
		simulated_days -= 1



	print(TEMPLATE_STR)
	 

main()
