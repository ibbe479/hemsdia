from flask import Flask, render_template, request, redirect, url_for
from jobb import Jobb, JobbDetaljer


app = Flask(__name__)


jobb_lista = [
    Jobb(
        titel="Lastbilsförare",
        beskrivning="Transporterar gods över korta eller långa sträckor, antingen nationellt eller internationellt.",
        lön="23 000 - 30 000kr",
        plats="Malmö"
    ),
    Jobb(
        titel="Butiksbiträde",
        beskrivning="Hjälper kunder och sköter kassan i butik.",
        lön="20 000 - 25 000kr",
        plats="Stockholm"
    ),
]

beskrvningar=[
    JobbDetaljer(
        "Dina huvudsakliga arbetsuppgifter är att planera och utföra dagliga leveranser av pallgods i Malmö med omnejd. Detta inkluderar att ansvara för säker lastning och lossning av varor samt att hantera leveransdokument för att se till att alla uppgifter är korrekta. Dessutom ingår det att utföra daglig tillsyn av fordonet för att säkerställa att det är i gott skick.",
        "För att vara aktuell för tjänsten krävs det att du har C-körkort och ett giltigt YKB (Yrkeskompetensbevis). Vi ser det som en stor fördel om du har minst två års erfarenhet av att köra lastbil, och truckkort är meriterande. Du bör även ha goda kunskaper i svenska, både i tal och skrift, och vara en ansvarsfull, noggrann och självständig person.",
        "Vi erbjuder en konkurrenskraftig månadslön på 23 000 – 30 000 kr beroende på din erfarenhet och eventuell obekväm arbetstid. Dessutom får du förmåner som friskvårdsbidrag och betald övertid. Du får arbeta i ett litet, familjärt team med god sammanhållning.", 
        "Arbetstiden är på heltid, måndag till fredag, med start kl. 07:00 och slut kl. 16:00."
        ),
    
    JobbDetaljer(
        "Som butiksbiträde är dina huvudsakliga arbetsuppgifter att hjälpa kunder, ta betalt vid kassan, fylla på varor och hålla butiken städad. Du kommer att vara företagets ansikte utåt och ska ge en utmärkt service till alla kunder.",
        "Vi söker dig som är serviceinriktad, har god social kompetens och kan arbeta självständigt. Tidigare erfarenhet av butiksarbete är meriterande men inte ett krav. Du behöver vara över 18 år och ha goda kunskaper i svenska.",
        "Vi erbjuder en timlön på 110 kr, personalrabatt, och möjligheter till vidareutbildning och avancemang inom företaget. Du kommer att arbeta i ett trevligt team med härliga kollegor.", 
        "Arbetstiderna varierar mellan dag- och kvällspass, inklusive helger. Arbetstiden är på deltid, med möjlighet till utökning vid behov."
    )
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