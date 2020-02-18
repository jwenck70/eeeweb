from flask import Flask, render_template, url_for
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/components.html')
# def components_page():
#     return render_template('components.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

@app.route('/')
def underconstruction():
    return 'We are engineering a better website before we engineer your emotions and energy. Stay tuned!'