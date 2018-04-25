from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def root():
        return render_template('Boostrap.html'),200

@app.route('/inherits/')
def inherits():
        return render_template('base.html')
@app.route('/inherits/one/')
def inherits_one():
        return render_template('ir1.html')

@app.route('/inherits/two/')
def inherits_two():
        return render_template('ir2.html')

@app.route ('/users/')
def users():
	names = ['simon', 'thomas ', 'lee', 'jamie', 'sylvester']
	return render_template('loops.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1234, debug=True)
