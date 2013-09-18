from flask import Flask, redirect, render_template, url_for, send_from_directory, request
from arnaldo import TestBot

app = Flask(__name__)

try:
    arna = TestBot('','','')
except Exception:
    arna = None

#arnaldo = None

@app.route("/proverbia")
def proverbia():
    if arna == None:
        return "None"
    if request.method == 'GET':
        try:
            p = request.args['p']
            return render_template("proverbia.html", proverbio = p)
        except Exception:
            p = arna.saggezza()
            import urllib
            return render_template("proverbia.html", proverbio = p, urlprov = urllib.quote(p.encode('utf8')))

@app.route("/boobs")
def boobs():
    if arna == None:
        return "None"
    return render_template("boobsplease.html", link = arna.bombe('',''))

@app.route("/attardati")
def attardati():
    if arna == None:
        return "None"
    return render_template("proverbia.html", proverbio = arna.attardati('',''))

@app.route("/ANAL")
def ANAL():
    if arna == None:
        return "None"
    return render_template("proverbia.html", proverbio = arna.ANAL())

@app.route("/<filename>")
def arnafile(filename):
    return send_from_directory('/home/httpd/arnaldo/resources', filename)

if __name__ == "__main__":
    app.run()
