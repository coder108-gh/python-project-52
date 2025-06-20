### Hexlet tests and linter status:
[![Actions Status](https://github.com/coder108-gh/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/coder108-gh/python-project-52/actions)

### SonarCube:
[![Coverage](https://img.shields.io/sonar/coverage/coder108-gh_python-project-52?server=https://sonarcloud.io)](https://sonarcloud.io/summary/new_code?id=coder108-gh_python-project-52)

### [Демо](https://python-project-52-w6ey.onrender.com) на render.com
****
## Task Manager (Менеджер задач)
****
##### Менеджер задач — это приложение ведения задачю Разработано на Django/Python. Основные функции: создавать задачи, назначать исполнителей, устанавливать  метки и статусы.

### Технологии


|                                                   | Описание                                                                                           |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Django](https://www.djangoproject.com/)          | "Веб-фреймворк на Python," |
| [Bootstrap 5](https://getbootstrap.com/)          | ""CSS-фреймворк для создания адаптивных веб-проектов"                   |
| [PostgreSQL](https://www.postgresql.org/)         | "СУБД"                                   |
| [Gunicorn](https://gunicorn.org/)                 | "Сервер WSGI для Unix для развертывания приложений на Python"                                      |
| [uv](https://docs.astral.sh/uv/)                  | ""пакетный менеджер для проектов на Python"                             |
| [Whitenoise](http://whitenoise.evans.io/en/latest/) | "Библиотека для обслуживания статических файлов в приложениях на Python"|
| [Rollbar](https://rollbar.com/)                   | "Инструмент для мониторинга ошибок и отслеживания неполадок в режиме реального времени"|
| [ruff](https://docs.astral.sh/ruff/)              | "Линтер и форматерRust"                              |

### Установка:

#### Необходимо:
- Python 3.12 +
- uv 
#### Клонируем репозиторий:
```
git clone git@github.com:coder108-gh/python-project-52.git && cd python-project-52
```
#### Создать файл .env:
```python
SECRET_KEY = ... #  django-insecure
ROLLBAR_TOKEN = ... #  rollbat token
```

#### Устанавка:
```
make install
```
#### Запуск dev-сервера:
```
make dev
```
#### Проект будет доступен по адресу http://127.0.0.1:8000
****

#### Запуск продакшн сервера 
```
make start-prod
```
#### Проект будет доступен по адресу http://127.0.0.1:8000

****

После запуска приложения необходимо зарегистрироваться и тогда можно создавать задачи, назначать им исполнителей и метки, устанавливать статусы.
