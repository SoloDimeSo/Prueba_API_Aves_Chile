import requests
from string import Template 

html_template = Template('''
                         <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves Chile</title>
</head>
<body>

$body


</body>
</html>
                         ''')

elem_template = Template('''<h2>Nombre : <p>$nombre_ave_espanol</p></h2>
                            <h2>Nombre : <p>$nombre_ave_ingles>/p></h2>
                            <img src="$url">
                         ''')



def request_get(url):
    return requests.get(url).json()

def build_html(url):
    response = request_get(url)[10:20]
    texto =''
    
    print(response)
    
    for ave in response:
        nombre = ave["name"]["spanish"]
        nombre_ingles = ave["name"]["english"]
        imagen_url= ave["images"]["full"]
        print("imagen_url")
        texto += elem_template.substitute(nombre_ave_espanol=nombre, nombre_ave_ingles = nombre_ingles, url = imagen_url)
        
    return html_template.substitute(body=texto)
    
    
    
    
html = build_html('https://aves.ninjas.cl/api/birds')
with open('aves_chile.html','w') as f:
    f.write(html)