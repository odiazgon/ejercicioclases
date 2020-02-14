from personajesub import *
class personaje:
    def __init__(self,numPersonaje): # para recibir el numero de personaje que vamos a llamar
        self.url= "https://swapi.co/api/people/"
        self.numPersonaje=numPersonaje
        url = "https://swapi.co/api/people/" + str(self.numPersonaje)
        response = requests.request("GET", url)
        print(response.text)
        jsonDiccionario = json.loads(response.text)
        if tipomensaje == "yaml":result_list = ['--- ! personaje starwars\n']
        for tag_name in jsonDiccionario:
            sub_obj = jsonDiccionario[tag_name]
            if tipomensaje == "xml":
                result_list.append("\t<" + str(tag_name) + ">" + str(sub_obj) + "</" + str(tag_name) + ">\n")
                result_list2="".join(result_list)
            if tipomensaje == "yaml":
                result_list.append(tag_name + ": " + str(sub_obj) + "\n")
                result_list2="".join(result_list)
        with open(nombrearchivo, "w") as output:
            output.write(str(result_list2))
    mandarmensaje()