##class personaje

##def	obtenerinfo()
import requests
import json

class personaje:

	def obtenerinfo():
		url = "https://swapi.co/api/people/1"

		payload = {}
		headers = {}

		response = requests.request("GET", url, headers=headers, data = payload)
		jsonDiccionario = json.loads(response.text)
		print(jsonDiccionario)


	obtenerinfo()