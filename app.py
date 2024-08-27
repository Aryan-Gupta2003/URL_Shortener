from flask import Flask, request, redirect, render_template
from config import Config
from models import db, save_url_mapping, URLMapping, get_long_url
from utils import generate_short_url

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = b'EW\x03\xfd?A$\xfc\xeaH\xc1\xcf\r6\x07\rg\x93&\xf5U"\xd2K'

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if not long_url:
            flash('Please enter a valid URL.')
            return redirect(url_for('index'))
        
        short_url = generate_short_url(long_url)
        existing_short_url = save_url_mapping(long_url, short_url)
        full_short_url = request.host_url + existing_short_url
        return render_template('index.html', short_url=full_short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
