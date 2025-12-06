<?PHP
	include("conecte.php");
	$m="UPDATE persona SET nombre ='".$_POST['nom']."',paterno='".$_POST['apat']."',materno='".$_POST['amat']."',fecha_nacimiento='".$_POST['fenac']."' WHERE idpersona ='".$_POST['idper']."'";
	$m=mysqli_query($conexion,$m);
    echo "persona modificada";
?>