from flask import Flask, request, jsonify
import joblib

app=Flask(__name__)

model=joblib.load("coustomer_model.pkl")

@app.route("/")
def home():
   return jsonify({
     "message":"customer segmentation API is running"
   })
 
@app.route("/predict", methods=["POST"])
def predict():
  data=request.get_json()
  annual_income=int(data[annual_income])
  spending_score=int(data[spending_score])
  

  prediction=model.predict([[annual_income,spending_score]])
  print("prediction",prediction)
    
  cluster=int(prediction[0])
  print("cluster",cluster)

  if cluster==0:
    segment=" you are belong Low Income, High Spending group"
  elif cluster==1:
    segment="you are belong to High Income, Law Spending group"
  elif cluster==2:
    segment="you are belong to very Law Income, very High Spending group" 
  elif cluster==3:
    segment="you are belong to medium income,medium spending group" 
  elif cluster==4:
    segment="you are belong to medium income,law spending group" 
  else:
     segment="lnvalid customer segment"
    
    
  return jsonify({
    "prediction":segment
  })
     
if __name__=="__main__":
   app.run(debug=True)


