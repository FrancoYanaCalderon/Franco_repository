<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Adicionar Persona</title>
	<link rel = "stylesheet" href="stylesagen.css">
</head>
<body>
	<center>
	<form action="adicion_persona2.php" method="post">
		<h2>Adicionar Persona</h2><br>
		Id_persona:<input type="text" name="idper"><br>
		Nombre:<input type="text" name="nom"><br>
		Apellido Paterno:<input type="text" name="apat"><br>
		Apellido Materno:<input type="text" name="amat"><br>
		Fecha Nacimiento:<input type="date" name="fenac"><br>
		<input type="submit" value="adicionar">
	</form>
	</center>
</body>
</html>