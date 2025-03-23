# Comppractic2c

## Задание 1
На основе бордов:
[борд 1](https://replit.com/@zhukov/kp-28-03-my-server-1)
[борд 2](https://replit.com/@zhukov/kp-28-03-my-server-2)
, сделав форки этих бордов, реализуйте следующее задание:

Исследуйте функционал двух способов создания простейшего http-сервера.
Перепешите приложения так, чтобы приложение отправляло  ответ на запрос по localhost:port (или с по доменному имени replit.com) ваш логин в системе moodle и текущую дату и время в текущей локали (СПБ, МСК). Например, на запрос: https://kp-28-03-my-server-2.zhukov.repl.co/ Ответ: nzhukov, 12.03.25 16:40:27
Это надо сделать в обоих бордах-решениях (с фреймворком и без него). Можно использовать другой MIME-тип и формат ответа (например, json, html или что-то другое).
Дополнительное необязательное задание (НЕ ВЫПОЛНЕННО): исследовать и разработать аналогичный функционал пункта 2 для какого-либо серверного фреймворка на Node.js или другом языке:
PHP*, JS (Node)*, Go*, Ruby*(Ruby on Rails), Kotlin, Java (Spring).

**Результат:**

**mainnoframework.py**

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/1conmain.png)

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/1hostmain.png)

**mainframeworkflask.py**


![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/12con.png)

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/12host.png)

---

## Задание 2.1
Разработать веб-приложение, которое позволяет пользователям отправлять данные через HTML-форму с помощью POST-запроса, обрабатывать их на сервере с использованием фреймворка Flask и сохранять в текстовый файл или базу данных.

Задачи:

1. Создание HTML-формы:

:small_blue_diamond: Разработайте HTML-страницу с формой, которая содержит следующие поля:
- логин в системе Moodle (текстовое поле) / тот же самый, что и в заданиях с автопроверкой курса "Серверные веб-технологии»;
- текущее время (выводится автоматически) (текстовое поле). Автоматический вывод реализовать как скрипт;
- кнопка "Отправить".

2. Создайте базовое приложение на Flask.
   
  :small_blue_diamond: Настройте маршруты для отображения формы и обработки POST-запросов.

3. Обработка POST-запроса:

:small_blue_diamond: При отправке формы данные должны отправляться на сервер через POST-запрос.
:small_blue_diamond: На сервере обработайте полученные данные (имя и текущее время).

4. Сохранение данных:

:small_blue_diamond: Сохраните полученные данные:
- в текстовый файл (например, data.json, data.csv) или
- в базу данных (например, SQLite).
5. Отображение подтверждения:

:small_blue_diamond: После успешной обработки и сохранения данных отобразите пользователю сообщение о том, что данные были успешно сохранены.

**Результат:**

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/21app.png)

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/21appv.png)

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/21appans.png)

---

## Задание 2.2
Разработать веб-приложение, которое позволяет пользователям отправлять данные через HTML-форму с помощью POST-запроса, обрабатывать их на сервере без использования фреймворков и сохранять в текстовый файл или базу данных. 

**Задачи:**
Аналогичны описанному в части 2.1.

**Результат:**

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/22appcon.png)

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/22appv.png)

![code1](https://github.com/MelnikNO/Comppractic2c/blob/main/Screen/ЛР5/22appans.png)
