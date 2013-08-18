from flask import Flask, request, Response, session, g, redirect, url_for, \
	abort, render_template, flash, send_from_directory, send_file, escape

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('WebTools_Settings')

@app.route('/')
def index():
	print url_for('logout', _external=True)
	print app.config['SERVER_NAME']
	if 'username' in session:
		return render_template('Login.html', loggedIn = True)
	else:
		return render_template('Login.html', loggedIn = False)
  #  if 'username' in session:
   #     return 'Logged in as %s' % escape(session['username'])
   # return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    	if request.form['username'] == 'ATGUuser':
        	session['username'] = request.form['username']
        	return redirect(url_for('index'))
        else:
        	return '''
    			<p>Incorrect Username
        		<form action="" method="post">
        		    <p><input type=text name=username>
        		    <p><input type=submit value=Login>
        		</form>
        		'''
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
        '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key (keep this the same as other utilities to have cross utility logins)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



if __name__ == '__main__':
	app.run()