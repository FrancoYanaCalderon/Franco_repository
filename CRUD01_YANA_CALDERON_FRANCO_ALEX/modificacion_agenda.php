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
	<form action="modificacion_agenda2.php" method="POST">
	<h2>Modificar agendacion</h2><br>
        Id_agendacion:<input type="text" name="idag"><br>
		Fecha:<input type="date" name="fec"><br>
		Hora:<input type="time" name="hor"><br>
		Actividad:<input type="text" name="act"><br>
		Completado:<input type="text" name="comp"><br>
	<input type="submit" value="modificar">
	</form>
	</center>
</body>
</html>