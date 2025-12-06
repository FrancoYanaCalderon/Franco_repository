<?php
	include("conecte.php");
	$el="DELETE FROM persona WHERE idpersona='".$_POST['idper']."'";
	$el=mysqli_query($conexion,$el);
    echo "persona eliminada";
?>