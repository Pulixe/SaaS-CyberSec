# Sistema de Autenticación de Usuarios 2FA con Flask-RESTful 🔐🐍

Este proyecto implementa un sistema de autenticación de usuarios con **2FA** (autenticación de dos factores) utilizando el framework **Flask-RESTful**. El sistema genera un código válido por 5 minutos para mejorar la seguridad en el proceso de inicio de sesión. También se ha utilizado **Docker** para crear una imagen lista para el despliegue en servidores web, utilizando una imagen de **Red Hat** para mayor seguridad.

## Aprendizajes y Retos 📚

A través de este proyecto, adquirí habilidades en varias áreas clave:
- **Flask-RESTful**: Aprendí a construir APIs RESTful utilizando Flask y la extensión Flask-RESTful.
- **Autenticación 2FA**: Implementación de un sistema de autenticación de dos factores que mejora la seguridad del acceso de los usuarios.
- **Generación de Códigos Temporales**: Utilización de bibliotecas para generar códigos de autenticación con un tiempo de validez de 5 minutos.
- **Docker**: Creación de una imagen de Docker para facilitar el despliegue del servicio en servidores web, usando una imagen base de Red Hat para asegurar un entorno confiable.

## Tecnologías y Herramientas Utilizadas 🚀

- **Python**: Lenguaje de programación utilizado para desarrollar la aplicación.
- **Flask**: Framework utilizado para construir la API.
- **Flask-RESTful**: Extensión de Flask que simplifica la creación de APIs RESTful.
- **PyOTP**: Biblioteca utilizada para generar códigos de autenticación temporales.
- **Docker**: Herramienta utilizada para crear y gestionar contenedores, facilitando el despliegue.
- **Red Hat**: Imagen base utilizada para el contenedor, proporcionando un entorno seguro y confiable.

## Instalación y Ejecución 🚀


1. Construye la imagen de Docker:

    ```bash
    docker build -t flask-2fa-auth .

2. Ejecuta el contenedor de Docker:
    ```bash
   docker run -p 5000:5000 flask-2fa-auth
