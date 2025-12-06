<?php
	include("conecte.php");
	$el="DELETE FROM agendacion WHERE idagendacion='".$_POST['idag']."'";
	$el=mysqli_query($conexion,$el);
    echo "agendacion eliminada";
?>