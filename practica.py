#muestra la descripción de todos los productos por consola.No de uno solo
#archivo xml de referencia en el siguiente enlace
#https://gist.github.com/Fhernd/6f2aa7527a682f76c165b91fe0e989ee

#Al café negro le añadimos el precio 9.95

from bs4 import BeautifulSoup
with open('CatalogoProductos.xml','r') as f:
    data=f.read()

Bs_data=BeautifulSoup(data,'xml')
Descripcion=Bs_data.find_all('Descripcion')
print(Descripcion)

for tag in Bs_data.find_all('Producto', {'ID':"100001"}):
    tag['Precio'] = "9.95"

print(Bs_data.prettify())