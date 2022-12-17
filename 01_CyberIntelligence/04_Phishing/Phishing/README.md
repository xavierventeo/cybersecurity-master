# Página phishing que guarda los registros en fichero local

## Pasos

### 1.- Instalar XAMPP 
### 2.- Creación de las páginas
###     - Copiar carpeta phishing en /opt/lampp/htdocs
###     - Página simple de login
###     - Página facebook (descargar código fuente y cambiar el action del form)
###     - Página php que guarda las credenciales capturadas
###  3.- Arrancar apache / xampp
###     - Arrancar XAMPP: sudo /opt/lampp/lampp start 
###     - Iniciar página simple https://localhost/phishing
###     - Iniciar página facebook https://localhost/phishing/fa
###     - Parar XAMPP: sudo /opt/lampp/lampp stop 

# Pharming

###  Modificar fichero host para que la web de facebook vaya a loca
###  vi /etc/hosts
###  poner: 127.0.0.1     facebook.com
###  limpiar caché del navegador y refrescar
###  Si es necesario renombrar la carpeta phishing por dashboard


