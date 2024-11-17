from flask import Flask
#from routes.about import about_blueprint
from routes.index import index_blueprint
from routes.admin import admin_blueprint

app = Flask(__name__)

# Blueprint'leri uygulamaya kaydet
#app.register_blueprint(about_blueprint, url_prefix='/about')
app.register_blueprint(index_blueprint, url_prefix='/index')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.route('/')
def home():
    return redirect(url_for('index.index_home'))


if __name__ == "__main__":
    app.run(debug=True)

