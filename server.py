from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Pants are an illusion"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info_submission', methods=['POST'])
def submit_info():
    session['username'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_lang'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)