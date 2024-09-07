# Project Title

Project created to manage employee registration and inventory control.

# Project Name

enterprise_sidebar

## Description

This project was developed using Django, a Python web framework that facilitates the creation of robust and scalable applications. The main objective of this project is to manage employee registrations and inventory, providing the company with an efficient and organized system to track employee information and manage stock categories, prices, and quantities.

## Objective

The goal of the project is to streamline the management of employee data and inventory, allowing the company to maintain an up-to-date and accessible record of both employees and stock items.

## History

This project emerged from the need to create an internal system for the company, ensuring efficient management of both human resources and inventory.


## Technologies Used

This project was built using the following technologies:

- **[Python 11](https://www.python.org/)**: Programming language used for the backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Python web framework that facilitates rapid and secure web application development.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML/HTML5)**: Structure of the user interface.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Styling of the user interface.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: CSS framework for responsive design and UI components.
- **[MDBootstrap](https://mdbootstrap.com/)**: Material Design for Bootstrap, adding additional UI components and design patterns.
- **[Git](https://git-scm.com/)**: Version control for source code management.
- **[SQLite Database](https://www.sqlite.org/)**: Data storage for the project.


# Company and Products Project

This project aims to put into practice some knowledge in Django, such as using an API to auto-complete the addresses of employees registered in the system, as well as the idea of creating a dashboard to display IT indicators.

# Screen


| Enterprise                                                                                     
|----------------------------------------------------------------------------------------------------|
| ![2024-08-2711-24-58-ezgif com-crop](https://github.com/user-attachments/assets/2dc6cdb7-47a8-4b12-86df-57ed290bc287) |


## Link

<a href="https://youtu.be/XmIuXdTQrJg" target="_blank">Video the project (Youtube)</a>


## How to run the project

### Clone the project

```bash
git clone https://github.com/kemuelkesley/empresa_sidebar.git
```

### Open the terminal in VSCode or PowerShell and run these commands

- Create a virtual environment:
  ```bash
  virtualenv env 
  ```
  or 
  ```bash
  python -m venv env
  ```

- Activating the environment on Windows:
  ```bash
  env\Scripts\ctivate
  ```

- Activating the environment on Linux:
  ```bash
  source env/bin/activate
  ```

- Install the required libraries from requirements.txt:
  ```bash
  pip install -r requirements.txt
  ```

- Apply the migrations (SQLite database tables) that come with Django:
  ```bash
  python manage.py migrate
  ```

- Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```

- After creating a user, run the server:
  ```bash
  python manage.py runserver
  ```

The server will run on:
  ```bash
  http://127.0.0.1:8000/
  ```

### Access the admin area

  ```bash
  http://127.0.0.1/admin
  ```

## Creating Gender and Roles for Company Employees

- In the admin area, go to "Gender" and create entries.
- Do the same for "Professions."
- After registering, go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Register an Employee, create categories, products, etc.

