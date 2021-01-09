import pickle
from flask import Flask, request, jsonify
from model_files.ml_model import fever_prediction


app = Flask("fever_prediction")


@app.route('/',methods = ['POST'])
def predict():
    details = request.get_json()


    with open('./model_files/fevermodel.bin','rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()

    predictions = fever_prediction(details,model)
    response = {
        'fever_prediction': list(predictions)
    }
    return jsonify(response)






if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1' , port =9696)