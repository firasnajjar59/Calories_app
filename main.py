from flask.views import MethodView
from flask import Flask,render_template,request
from wtforms import Form,SubmitField,StringField
from backend.calorie import Calorie
from backend.temperature import Temperature
app= Flask(__name__,template_folder="templates",)


class HomePage(MethodView):

    def get(self):
        form = CaloriesForm()
        return render_template("index.html", form=form, result=False)

    def post(self):
        form= CaloriesForm(request.form)
        print(form.city.data)
        temp= Temperature(form.country.data,
                               form.city.data)
        calories = Calorie(float(form.weight.data),
                           float(form.height.data),
                           float(form.age.data),
                           temp.get_temperature()).calculate_calories()
        return render_template("index.html",
                               form=form,
                               result=True,
                               calories=calories)


class CaloriesForm(Form):

    country=StringField(label="Enter your country: ", default="israel")
    city=StringField(label="Enter your city: ", default="jerusalem")
    weight=StringField(label="Enter your weight: ", default="80.5")
    height=StringField(label="Enter your height: ", default="180")
    age=StringField(label="Enter your age: ", default="30")
    submit_button=SubmitField("Calculate")


app.add_url_rule("/",view_func=HomePage.as_view("home_page"))
app.run(debug="True")