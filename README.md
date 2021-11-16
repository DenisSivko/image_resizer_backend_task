# Image resizer
## Техническое задание [Запросы в POSTMAN](https://documenter.getpostman.com/view/2157092/TzkzrzNU)
Необходимо разработать сервис, на основе фреймворка Django c использованием DRF, который позволит загружать изображения с компьютера пользователя, или по ссылке, а затем изменять их размер используя библиотеку Pillow. Изображения должны сохраняться на диск.
Так же необходимо реализовать api в соответствии с запросами в POSTMAN(закреплённом сверху).
----
### Локальный запуск приложения
#### Что бы поднять контейнеры
```shell
docker stop $(docker ps -aq)
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
```
#### Что бы зайти внутрь контейнера бекенда
```shell
docker-compose exec backend sh
```
Сервис будет доступен по ссылке [http://localhost:8000/admin/login/?next=/admin/](http://localhost:8000/admin/login/?next=/admin/)