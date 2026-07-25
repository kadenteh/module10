# import json
# import requests
# from flask import Flask
#
# # API endpoint URL's and access keys
# WMATA_API_KEY = "e553f54f992f4a9f95de547b8ffee915"
# INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
# headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}
#
# ################################################################################
#
# app = Flask(__name__)
#
# # get incidents by machine type (elevators/escalators)
# # field is called "unit_type" in WMATA API response
# @app.route("/incidents/<unit_type>", methods=["GET"])
# def get_incidents(unit_type):
#   # create an empty list called 'incidents'
#
#   # use 'requests' to do a GET request to the WMATA Incidents API
#   # retrieve the JSON from the response
#
#   # iterate through the JSON response and retrieve all incidents matching 'unit_type'
#   # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
#   #   -StationCode, StationName, UnitType, UnitName
#   # add each incident dictionary object to the 'incidents' list
#
#   # return the list of incident dictionaries using json.dumps()
#
# if __name__ == '__main__':
# #     app.run(debug=True)
# #==============================================================================================================

# import json
# import requests
# from flask import Flask

# # API endpoint URL's and access keys
# WMATA_API_KEY = "e553f54f992f4a9f95de547b8ffee915"
# INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
# headers = {"api_key": WMATA_API_KEY, "Accept": "*/*"}

# ################################################################################

# app = Flask(__name__)

# # get incidents by machine type (elevators/escalators)
# # field is called "UnitType" in WMATA API response
# @app.route("/incidents/<unit_type>", methods=["GET"])
# def get_incidents(unit_type):

#     # create an empty list called 'incidents'
#     incidents = []

#     # use 'requests' to do a GET request to the WMATA Incidents API
#     # retrieve the JSON from the response
#     response = requests.get(INCIDENTS_URL, headers=headers)
#     response_json = response.json()

# #     # iterate through the JSON response and retrieve all incidents matching 'unit_type'
# #     for incident in response_json["ElevatorIncidents"]:

# #         if incident["UnitType"].lower() == unit_type.lower():

# #             # create a dictionary containing the 4 required fields
# #             incident_dict = {
# #                 "StationCode": incident["StationCode"],
# #                 "StationName": incident["StationName"],
# #                 "UnitType": incident["UnitType"],
# #                 "UnitName": incident["UnitName"]
# #             }

# #             # add each incident dictionary object to the incidents list
# #             incidents.append(incident_dict)

# #     # return the list of incident dictionaries using json.dumps()
# #     return json.dumps(incidents)


# # if __name__ == '__main__':
# #     app.run(debug=True)
    
    
# #================================================================================================


# import json
# import requests
# from flask import Flask

# # API endpoint URL and access key
# WMATA_API_KEY = "YOUR_WMATA_API_KEY"

# INCIDENTS_URL = (
#     "https://api.wmata.com/"
#     "Incidents.svc/json/ElevatorIncidents"
# )

# headers = {
#     "api_key": WMATA_API_KEY,
#     "Accept": "*/*"
# }

# ################################################################################

# app = Flask(__name__)


# # Home route
# @app.route("/", methods=["GET"])
# def home():
#     return "WMATA Incident API is running."


# # Get incidents by machine type: elevators or escalators
# @app.route("/incidents/<unit_type>", methods=["GET"])
# def get_incidents(unit_type):

#     # Create an empty list called incidents.
#     incidents = []

#     # Convert the URL value to uppercase.
#     requested_unit_type = unit_type.upper()

#     # Convert plural URL values to WMATA's singular UnitType values.
#     if requested_unit_type == "ELEVATORS":
#         requested_unit_type = "ELEVATOR"

#     if requested_unit_type == "ESCALATORS":
#         requested_unit_type = "ESCALATOR"

#     # Send a GET request to the WMATA API.
#     response = requests.get(
#         INCIDENTS_URL,
#         headers=headers
#     )

#     # Retrieve JSON from the response.
#     response_json = response.json()

#     # Iterate through all incidents returned by WMATA.
#     for incident in response_json["ElevatorIncidents"]:

#         # Select incidents that match the requested unit type.
#         if incident["UnitType"] == requested_unit_type:

#             incident_dictionary = {
#                 "StationCode": incident["StationCode"],
#                 "StationName": incident["StationName"],
#                 "UnitType": incident["UnitType"],
#                 "UnitName": incident["UnitName"]
#             }

#             incidents.append(incident_dictionary)

#     # Return the list as JSON text.
#     return json.dumps(incidents)


# if __name__ == "__main__":
#     app.run(debug=True)

#==================================================================================================

import json
import requests
from flask import Flask

# API endpoint URL and access key
WMATA_API_KEY = "86ecf7bdff2e4f3cb2bcd3bbd7af11b6"     #"YOUR_WMATA_API_KEY"

INCIDENTS_URL = (
    "https://api.wmata.com/"
    "Incidents.svc/json/ElevatorIncidents"
)

headers = {
    "api_key": WMATA_API_KEY,
    "Accept": "application/json"
}

################################################################################

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "WMATA Incident API is running."


@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):

    incidents = []

    requested_unit_type = unit_type.upper()

    if requested_unit_type == "ELEVATORS":
        requested_unit_type = "ELEVATOR"

    if requested_unit_type == "ESCALATORS":
        requested_unit_type = "ESCALATOR"

    response = requests.get(
        INCIDENTS_URL,
        headers=headers
    )

    response_json = response.json()

    # Display the actual WMATA response in the terminal.
    print("HTTP status code:", response.status_code)
    print("WMATA response:", response_json)

    # Check whether WMATA returned the expected field.
    if "ElevatorIncidents" not in response_json:
        return json.dumps(
            {
                "error": "WMATA did not return ElevatorIncidents",
                "status_code": response.status_code,
                "wmata_response": response_json
            }
        ), response.status_code

    for incident in response_json["ElevatorIncidents"]:

        if incident["UnitType"] == requested_unit_type:

            incident_dictionary = {
                "StationCode": incident["StationCode"],
                "StationName": incident["StationName"],
                "UnitType": incident["UnitType"],
                "UnitName": incident["UnitName"]
            }

            incidents.append(incident_dictionary)

    return json.dumps(incidents)


if __name__ == "__main__":
    app.run(debug=True)









