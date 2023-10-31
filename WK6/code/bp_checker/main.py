from flask import escape
import functions_framework
import json

@functions_framework.http
def hello_http(request):

    # systolic, this is will be a number 
    # diastolic, this is also be a number 
    # idea: we will sum systolic + diastolic, to get some count 
    # if the count is above 120+80=200, so if > 200, return response
    # but also say that they are potentially pre-hypertensive 

    request_args = request.args

    if request_args and "systolic" in request_args:
        systolic_value = request_args["systolic"]
    else:
        systolic_value = 120

    if request_args and "diastolic" in request_args:
        diastolic_value = request_args["diastolic"]
    else:
        diastolic_value = 70

    # Step 1 convert everything to numbers 
    systolic_num = int(systolic_value)
    diastolic_num = int(diastolic_value)

    # Step 2 we now some them all together 
    bp_sum = systolic_num + diastolic_num 

    # Step 3 create a json object to return to the user 
    output = json.dumps(
        {
            "entered_systolic" : systolic_num, 
            "entered_diastolic": diastolic_num, 
            "bp_sum" : bp_sum
        }
    )

    return output


