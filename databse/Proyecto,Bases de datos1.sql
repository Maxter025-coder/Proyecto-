-- Crear base de datos y usarla
CREATE DATABASE gestion_recursos_humanos;
USE gestion_recursos_humanos;

-- Crear tabla departamentos
CREATE TABLE departamentos (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(150),
    presupuesto DECIMAL(12, 2)
);

-- Crear tabla puestos, con referencia a departamentos
CREATE TABLE puestos (
    id_puesto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id_departamento) ON DELETE CASCADE
);

-- Crear tabla empleados, con referencia a puestos
CREATE TABLE empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(150),
    puesto_id INT,
    salario DECIMAL(10, 2),
    FOREIGN KEY (puesto_id) REFERENCES puestos(id_puesto) ON DELETE CASCADE
);

-- Insertar datos en la tabla departamentos
INSERT INTO departamentos (nombre, ubicacion, presupuesto) 
VALUES ('Recursos Humanos', 'Edificio A', 50000.00);

-- Insertar datos en la tabla puestos, asegurando que departamento_id existe
INSERT INTO puestos (nombre, descripcion, departamento_id) 
VALUES ('Gerente de RRHH', 'Encargado de la gestión de personal', 1);

-- Insertar datos en la tabla empleados, asegurando que puesto_id existe
INSERT INTO empleados (nombre, direccion, puesto_id, salario) 
VALUES ('Carlos López', 'Calle 456', 1, 4000.00);

-- Selección de empleados con datos de sus puestos
SELECT e.nombre, e.direccion, p.nombre AS puesto, e.salario
FROM empleados e
JOIN puestos p ON e.puesto_id = p.id_puesto;

-- Actualizar salario de un empleado
UPDATE empleados
SET salario = 3500.00
WHERE id_empleado = 1;


DELETE FROM empleados
WHERE id_empleado = 1;
