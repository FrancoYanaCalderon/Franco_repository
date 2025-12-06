<?php
	include("conecte.php");
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Reporte</title>
	<link rel = "stylesheet" href="stylesagen.css">
</head>
<body>
	<center>
		<h2>Reporte de Personas</h2>
		<table border="2">
			<tr>
				<td>id</td>
				<td>nombre</td>
				<td>paterno</td>
				<td>materno</td>
				<td>Fecha nac</td>
			</tr>
			<?php
			$ls="select *from persona";
			$ls=mysqli_query($conexion,$ls);	
			while($r=mysqli_fetch_array($ls))
			{
			?>
			<tr>
				<td><?php echo $r[0];?></td>
				<td><?php echo $r[1];?></td>
				<td><?php echo $r[2];?></td>
				<td><?php echo $r[3];?></td>
				<td><?php echo $r[4];?></td>
			</tr>
			<?php
			}	
			?>

		</table>
	</center>
</body>
</html>