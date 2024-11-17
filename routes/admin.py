from flask import Blueprint, render_template

# Admin Blueprint'ini tanımlıyoruz, static ve template klasörleri bir üst seviyede
admin_blueprint = Blueprint(
    'admin', __name__,
    static_folder='../static',   # static dosyaları ana klasörden alıyoruz
    template_folder='../templates'  # template dosyaları ana klasörden alıyoruz
)

@admin_blueprint.route('/')
def admin_home():
    # 'admin.html' şablonunu render ediyoruz
    return render_template('admin/index.html')

