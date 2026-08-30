# Django Basic Commands & Admin Guide

## 1. Create a Django Project

```bash
django-admin startproject project_name
```

Example:

```bash
django-admin startproject myproject
```

---

## 2. Navigate to Project Folder

```bash
cd myproject
```

---

## 3. Run the Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

To use a custom port:

```bash
python manage.py runserver 8080
```

---

# Django App Commands

## Create a New App

```bash
python manage.py startapp app_name
```

Example:

```bash
python manage.py startapp blog
```

After creating the app, add it to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # Default apps
    'blog',
]
```

---

# Database Commands

## Create Migration Files

Whenever you make changes to models:

```bash
python manage.py makemigrations
```

For a specific app:

```bash
python manage.py makemigrations app_name
```

## Apply Migrations

```bash
python manage.py migrate
```

## Show Migrations

```bash
python manage.py showmigrations
```

---

# Django Admin

## Create Admin/Superuser

Run:

```bash
python manage.py createsuperuser
```

You will be asked for:

```text
Username:
Email address:
Password:
Password (again):
```

After creating the superuser, start the server:

```bash
python manage.py runserver
```

Open Django Admin:

```text
http://127.0.0.1:8000/admin/
```

Login using your superuser credentials.

---

# Register Models in Django Admin

Suppose you have a model in `models.py`:

```python
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

Register it in `admin.py`:

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

Now the `Product` model will appear in the Django Admin panel.

---

# Customize Django Admin

```python
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
```

This enables:

* Displaying selected fields in the admin list
* Searching products
* Better admin interface customization

---

# Useful Django Commands

### Check for Project Issues

```bash
python manage.py check
```

### Open Django Shell

```bash
python manage.py shell
```

### Collect Static Files

```bash
python manage.py collectstatic
```

### Create a New Migration

```bash
python manage.py makemigrations
```

### Apply Database Changes

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

---

# Common Project Structure

```text
myproject/
│
├── manage.py
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── blog/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

---

# Quick Command Reference

| Command                            | Description              |
| ---------------------------------- | ------------------------ |
| `django-admin startproject name`   | Create a Django project  |
| `python manage.py startapp name`   | Create a Django app      |
| `python manage.py runserver`       | Start development server |
| `python manage.py makemigrations`  | Create migrations        |
| `python manage.py migrate`         | Apply migrations         |
| `python manage.py createsuperuser` | Create admin user        |
| `python manage.py shell`           | Open Django shell        |
| `python manage.py check`           | Check project for issues |
| `python manage.py collectstatic`   | Collect static files     |

---

## Requirements

Install Django:

```bash
pip install django
```

Check Django version:

```bash
django-admin --version
```

Happy Coding! 🚀
