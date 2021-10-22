from flask import Flask, request, render_template, redirect, url_for

from forms import LibForm
from models import films

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/library/", methods=['GET', 'POST'])
def film_list():
    form = LibForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            films.create(form.data)
            films.save_all()
        return redirect(url_for("film_list"))

    return render_template("library.html", form=form, films=films.all(), error=error)


@app.route("/library/<int:film_id>/", methods=['GET', 'POST'])
def film_details(film_id):
    film = films.get(film_id -1)
    form = LibForm(data=film)

    if request.method == "POST":
        if form.validate_on_submit():
            films.update(film_id - 1, form.data)
        return redirect(url_for("film_list"))
    return render_template("film.html", form=form, film_id=film_id)


if __name__ == "__main__":
    app.run(debug=True)