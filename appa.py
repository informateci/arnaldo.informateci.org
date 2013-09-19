from flask import Flask, redirect, render_template, url_for, send_from_directory, request
from arnaldo import sproloquio, accendi_il_cervello
#from motorino_d_avviamento import accendi_il_cervello

app = Flask(__name__)
accendi_il_cervello()

#count_proverbia = []
#def contaggio(arg):
#    sleep(600)
#    count_proverbia = []
#
#from threading import Thread
#
#t = Thread(target = contaggio)
#t.start()

@app.route("/proverbia")
def proverbia():
    import sqlite3
    conn = sqlite3.connect('/home/httpd/arnaldo.informateci.org/database.db')
    c = conn.cursor()
    if request.method == 'GET':
        ip = str(request.remote_addr)
        #if ip not in count_proverbia:
        #    count_proverbia.append(ip)
        try:
            i = (request.args['id'],)
            c.execute("SELECT proverbio FROM proverbia WHERE id = ?", i)
            p = c.fetchone()[0].replace('\\\'','\'')
            conn.close()
            return render_template("proverbia.html", proverbio = p, users = "0", id = str(i[0]))
        except Exception as e:
            try:
                p = sproloquio.proverbia()
                c.execute("INSERT INTO proverbia(proverbio) VALUES (?)", (p.replace('\'','\\\''),))
                conn.commit()
                conn.close()
                i = c.lastrowid
                import urllib
                return render_template("proverbia.html", proverbio = p, id = str(i), users = "0")
            except Exception as e:
                return str(e.args) + '<br/>'+str(e) + ' ' + p
            #i = c.lastrowid
            #conn.commit()
            #return str(i)
            #import urllib
            #return render_template("proverbia.html", proverbio = p, id = str(i), urlprov = urllib.quote(p.encode('utf8')), users = str(len(count_proverbia)))
    conn.close()

@app.route("/boobs")
def boobs():
    if arna == None:
        return "None"
    return render_template("boobsplease.html", link = sproloquio.boobs())

@app.route("/attardati")
def attardati():
    return render_template("proverbia.html", proverbio = sproloquio.attardati())

@app.route("/ANAL")
def ANAL():
    return render_template("proverbia.html", proverbio = sproloquio.ANAL())

@app.route("/<filename>")
def arnafile(filename):
    return send_from_directory('/home/httpd/arnaldo.informateci.org/resources', filename)

if __name__ == "__main__":
    app.run()
