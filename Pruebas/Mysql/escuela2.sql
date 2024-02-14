-- create tables
CREATE TABLE `inscripcion` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idpersona` INT(10) NOT NULL,
    `fecha` date NOT NULL,
    
    PRIMARY KEY (id)
)
CREATE TABLE `docente` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idpersona` INT(10) NOT NULL,
    
    
    PRIMARY KEY (id)
  

)

CREATE TABLE `inspector` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idpersona` INT(10) NOT NULL,
    PRIMARY KEY (id)
  

)
CREATE TABLE `persona`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` varchar(20) NOT NULL,
    `cedula` INT(10) NOT NULL,
    `apellido` varchar(20) NOT NULL,
    `sexo` varchar(1) NOT NULL,

    PRIMARY KEY (id)

)
CREATE TABLE `matricula`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idinscripcion` INT(10) NOT NULL,
    `idgradodelparalelo` INT(10) NOT NULL,
       
    PRIMARY KEY (id),
    
)
CREATE TABLE `paralelo`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` varchar(20) NOT NULL,
        
    PRIMARY KEY (id)
)

CREATE TABLE `grado`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` varchar(20) NOT NULL,
    `idinspector` INT(10) NOT NULL    
    PRIMARY KEY (id)
   
)

CREATE TABLE `gradoparalelo`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idgrado` INT(10) NOT NULL,
    `idparalelo` INT(10) NOT NULL    
    PRIMARY KEY (id),
   
)
CREATE TABLE `materia`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` varchar(20) NOT NULL,
        
    PRIMARY KEY (id)
)

CREATE TABLE `materiadocente`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `iddocente` INT(10) NOT NULL,
    `idmateria` INT(10) NOT NULL,
        
    PRIMARY KEY (id)
)
CREATE TABLE `docenteparalelo`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idmateriadocente` INT(10) NOT NULL,
    `idparalelo` INT(10) NOT NULL,
        
    PRIMARY KEY (id)
)

CREATE TABLE `materiagrado`(
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idmateria` INT(10) NOT NULL,
    `idgrado` INT(10) NOT NULL,
        
    PRIMARY KEY (id)
)