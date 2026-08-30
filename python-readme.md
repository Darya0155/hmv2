# Python Basic Commands

## Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

---

## Check Pip Version

```bash
pip --version
```

---

# Virtual Environment (venv)

## Create a Virtual Environment

```bash
python -m venv venv
```

Here `venv` is the virtual environment folder name.

You can use any name:

```bash
python -m venv myenv
```

---

## Activate Virtual Environment

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, you should see:

```text
(venv) project-folder>
```

---

## Deactivate Virtual Environment

```bash
deactivate
```

---

# Install Packages

Install a package:

```bash
pip install package_name
```

Example:

```bash
pip install django
```

Install a specific version:

```bash
pip install django==5.0
```

Upgrade a package:

```bash
pip install --upgrade django
```

---

# View Installed Packages

```bash
pip list
```

Check package details:

```bash
pip show django
```

---

# Requirements File

Create `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Install packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

# Upgrade Pip

```bash
python -m pip install --upgrade pip
```

---

# Complete Project Setup Example

```bash
# Create project folder
mkdir myproject

# Enter project folder
cd myproject

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install Django
pip install django

# Create Django project
django-admin startproject config .

# Run server
python manage.py runserver
```

## Useful Commands Quick Reference

| Command                               | Description                 |
| ------------------------------------- | --------------------------- |
| `python --version`                    | Check Python version        |
| `python -m venv venv`                 | Create virtual environment  |
| `venv\Scripts\activate`               | Activate venv (Windows)     |
| `source venv/bin/activate`            | Activate venv (Linux/macOS) |
| `deactivate`                          | Exit virtual environment    |
| `pip install django`                  | Install Django              |
| `pip list`                            | List installed packages     |
| `pip freeze > requirements.txt`       | Save dependencies           |
| `pip install -r requirements.txt`     | Install dependencies        |
| `python -m pip install --upgrade pip` | Upgrade pip                 |
