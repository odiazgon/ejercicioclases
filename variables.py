import requests
import json
token = 'insert_token'
urlteams = 'https://api.ciscospark.com/v1/messages'
Line_spacing=""
tipomensaje = input("Ingresa el formato de mensaje (xml/yaml) : ")
nombrearchivo = str(tipomensaje) + ".txt"
result_list = ['<personaje>']
toPersonEmail = input("Ingresa correo para mensaje : ")