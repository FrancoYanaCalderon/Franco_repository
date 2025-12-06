<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Adicionar Agenda</title>
	<link rel = "stylesheet" href="stylesagen.css">
</head>
<body>
	<center>
	<form action="adicion_agenda2.php" method="post">
		<h2>Adicionar agendacion</h2><br>
		Id_agendacion:<input type="text" name="idag"><br>
		Fecha:<input type="date" name="fec"><br>
		Hora:<input type="time" name="hor"><br>
		Actividad:<input type="text" name="act"><br>
		Completado:<input type="text" name="comp"><br>
		<input type="submit" value="adicionar">
	</form>
	</center>
</body>
</html>