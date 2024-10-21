from flask import Flask, render_template

app = Flask(__name__)

# Anasayfa
@app.route('/')
def home():
    return render_template('index.html')

# Shop sayfası
@app.route('/product')
def product():
    return render_template('product.html')

# Tekli ürün sayfası
@app.route('/single')
def single():
    return render_template('single.html')

# About sayfası
@app.route('/about')
def about():
    return render_template('about.html')

# Services sayfası
@app.route('/services')
def services():
    return render_template('services.html')

# Contact sayfası
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
