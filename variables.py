import requests
import json
token = 'OTg4NzBhNjItZmZhYy00MzFhLTk0ODItMGZmY2M5YWFiZjk1ZDgwMmI3M2EtNmEy_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
urlteams = 'https://api.ciscospark.com/v1/messages'
Line_spacing=""
tipomensaje = input("Ingresa el formato de mensaje (xml/yaml) : ")
nombrearchivo = str(tipomensaje) + ".txt"
result_list = ['<personaje>']
toPersonEmail = input("Ingresa correo para mensaje : ")