from flask import Flask, render_template, request, redirect, url_for
from jobb import Jobb, JobbDetaljer


app = Flask(__name__)


jobb_lista = [
    
]

beskrvningar=[
    
]



@app.route("/lediga_jobb.html")
def lediga_jobb():
    return render_template("lediga_jobb.html", jobb=jobb_lista)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")
    
@app.route("/admin.html")
def admin():
    return render_template("admin.html")

# Lägg till en ny route som hanterar formulärinlämningen
@app.route("/skapa-jobb", methods=["POST"])
def skapa_jobb():
    # Hämta data från formuläret med hjälp av name-attributen
    titel = request.form.get("titel")
    beskrivning = request.form.get("beskrivning")
    lon = request.form.get("lon")
    plats = request.form.get("plats")
    ansvar = request.form.get("ansvar")
    krav = request.form.get("krav")
    formaner = request.form.get("formaner")
    arbetstider = request.form.get("arbetstider")

    # Skapa nya objekt och lägg till dem i listorna
    nytt_jobb = Jobb(
        titel=titel,
        beskrivning=beskrivning,
        lön=lon,
        plats=plats
    )
    ny_beskrivning = JobbDetaljer(
        Ansvar=ansvar,
        krav=krav,
        Förmåner=formaner,
        Arbetstider=arbetstider
    )

    jobb_lista.append(nytt_jobb)
    beskrvningar.append(ny_beskrivning)

    # Omdirigera tillbaka till "Lediga jobb"-sidan för att se det nya jobbet
    return redirect(url_for("lediga_jobb"))

@app.route("/mer_om_jobbet.html/<int:jobb_id>")
def jobbet(jobb_id):
    # Check if the job_id is valid
    if 0 <= jobb_id < len(jobb_lista):
        jobb_data = jobb_lista[jobb_id]
        jobb_detaljer = beskrvningar[jobb_id] # Assuming index corresponds
        return render_template("mer_om_jobbet.html", jobb=jobb_data, besk=jobb_detaljer)
    else:
        return "Jobbet hittades inte", 404

if __name__ == "__main__":
    app.run(debug=True)