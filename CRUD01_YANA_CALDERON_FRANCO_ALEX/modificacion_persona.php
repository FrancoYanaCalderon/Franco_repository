<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Modificar Persona</title>
    <link rel = "stylesheet" href="stylesagen.css">
</head>
<body>
	<center>
	<form action="modificacion_persona2.php" method="POST">
	<h2>Modificar Persona</h2><br>
        Id_persona:<input type="text" name="idper"><br>
		Nombre:<input type="text" name="nom"><br>
		Apellido Paterno:<input type="text" name="apat"><br>
		APELLIDO Materno:<input type="text" name="amat"><br>
		Fecha Nacimiento:<input type="date" name="fenac"><br>
	<input type="submit" value="modificar">
	</form>
	</center>
</body>
</html>