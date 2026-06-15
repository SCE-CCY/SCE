from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/roles')
def roles():
    return render_template('roles.html')

@app.route('/channels')
def channels():
    return render_template('channels.html')

@app.route('/essence')
def essence():
    return render_template('essence.html')

if __name__ == '__main__':
    app.run(debug=True)
