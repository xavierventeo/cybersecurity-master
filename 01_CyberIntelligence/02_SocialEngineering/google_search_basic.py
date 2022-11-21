#python3 -m pip install googlesearch-python
#https://github.com/Nv7-GitHub/googlesearch

from googlesearch import search
busqueda="site:elladodelmal.com"
busqueda="Name+Surname1+Surname2"

for i in search(busqueda, num_results=5):
    print(i)
