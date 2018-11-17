# -*- coding: utf-8 -*-
import unittest, json, requests
import os
from requests import *



url = 'https://proyecto-tpv.herokuapp.com/'

class testAPI(unittest.TestCase):
	def test_root(self):
		response = requests.get(url)
		self.assertEqual(response.status_code,200, "Código correcto")
		self.assertEqual(response.json()['status'], "OK", "Estado correcto")


	def test_getMesa(self):
		response = requests.get(url+'/getMesas')
		self.assertEqual(response.json(),auxiliar_mesas, "Mesas correctas")

	def test_cuantasMesas(self):
		response = requests.get(url+'/cuantasMesas')
		self.assertEqual(response.json()['NMesas'],len(auxiliar_mesas), len(auxiliar_mesas))
	
	def test_reponer(self):
		response = requests.get(url+'/reponer')
		self.assertEqual(response.json()['Repuesto'],True, "Repuestas")

	
	def test_apunta(self):
		response = requests.get(url + '/apuntar')
		self.assertEqual(response.json()['Error'],"Tiene que indicar la mesa al menos","Apuntando")


def setUpModule():
	global auxiliar_mesas
	global auxiliar_caja
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	MESAS = BASE_DIR+'/data/mesas.json'
	CAJA = BASE_DIR + '/data/ganancias.json'
	with open(MESAS, 'r') as f:
		auxiliar_mesas = json.loads(f.read())


if __name__ == '__main__':
	unittest.main()

