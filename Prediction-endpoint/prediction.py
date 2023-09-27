import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "input1": [
      {
        "UDI": 1,
        "Product ID": "M14860",
        "Type": "M",
        "Air temperature [K]": 298.1,
        "Process temperature [K]": 308.6,
        "Rotational speed [rpm]": 1551,
        "Torque [Nm]": 42.8,
        "Tool wear [min]": 0,
        "Machine failure": 0,
        "TWF": 0,
        "HDF": 0,
        "PWF": 0,
        "OSF": 0,
        "RNF": 0
      },
      {
        "UDI": 2,
        "Product ID": "L47181",
        "Type": "L",
        "Air temperature [K]": 298.2,
        "Process temperature [K]": 308.7,
        "Rotational speed [rpm]": 1408,
        "Torque [Nm]": 46.3,
        "Tool wear [min]": 3,
        "Machine failure": 0,
        "TWF": 0,
        "HDF": 0,
        "PWF": 0,
        "OSF": 0,
        "RNF": 0
      },
      {
        "UDI": 3,
        "Product ID": "L47182",
        "Type": "L",
        "Air temperature [K]": 298.1,
        "Process temperature [K]": 308.5,
        "Rotational speed [rpm]": 1498,
        "Torque [Nm]": 49.4,
        "Tool wear [min]": 5,
        "Machine failure": 0,
        "TWF": 0,
        "HDF": 0,
        "PWF": 0,
        "OSF": 0,
        "RNF": 0
      },
      {
        "UDI": 4,
        "Product ID": "L47183",
        "Type": "L",
        "Air temperature [K]": 298.2,
        "Process temperature [K]": 308.6,
        "Rotational speed [rpm]": 1433,
        "Torque [Nm]": 39.5,
        "Tool wear [min]": 7,
        "Machine failure": 0,
        "TWF": 0,
        "HDF": 0,
        "PWF": 0,
        "OSF": 0,
        "RNF": 0
      },
      {
        "UDI": 5,
        "Product ID": "L47184",
        "Type": "L",
        "Air temperature [K]": 298.2,
        "Process temperature [K]": 308.7,
        "Rotational speed [rpm]": 1408,
        "Torque [Nm]": 40,
        "Tool wear [min]": 9,
        "Machine failure": 0,
        "TWF": 0,
        "HDF": 0,
        "PWF": 0,
        "OSF": 0,
        "RNF": 0
      }
    ]
  },
  "GlobalParameters": {}
}

body = str.encode(json.dumps(data))

url = 'http://82e7629e-ad1e-4d7c-b30d-2140c8758633.centralus.azurecontainer.io/score'
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = ''
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
