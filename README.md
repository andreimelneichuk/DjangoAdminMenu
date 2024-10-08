# Документация по использованию шаблона для древовидного меню

## Введение

Этот документ описывает, как использовать шаблон для отображения древовидного меню на веб-страницах вашего Django проекта. Меню хранится в базе данных и может быть отрисовано на любой странице с помощью шаблонного тега.

## Подключение шаблонного тега

Чтобы использовать древовидное меню в вашем проекте, выполните следующие шаги:

### 1. Загрузка шаблонных тегов

Перед использованием тега шаблона в любом HTML-файле, необходимо загрузить его в шаблоне. В начале вашего шаблона добавьте следующую строку:

```html
{% load menu_tags %}
```

Эта строка загружает все теги шаблонов, определенные в `menu_tags.py`.

### 2. Использование тега для отображения меню

Чтобы отобразить меню на странице, используйте следующий тег шаблона:

```html
{% draw_menu 'название_меню' %}
```

- `название_меню` — это имя меню, которое вы задали в админке Django при создании меню. 

Пример:

```html
{% draw_menu 'main_menu' %}
```

Этот тег будет выводить меню с именем `'main_menu'`.

### 3. Вставка тега в шаблон

Вставьте тег в нужное место вашего HTML-шаблона, чтобы отобразить меню. Например, если вы хотите, чтобы меню отображалось в заголовке сайта, вы можете сделать это так:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Site</title>
</head>
<body>
    <header>
        <!-- Главное меню -->
        {% draw_menu 'main_menu' %}
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <!-- Футер -->
    </footer>
</body>
</html>
```

### 4. Работа с активными пунктами меню

Пункт меню будет автоматически помечен как активный, если его URL совпадает с текущим URL страницы. Это означает, что текущий активный пункт меню будет выделен, что помогает пользователям понять, на какой странице они находятся.

### 5. Примеры использования

#### Пример 1: Простое меню

Если ваше меню состоит из простого списка ссылок, оно будет отображаться как обычный список:

```html
{% draw_menu 'simple_menu' %}
```

#### Пример 2: Меню с подменю

Если у вашего меню есть подменю, оно будет отображаться как вложенные списки:

```html
{% draw_menu 'nested_menu' %}
```

### 6. Создание меню в админке

1. Перейдите в админку Django по адресу `/admin/`.
2. Перейдите к модели `Menu` и создайте новое меню, указав его название.
3. Перейдите к модели `MenuItem` и добавьте пункты меню. Укажите родительский пункт для создания иерархии, URL или имя URL для перехода, и порядок отображения.

## Заключение

Использование шаблонного тега для отображения древовидного меню позволяет легко управлять и отображать меню на вашем сайте. Убедитесь, что вы правильно указали имя меню в теге шаблона и что данные меню корректно внесены в базу данных через админку Django.
