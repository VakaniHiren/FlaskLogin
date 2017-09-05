from flask import Flask, render_template,request,redirect,url_for
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hiren'
app.config['MYSQL_DATABASE_DB'] = 'flaskdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
       uid = request.form['uid']
       upass = request.form['upass']
       cur = mysql.connect().cursor()
       try:
           sql = "SELECT * FROM usertb WHERE uname='%s' and upass='%s'" % (uid, upass)
           cur.execute(sql)
           res = cur.rowcount
           if (res==1):
               return redirect(url_for('success', name=uid))
           else:
               return render_template('login.html')
       except:
           print "Error"
   else:
      uid = request.args.get('uid')
      upass = request.args.get('upass')
      return render_template('login.html')

if __name__ == '__main__':
       app.run(debug=True)