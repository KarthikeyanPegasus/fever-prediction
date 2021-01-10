import pickle
import json
import ast
from flask import Flask, request, jsonify
from model_files.ml_model import fever_prediction


app = Flask("fever_prediction")


@app.route('/',methods = ['POST'])
def predict():
    detai =  (request.get_json())
    print(detai)
    de=json.dumps(detai)
    print(de)
    detail = json.loads(de)
    print(detail)
    deta= detail["list"]
    print(deta)
    details = ast.literal_eval(deta)
    print(details,type(details))

    fevers = []
    pulses = []
    sugars = []
    doses = []

    fevers.append(details[0])
    fevers.append(details[1])

    pulses.append(details[2])
    pulses.append(details[3])

    sugars.append(details[4])
    sugars.append(details[5])

    doses.append(details[6])
    doses.append(details[7])

    fever = list([fevers])
    pulse = list([pulses])
    sugar = list([sugars])
    dose = list([doses])


    with open('./model_files/fevermodel.bin','rb') as f_in:
        fevermodel = pickle.load(f_in)
        f_in.close()
    with open('./model_files/pulsemodel.bin','rb') as f_in:
        pulsemodel = pickle.load(f_in)
        f_in.close()
    with open('./model_files/sugarmodel.bin','rb') as f_in:
        sugarmodel = pickle.load(f_in)
        f_in.close()
    with open('./model_files/dosagemodel.bin','rb') as f_in:
        dosagemodel = pickle.load(f_in)
        f_in.close()

    fe_predictions = fever_prediction(fever,fevermodel)
    pul_predictions = fever_prediction(pulse,pulsemodel)
    suga_predictions = fever_prediction(sugar,sugarmodel)
    dose_predictions = fever_prediction(dose,dosagemodel)
    response = {
        'fever_prediction': list(fe_predictions),
        'pulse_prediction': list(pul_predictions),
        'sugar_prediction': list(suga_predictions),
        'dosage_prediction': list(dose_predictions)

    }
    return jsonify(response)






if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1' , port =9696)
