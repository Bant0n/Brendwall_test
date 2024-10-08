# Telegram https://t.me/B4nton
# Приложение для управления продуктами

## Введение и функциональные возможности

Это Django-приложение предоставляет API для управления продуктами и HTML-страницу для добавления и отображения продуктов. Пользователи могут создавать новые продукты, просматривать все добавленные продукты и управлять ими через интуитивный пользовательский интерфейс.

Основные возможности приложения:

- Создание новых продуктов через API или HTML-форму.
- Просмотр списка всех продуктов с использованием AJAX-запросов.
- Проверка вводимых данных: цена должна быть положительным числом, название — не пустым.

## Технологии

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, JavaScript (Fetch API)
- **Database**: SQLite (по умолчанию в Django)

## Предварительные требования

Для запуска приложения убедитесь, что у вас установлены:

- Python 3.x
- pip (инструмент для управления пакетами Python)
- Виртуальное окружение (рекомендуется)

## Начало работы и установка

Следуйте этим шагам для установки и запуска приложения на локальной машине:

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/yourusername/product-management-app.git
    cd product-management-app
    ```

2. **Скачайте и poetry:**

    ```bash
    pip install poetry
    ```

3. **Установите зависимости:**

    ```bash
    poetry install
    ```

4. **Запустите миграции для настройки базы данных:**

    ```bash
    python manage.py migrate
    ```

5. **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

6. **Откройте приложение в браузере:**

    Перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), чтобы открыть пользовательский интерфейс.

## Использование

- Используйте форму на главной странице для добавления новых продуктов.
- После успешного добавления продукта список продуктов автоматически обновится.
- Продукты отображаются в таблице ниже формы, данные обновляются динамически с использованием JavaScript.

## Конечные точки API

- **GET /api/v1/products/**: Возвращает список всех продуктов. (Без HTML)
- **POST /api/v1/products/**: Добавляет новый продукт (принимает JSON с `name`, `description` и `price`). (Без HTML)
- **GET /api/v1/index/**: Добавляет новый продукт (принимает JSON с `name`, `description` и `price`). (C HTML)
- **POST /api/v1/index/**: Добавляет новый продукт (принимает JSON с `name`, `description` и `price`). (C HTML)

### Пример JSON для POST-запроса

```json
{
  "name": "Пример продукта",
  "description": "Описание примерного продукта.",
  "price": 19.99
}
```
