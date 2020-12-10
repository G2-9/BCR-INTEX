from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def indexPageView(request) :
    return render(request, 'recommender/index.html')

def azure_recommender(request) :
    from urllib import request as r

    # If you are using Python 3+, import urllib instead of urllib2
    import json
    data =  {
            "Inputs": {
                    "input":
                    {
                        "ColumnNames": ["user_id", "job_title", "matching_skills"],
                        "Values": [ request.GET['user_id'], request.GET['job_title'], request.GET['matching_skills']]
                    },
            }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/c8c25a0a72b94385b6e2c405efd13304/services/f404c124114445b9b01c1f27c1e82054/execute?api-version=2.0&details=true'
    api_key = 'RkaPucwFOUZhZNnM1L/KvF9bbnwdS/u0RMpZ5JG0F6qINAJ14uAfbupwmK6FFAu2LaPtDkHfwu4mwaXT6lLqhw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    #Generate web service request
    req = r.Request(url, body, headers)

    #Open/request/call the web service
    response = r.urlopen(req)

    #Read the response into an object
    result = response.read()

    #Cast response to json
    result = json.loads(result)
    prediction = str(result['Results']['output']['value']['Values'][0][0])
    prediction = prediction + ', ' + str(result['Results']['output']['value']['Values'][0][1])
    prediction = prediction + ', ' + str(result['Results']['output']['value']['Values'][0][2])
    data = {'azure_job':str(prediction)}

    return render(request, 'recommender/index.html', data)