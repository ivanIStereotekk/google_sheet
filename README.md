# google_sheet
Google Sheets API.  //.   Flask. // SQLAlchemy  // React in a proccess //PostgresSQL // Scheduler (CRON)


Приложение которое парсит данные из гугл таблицы Google Sheets (Exel file), 


Поля такие...| id = №	| заказ =№ |	стоимость,$ |	срок поставки	|


В общем скрипт собирает данные от туда каждые "икс" минут/секунд. (Настроен scheduler)


Запрашивает А-Пи-Ай Центробанка получает данные о текущем курсе валют, ( JSON )


Берет короче данные из Google Sheets таблицы, формирует цену в рублях по текущему курсу.


Потом кладет все данные в PostgresSQL БД (включая цену в рублях по курсу)


Потом, если меняешь данные в таблице, то в базе данных все тоже меняется.


Удалил данные, в базе тоже удалится... Scheduler может переписывать базу по текущему состоянию файла в гугл диске. 

React и Flask, на фронте будет оповещалка - срок поставки сейчас закончится. какое то еще взаимодействие

Микросервисная архитектура, .env конфиги

Еще в этом стэке будет бот который шлет сообщения клиенту о доставке товара.

Знаю что ключи и .env нельзя, но пусть лежат сейчас. Это демонстрация.


Что под капотом: 
Под капотом requirements.txt можно почитать.

На большом прод проекте сделал бы крон асинхронный. Но тут нет смысла...


Конечно я не гений программирования. Но обязательно стану если не помру раньше!

Берегите себя
