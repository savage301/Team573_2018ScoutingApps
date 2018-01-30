import htmlPy
from back_end import BackEnd


app = htmlPy.AppGUI(
    title=u"Team 573 2018 Pit Scouting App")
app.maximized = True
app.template_path = "."
app.bind(BackEnd(app))

app.template = ("index.html", {})

if __name__ == "__main__":
    app.start()
