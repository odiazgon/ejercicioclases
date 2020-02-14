from requests_toolbelt import MultipartEncoder
from variables import *
def mandarmensaje():
    filetype = str(tipomensaje) + "/txt"
    #roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vNWQzYTUwODAtMjA0MC0xMWVhLTgyZWUtOTFjNzhjNTk1NDJl'
    my_fields = {'toPersonEmail': toPersonEmail,
                'text': str(nombrearchivo),
                'files': (str(nombrearchivo), open(nombrearchivo, 'rb'), filetype)}
    m = MultipartEncoder(fields=my_fields)
    r = requests.post(urlteams, data=m,
                      headers={'Content-Type': m.content_type,
                              'Authorization': 'Bearer ' + token})