#!/usr/bin/env python
from flask import Flask, redirect, render_template, url_for, send_from_directory, request
from arnaldo import sproloquio, accendi_il_cervello
PATH='/home/autoscatto/prototipi/git/arnaldo.informateci.org'

app = Flask(__name__)

import os
os.chdir(PATH + '/arnaldo')
accendi_il_cervello()
os.chdir(PATH)

@app.route("/proverbia")
def proverbia():
    if request.method == 'GET':
        i = request.args.get('id', False)
        print i
        if i:
            p=sproloquio.proverbiabyid(i)
            pid=i
        else:
            p,pid=sproloquio.proverbiaandid()
        return render_template("proverbia.html", proverbio = p, id = pid)

@app.route("/boobs")
def boobs():
    return render_template("boobsplease.html", link = sproloquio.boobs())

@app.route("/attardati")
def attardati():
    return render_template("proverbia.html", proverbio = sproloquio.attardati(), ricarica="attardati")

@app.route("/anal")
def anal():
    return render_template("proverbia.html", proverbio = sproloquio.ANAL(), ricarica="anal")


@app.route("/static/<filename>")
def arnafile(filename):
    return send_from_directory(os.path.join(PATH,'resources'), filename)

@app.route("/")
def ANAL():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=False)
