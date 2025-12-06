SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `persona` (
    `idpersona` int PRIMARY KEY,
    `nombre` varchar(60) NOT NULL,
    `apellido_paterno` varchar(60) NOT NULL,
    `apellido_materno` varchar(60) NOT NULL,
    `fecha_nacimiento` varchar(60) NOT NULL 
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `agendacion`(
    `idagendacion` int PRIMARY KEY,
    `fecha` date NOT NULL,
    `hora` time NOT NULL,
    `actividad` varchar(200) NOT NULL,
    `completado` varchar(10) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;