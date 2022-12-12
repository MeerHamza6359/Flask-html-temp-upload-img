from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='template',
     static_url_path='', 
     static_folder='static')

app.config["IMAGE_UPLOADS"] = "/home/hamza/Assigmanet-1/web_flask_app/media"

@app.route("/")
def main():
	return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            return render_template("upload.html", uploaded_image=image.filename)
    return render_template("upload.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOADS"], filename)


if __name__ == "__main__":
    app.run()

