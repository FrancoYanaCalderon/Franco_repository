<?php
	include("conecte.php");
	echo $idper=$_POST['idper'];
	echo $nom=$_POST['nom'];
	echo $apat=$_POST['apat'];
	echo $amat=$_POST['amat'];
	echo $fenac=$_POST['fenac'];
	$re="INSERT INTO persona(idpersona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento) VALUES ('".$idper."','".$nom."','".$apat."','".$amat."','".$fenac."')";
	$re=mysqli_query($conexion,$re);

?>