import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "XsUSy5q2FTAto1GV_GO3H8-K1Mo5eL3VXC4AS96Z2nbU"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["layer_height","wall_thickness","infill_density","G1","nozzle_temperature","bed_temperature","print_speed","fan_speed","roughness","tension_strenght","elongation"], "values": [[0.7, 0., 0.4, 0. , 0.4 ,0. , 1.  , 0., 0.2, 0.3, 0.3]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7a01f8dd-4f12-4b56-a04a-c7f360ca052e/predictions?version=2021-10-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
print("Final Prediction:")
print(predictions['predictions'][0]['values'][0][0])
#print(prediction)
if(predictions==0):
    print("ABS")
elif(predictions==1):
    print("PLA")
else:
    print("Invalid Input")