# Image Gallery Application

![image](https://github.com/WilerMS/gallery-app/assets/70902862/5ec948c0-56a9-4217-b352-1bbead58fb4c)


[![Svelte](https://img.shields.io/badge/Frontend-Svelte-blueviolet)](https://svelte.dev/)
[![TypeScript](https://img.shields.io/badge/Frontend-TypeScript-blue)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Frontend-Tailwind_CSS-38B2AC)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Backend-Python-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-4DB33D)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Containerization-Docker-2496ED)](https://www.docker.com/)

This repository contains a full-stack image gallery application. The frontend is built using Svelte with TypeScript and Tailwind CSS. The backend is developed in Python with Flask. The application uses MongoDB as the database and is containerized with Docker using Docker Compose.

## Features

- Add and remove images by providing a description and image link
- Search functionality
- Ability to delete an image by entering a unique password known only to admins

## Prerequisites

Before running the application, ensure that you have the following installed:

- [Docker](https://www.docker.com/get-started)

## Getting Started

Follow the steps below to launch the application:

1. Clone this repository:

   ```bash
   git clone https://github.com/WilerMS/gallery-app.git
   ```

2. Navigate to the project's directory:

   ```bash
   cd gallery-app
   ```

3. Set the required environment variables. Edit the `.env` file and replace the placeholders with your own values:

   ```plaintext
   ADMIN_PASSWORD=your-unique-admin-password
   ```

4. Build and run the Docker container:

   ```bash
   docker-compose up -d
   ```

5. Once the container is running, you can access the application by opening a web browser and visiting:

   ```plaintext
   http://localhost:5173
   ```
