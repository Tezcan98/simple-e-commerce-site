from flask import Blueprint, render_template

# Admin Blueprint'ini tanımlıyoruz, static ve template klasörleri bir üst seviyede
index_blueprint = Blueprint(
    'index', __name__,
    static_folder='../static',   # static dosyaları ana klasörden alıyoruz
    template_folder='../templates'  # template dosyaları ana klasörden alıyoruz
)

@index_blueprint.route('/')
def index_home():  
    return render_template('index.html')

