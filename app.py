from flask import Flask, render_template
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
   
    Jobb(
        titel="Lastbilsförare",
        beskrivning="Transporterar gods över korta eller långa sträckor, antingen nationellt eller internationellt.",
        lön="23 000 - 30 000kr",
        plats="Malmö"
    )
]

beskrvningar=[
    JobbDetaljer(
        "Dina huvudsakliga arbetsuppgifter är att planera och utföra dagliga leveranser av pallgods i Malmö med omnejd. Detta inkluderar att ansvara för säker lastning och lossning av varor samt att hantera leveransdokument för att se till att alla uppgifter är korrekta. Dessutom ingår det att utföra daglig tillsyn av fordonet för att säkerställa att det är i gott skick.",
        "För att vara aktuell för tjänsten krävs det att du har C-körkort och ett giltigt YKB (Yrkeskompetensbevis). Vi ser det som en stor fördel om du har minst två års erfarenhet av att köra lastbil, och truckkort är meriterande. Du bör även ha goda kunskaper i svenska, både i tal och skrift, och vara en ansvarsfull, noggrann och självständig person.",
        "Vi erbjuder en konkurrenskraftig månadslön på 23 000 – 30 000 kr beroende på din erfarenhet och eventuell obekväm arbetstid. Dessutom får du förmåner som friskvårdsbidrag och betald övertid. Du får arbeta i ett litet, familjärt team med god sammanhållning.", 
        "Arbetstiden är på heltid, måndag till fredag, med start kl. 07:00 och slut kl. 16:00."
        )
]

@app.route("/lediga_jobb.html")
def lediga_jobb():
    return render_template("lediga_jobb.html", jobb=jobb_lista)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/mer_om_jobbet.html")
def jobbet():
    return render_template("mer_om_jobbet.html", besk=beskrvningar)

if __name__ == "__main__":
    app.run(debug=True)