<?PHP
	include("conecte.php");
	$m="UPDATE agendacion SET fecha ='".$_POST['fec']."',hora='".$_POST['hor']."',actividad='".$_POST['act']."',completado='".$_POST['comp']."' WHERE idagendacion ='".$_POST['idag']."'";
	$m=mysqli_query($conexion,$m);
    echo "agendacion modificada";
?>