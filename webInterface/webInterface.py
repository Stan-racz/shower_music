from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/home/pi/douche/songs/"
ALLOWED_EXTENTIONS = "mp3"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.file:
            flash('no file')
        file = request.files['file']
        if file.filename == '':
            flash('no selected file')
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('index.html')
    
    return render_template('index.html')


if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True, threaded=True) 

