import json
import joblib

MODEL_NAME = "model_1553724836.6208675.joblib"
model = joblib.load(MODEL_NAME)

def predict(event, context):
    body = {"message": "OK"}

    params = event.get("queryStringParameters")
    if params:
        medInc = float(params["medInc"]) / 100000
        houseAge = float(params["houseAge"])
        aveRooms = float(params["aveRooms"])
        aveBedrms = float(params["aveBedrms"])
        population = float(params["population"])
        aveOccup = float(params["aveOccup"])
        latitude = float(params["latitude"])
        longitude = float(params["longitude"])

        input_vector = [[
            medInc, houseAge, aveRooms, aveBedrms,
            population, aveOccup, latitude, longitude
        ]]

        predicted_price = round(float(model.predict(input_vector)[0]) * 100000, 2)
        body["predictedPrice"] = predicted_price
    else:
        body["message"] = "queryStringParameters not in event."

    return {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
