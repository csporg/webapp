Title
=================
This project is implemented to touch and feel Python Falsk WebApp

# Technologies
Python

Flask 

MySQL
                                                             
                                                             
                                               Traditional Web App
                                                           
Middle ware Python Flask
-----------------------------------
$sudo yum update -y && sudo yum install epel-release -y && sudo yum install wget -y && sudo yum install git -y 

$sudo yum install python-pip -y

$sudo yum install mysql mysql-devel mysql-common mysql-libs gcc  python-devel -y

$sudo pip install Flask

$sudo pip install mysqlclient==1.3.1

$sudo pip install Flask-MySQLdb

$git clone https://github.com/csporg/webapp.git

$cd src/flask

$gunicorn --bind 0.0.0.0:5001 wsgi
 
 
Reeference: 
 
https://pybuilder.io/documentation/tutorial
 
https://github.com/pyclectic/flask-example

Backend  MySQL 
------------------------
$wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm

$md5sum mysql57-community-release-el7-9.noarch.rpm

$sudo rpm -ivh mysql57-community-release-el7-9.noarch.rpm

$sudo yum install mysql-server

$sudo systemctl start mysqld

$sudo systemctl status mysqld

$sudo grep 'temporary password' /var/log/mysqld.log

$sudo mysql_secure_installation

$mysqladmin -u root -p version


                                               Distributed Web App


Python Flask
--------------
docker image build -t flask-image .

docker run --name flask-containergunci -p 5001:5001 -d flask-image

https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-centos-7


MySQL
----------
docker build -t my-mysql .

docker run -d -p 3306:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=Root_123 my-mysql

https://medium.com/better-programming/customize-your-mysql-database-in-docker-723ffd59d8fb
