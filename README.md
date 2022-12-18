# EMU-Graduation
CMSE 405 graduation project

## Important Information
We are using Docker for database, to achieve this create database with this
```bash
docker run --name [mysqldb-name] -e MYSQL_ROOT_PASSWORD=[my-secret-pw] -d -p 3306:3306 mysql:tag
```
for more information see this [resource](https://hub.docker.com/_/mysql)

then combine database with mysql to ease our access and modification add phpmyadmin to database

```bash
docker run --name [phpmyadmin] -d --link [mysqldatabase-created-before]:db -p 8080:80 phpmyadmin
```

for more information see this [resource](https://hub.docker.com/r/phpmyadmin/phpmyadmin/)

## ER Diagram
![](assets/er-diagram.png)

## Sources
Sources that has been used in development of this project.

- [How to connect docker mysql database to Python application](https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa)