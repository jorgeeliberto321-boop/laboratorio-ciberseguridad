Laboratorio de Ciberseguridad

Descripción

Aplicación desarrollada en Python con Flask y SQLite para demostrar prácticas de programación segura y detección de intentos de inicio de sesión fallidos.

Tecnologías utilizadas

- Python
- Flask
- SQLite
- Werkzeug
- Visual Studio Code

Funcionalidades

1. Registro de usuarios.
2. Inicio de sesión.
3. Validación de usuario, correo y contraseña.
4. Almacenamiento seguro de contraseñas mediante hash.
5. Consultas SQL parametrizadas.
6. Registro de eventos exitosos y fallidos.
7. Detección de tres o más intentos fallidos.
8. Simulación de respuesta ante alertas.
9. Cálculo de indicadores MTTD y MTTR.

Archivos principales

- app.py: aplicación web.
- crearDB.py: creación de base de datos.
- detector.py: detección de intentos fallidos.
- respuesta.py: simulación de respuesta.
- usuarios.db: base de datos.
- eventos.log: registro de eventos.
- respuesta.log: registro de respuestas.
- templates/: formularios HTML.

Ejecución

1. Instalar Flask:
   pip install flask
2. Ejecutar la aplicación:
   python app.py
3. Abrir en el navegador:
   http://127.0.0.1:5000

Resultados de prueba

- Usuario probado: prueba03.
- Intentos fallidos detectados: 3.
- MTTD observado: 100.59 segundos.
- MTTR de simulación: 0.00 segundos.

Seguridad implementada

Se utilizaron validaciones de entrada, contraseñas almacenadas mediante hash y consultas SQL parametrizadas.

Autor

Jorge eliberto carrillo delgado