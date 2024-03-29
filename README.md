## Тестовое задание MirGovorit backend
Нужно разработать небольшое приложение поварской книги на Django, со следующим функционалом:


1. add_product_to_recipe с параметрами recipe_id, product_id, weight. Функция добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.

2. cook_recipe c параметром recipe_id. Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.

3. show_recipes_without_product с параметром product_id. Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм. Страница должна генерироваться с использованием Django templates. Качество HTML верстки не оценивается.
   
## Запуск приложения
Установить зависимости:

```pip install -r requirements.txt```

Выполнить команду: 

```python manage.py runserver```

Или через docker-compose:

Для разработки:

1. ```docker-compose up -d --build```
2. ```docker-compose exec web python manage.py migrate --noinput```

Проверить работоспособность: запрос на ```http://localhost:8000/```

Для продакшена:
1. ```docker-compose -f docker-compose.prod.yml up -d --build```
2. ```docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput  ```
3. ```docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear  ```

Проверить работоспособность: запрос на ```http://localhost:1337/```