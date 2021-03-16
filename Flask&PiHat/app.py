from flask import Flask, render_template, redirect, url_for, request, json, jsonify, current_app as app
import requests

app = Flask(__name__)

from sense_emu import SenseHat

#@app.route('/')
#def info():
#    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      return render_template('login.html')


#@app.route('/login')
#def login():
   #if request.method == 'POST':
    #user = request.form['nm']
    #name = ''
    #return render_template('login.html', name = name)
   #else:
    #user = request.args.get('nm')
    #return redirect(url_for('success',name = user))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')