from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from GETFIT import GetFit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =   'sqlite:///SaveData.db'
db = SQLAlchemy(app)
Letsgetfit = GetFit()
@app.route('/')
def index():
    return render_template("Interface.html")
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    height = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(15))
    activity_level = db.Column(db.String(25))
    def __repr__(self):
        return '<Task %r>'  %self.id
    
with app.app_context():
    db.create_all()
@app.route('/sumbit', methods=['POST'])
def sumbit():
    name = request.form['name']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])
    gender = request.form['gender']
    activity_level = request.form['activity_level']
    
    new_entry = Todo(
        name = name,
        height = float(height),
        weight = float(weight)    ,
        age = int(age),
        gender = gender,
        activity_level = activity_level
    )
    db.session.add(new_entry)
    db.session.commit()
    InhertiedObj = GetFit()
    male_calorie_intake = int(InhertiedObj.Male_Calorie_calulator(weight,height,age,activity_level))
    Female_Calorie_intake = InhertiedObj.Female_Calorie_calulator(weight,height,age,activity_level)

    bmi = Letsgetfit.Bmi_Calculation(height,weight)
    if bmi < 18.5:
        if gender == "Male":
            return render_template("underweight.html", bmi = bmi,calorie = male_calorie_intake,name = name,activity_level=activity_level)
        else:
            return render_template("underweight.html",bmi=bmi, calorie = Female_Calorie_intake,name = name,activity_level=activity_level)
    elif 18.5 <= bmi <24:
        if gender == "Male":
            return render_template("underweight.html", bmi = bmi,calorie = male_calorie_intake,name = name,activity_level=activity_level)
        else:
            return render_template("underweight.html",bmi=bmi, calorie = Female_Calorie_intake,name = name,activity_level=activity_level)
    else:
        if gender == "Male":
            return render_template("Overweight.html", bmi = bmi,calorie =male_calorie_intake,name = name,activity_level=activity_level)
        else:
            return render_template("Overweight.html",bmi=bmi, calorie = Female_Calorie_intake,name = name,activity_level=activity_level)

if __name__ == "__main__":
    app.run(debug=True)