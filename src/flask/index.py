from flask import Flask, request, render_template
from flask_mysqldb import MySQL
application = Flask(__name__)

#configure db
application.config['MYSQL_HOST'] = '3.84.28.176'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = 'Root_123'
application.config['MYSQL_DB'] = 'indigo'
mysql = MySQL(application)

@application.route('/')
def selectdata():
       cur = mysql.connection.cursor()
       cur.execute('select * from student')
       data = cur.fetchall()
       return render_template('index.html', msg=data)
if __name__ == '__main__':
    application.run(port=5001)


