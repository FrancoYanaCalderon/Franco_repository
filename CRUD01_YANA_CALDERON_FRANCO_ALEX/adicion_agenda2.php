<?php
	include("conecte.php");
	echo $idag=$_POST['idag'];
	echo $fec=$_POST['fec'];
	echo $hor=$_POST['hor'];
	echo $act=$_POST['act'];
	echo $comp=$_POST['comp'];
	$re="INSERT INTO agendacion(idagendacion, fecha, hora, actividad, completado) VALUES ('".$idag."','".$fec."','".$hor."','".$act."','".$comp."')";
	$re=mysqli_query($conexion,$re);