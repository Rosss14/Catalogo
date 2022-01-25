CREATE DATABASE `Catalogo` /*!40100 DEFAULT CHARACTER SET latin1 */;

use Catalogo;

CREATE TABLE `profesional` (
  `profesionalId` int(11) NOT NULL,
  `Usuario` varchar(20) NOT NULL,
  `Clave` varchar(15) NOT NULL,
  `Especialidad` varchar(30) DEFAULT NULL,
  `Correo` varchar(40) DEFAULT NULL,
  `Licencia` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`profesionalId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `laboratorio` (
  `LabortorioId` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `Especialidad` varchar(50) DEFAULT NULL,
  `fecha_fundacion` datetime DEFAULT NULL,
  `profesional` int(11) DEFAULT NULL,
  PRIMARY KEY (`LabortorioId`),
  KEY `profesinalFK_idx` (`profesional`),
  CONSTRAINT `profesinalFK` FOREIGN KEY (`profesional`) REFERENCES `profesional` (`profesionalId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `medicamento` (
  `MedicamentoId` int(11) NOT NULL AUTO_INCREMENT,
  `grupoTerapeutico` varchar(30) NOT NULL,
  `dosisDiaria` varchar(255) DEFAULT NULL,
  `efectosSecundarios` varchar(255) DEFAULT NULL,
  `laboratorio` int(11) DEFAULT NULL,
  `profesional` int(11) DEFAULT NULL,
  PRIMARY KEY (`MedicamentoId`),
  KEY `laboratorioFK_idx` (`laboratorio`),
  KEY `profesionalFK_idx` (`profesional`),
  CONSTRAINT `laboratorioFK` FOREIGN KEY (`laboratorio`) REFERENCES `laboratorio` (`LabortorioId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `profesionalFK` FOREIGN KEY (`profesional`) REFERENCES `profesional` (`profesionalId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `componente` (
  `PrincipioActivo` tinyint(1) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `componente_medicamento` (
  `componenteId` int(11) NOT NULL,
  `medicamentoId` int(11) NOT NULL,
  KEY `medicamentoId_idx` (`medicamentoId`),
  KEY `componenteFK_idx` (`componenteId`),
  CONSTRAINT `componenteFK` FOREIGN KEY (`componenteId`) REFERENCES `componente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `medicamentoFK` FOREIGN KEY (`medicamentoId`) REFERENCES `medicamento` (`MedicamentoId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;








