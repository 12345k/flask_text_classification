from flask import Flask, render_template ,request
from flask_wtf import FlaskForm

from sklearn.externals import joblib

app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
def index():
   return render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
	if str(request.method)==str('POST'):
		file = request.form['text']
		if len(file)==0: 
			return render_template('index.html', label="Empty")
		prediction = model.predict([file])
		target=['alt.atheism','comp.graphics','comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','comp.windows.x','misc.forsale','rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey','sci.crypt','sci.electronics','sci.med','sci.space','soc.religion.christian','talk.politics.guns','talk.politics.mideast','talk.politics.misc','talk.religion.misc']
		label = target[prediction[0]]
		return render_template('index.html', label=label)
	
if __name__ == "__main__":
    model = joblib.load('filename.pkl')
    app.run(debug=True)