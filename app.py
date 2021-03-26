from flask import (
    Flask, 
    render_template,
    request,
    session,
    redirect,
    url_for
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Achal', password = '2017B30'))
users.append(User(id=2, username='Pratyush', password = '2017B32'))


app = Flask(__name__)
app.secret_key = 'abcd'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/faculty', methods = ['GET','POST'])
def faculty():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user =[x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('faculty'))

        return redirect(url_for('/'))

    return render_template('login.html')
'''
@app.route('/faculty')
def faculty():
    return render_template('faculty.html')'''

if __name__ == "__main__": 
    app.run(debug=True)