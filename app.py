from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():

    context = {
        "title": "My Presentation",
        "slide": {
            "width": 1511,
            "height": 1133,
        },
    }

    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
