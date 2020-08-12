from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/components.html')
# def components_page():
#     return render_template('components.html')

@app.route('/dreamjob')
def dreamjob():
    return redirect('https://content.e-motionsengineering.com/dreamjob')
    
@app.route('/dreamjob/')
def dreamjob2():
    return redirect('https://content.e-motionsengineering.com/dreamjob')


@app.route('/mycareer')
def mycareer():
    return redirect('https://content.e-motionsengineering.com/mycareer')
    
@app.route('/mycareer/')
def mycareer2():
    return redirect('https://content.e-motionsengineering.com/mycareer')

@app.route('/vipcareer')
def vipcareer():
    return redirect('https://content.e-motionsengineering.com/vipcareer/buy')
    
@app.route('/mycareer/')
def vipcareer2():
    return redirect('https://content.e-motionsengineering.com/vipcareer/buy')

@app.route('/challenge')
def challenge():
    return redirect('https://content.e-motionsengineering.com/perfect-life-10-day-meditation-challenge')
    #return render_template('10daychallenge.html')
    #return 'We are engineering a better website before we engineer your emotions and energy. Stay tuned! Please :D'

@app.route('/challenge/')
def challenge2():
    return redirect('https://content.e-motionsengineering.com/perfect-life-10-day-meditation-challenge')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/')
# def underconstruction():
#     return 'We are engineering a better website before we engineer your emotions and energy. Stay tuned! Please :D'