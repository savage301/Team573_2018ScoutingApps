import htmlPy
from back_end import BackEnd
import os


app = htmlPy.AppGUI(
    title=u"Team 573 2018 Pit Scouting App")
app.maximized = True
#app.template_path = "C:\Users\savag\Desktop\ScoutingApp\Team573_2018ScoutingApps\MatchScoutingApp"
app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")
app.bind(BackEnd(app))

app.template = ("index.html", {})


if __name__ == "__main__":
    app.start()
