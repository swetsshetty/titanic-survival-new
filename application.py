
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from sklearn.preprocessing import StandardScaler
import pickle
scaler = StandardScaler()
application = Flask(__name__) # initializing a flask app
app=application
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user	Age	SibSp	Parch	Fare	Sex_male
            Pclass=float(request.form['Pclass'])
            Age = int(request.form['Age'])
            SibSp = float(request.form['SibSp'])
            Parch = float(request.form['Parch'])
            Fare = float(request.form['Fare'])
            Sex = int(request.form['Sex'])
            filename = 'titanic_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict(scaler.fit_transform([[Pclass,Age,SibSp,Parch,Fare,Sex]]))
            print('prediction is', prediction)
            # showing the prediction results in a UI
            if prediction[0]==1:
                res='survived'
            else:
                res='not survived'

            return render_template('results.html',prediction=res)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True) # running the app