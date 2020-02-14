import json
import requests
from requests_toolbelt import MultipartEncoder
import requests

class personaje():
    def json2xml(json_obj, Line_spacing=""):
       result_list = list()
       json_obj_type = type(json_obj)
       if json_obj_type is dict:
           for tag_name in json_obj:
               sub_obj = json_obj[tag_name]
               result_list.append("%s<%s>" % (Line_spacing, tag_name))
               result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
               result_list.append("%s</%s>" % (Line_spacing, tag_name))
               # print(result_list)
               return "\n".join(result_list)
       return "%s%s" % (Line_spacing, json_obj)
    def pedirpersonajexml():
        url = "https://swapi.co/api/people/1"
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data = payload)
        jsonDiccionario = json.loads(response.text)
        #print(jsonDiccionario)
        result_list = ['<personaje>']
        Line_spacing=""
        for tag_name in jsonDiccionario:
            sub_obj = jsonDiccionario[tag_name]
            result_list.append("\t%s<%s>" % (Line_spacing, tag_name))
            result_list.append("\t" + str(sub_obj))
            result_list.append("\t%s</%s>" % (Line_spacing, tag_name))
            result_list2="\n".join(result_list)
        result_list2=result_list2 + "\n</personaje>"
        print(result_list2)
        with open("xml.txt", "w") as output:
            output.write(str(result_list2))
    pedirpersonajexml()

    def pedirpersonajeyaml():
        url = "https://swapi.co/api/people/1"
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data = payload)
        jsonDiccionario = json.loads(response.text)
        #print(jsonDiccionario)
        result_list = ['--- ! personaje starwars\n']
        Line_spacing=""
        for tag_name in jsonDiccionario:
            sub_obj = jsonDiccionario[tag_name]
            result_list.append(tag_name + ":")
            result_list.append(str(sub_obj) + "\n")
            result_list2="".join(result_list)
        print(result_list2)
        with open("yaml.txt", "w") as output:
            output.write(str(result_list2))
    pedirpersonajeyaml()

    def mandarmensaje():
        g = input("Enter the mail to send : ")
        filepath = 'xml.txt'
        filetype = 'xml/txt'
        roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vZGVhMWYxYTktMDU1NC0zNGU5LTljODQtMGIxYzk1YTRkYjg1'
        toPersonEmail = 'odiazgon@cisco.com'
        token = 'OTg4NzBhNjItZmZhYy00MzFhLTk0ODItMGZmY2M5YWFiZjk1ZDgwMmI3M2EtNmEy_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
        url = 'https://api.ciscospark.com/v1/messages'

        my_fields = {'toPersonEmail': toPersonEmail,
                    'text': 'Tarea Lista',
                    'files': ('xml.txt', open(filepath, 'rb'), filetype)}
        m = MultipartEncoder(fields=my_fields)
        r = requests.post(url, data=m,
                          headers={'Content-Type': m.content_type,
                                  'Authorization': 'Bearer ' + token})
    mandarmensaje()