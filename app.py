from flask import Flask, render_template, request
from flask import url_for, redirect, url_for, flash, session


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

# 7
@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

# 2
@app.route('/basic_grid')
def basic_grid():
    return render_template('basic_grid.html')

# 3
@app.route('/flex_wrap')
def flex_wrap():
    return render_template('flex_wrap.html')
# 5
@app.route('/flexbox')
def flexbox():
    return render_template('flexbox.html')
# 1
@app.route('/align_items')
def align_items():
    return render_template('align_items.html')
# 6
@app.route('/forms')
def forms():
    return render_template('forms.html')
# 4
@app.route('/justify_content')
def justify_content():
    return render_template('justify_content.html')

# 8
@app.route('/typography')
def typography():
    return render_template('typography.html')
# 9
@app.route('/color')
def color():
    return render_template('color.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/live', methods=['GET', 'POST'])
def live():
    if request.method == 'POST':
        code = request.form['code']
    else:
        code = "NONE"

    return render_template('live.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)