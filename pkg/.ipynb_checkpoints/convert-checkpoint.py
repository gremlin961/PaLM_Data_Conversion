# This module accepts 3 json files and uses text-bison to convert supplied data to a standard json data structure
# GCP Secret Manager is used to securely store and manage prompts
#
# The following modules are used in this service
# vertexai - Interacts with various GCP Vertex AI services, primarily the text-bison GenAI model
# SecurePrompt - Access prompt data from GCP Secret Manager
# json - Used to interact with json files and data passed to the web service

import vertexai
from vertexai.language_models import TextGenerationModel
import SecurePrompt 
import json


# The GetData function uses paramerters provided by the user to interact with a backend GenAI model
def GetData(PARAMETERS, TEMPLATE, DATA):

    # Define the needed parameters provided in the parameters.json file.
    project_id = PARAMETERS['project_id']
    location = PARAMETERS['location']
    model = PARAMETERS['model']
    secret_id = PARAMETERS['secret_id']
    secret_ver = PARAMETERS['secret_ver']
    
    # Pull the prompt data and parameters from GCP Secret Manager
    data = SecurePrompt.GetValue(project_id, secret_id, secret_ver)
    values = json.loads(data)
    
    # Define the parameters from the returned data
    c_count = values['parameters']['candidateCount']
    max_output = values['parameters']['tokenLimits']
    temp = values['parameters']['temperature']
    top_p = values['parameters']['topP']
    top_k = values['parameters']['topK']
    context = values['context']
    prompt = values['testData'][0]['inputs'][0]


    # Initialize the vertex AI text-bison model with values set from the previous step
    # The context and prompt are provided in the parameters file. The template and data are provided in the template and data files.
    vertexai.init(project=project_id, location=location)
    parameters = {
        "candidate_count": c_count,
        "max_output_tokens": max_output,
        "temperature": temp,
        "top_p": top_p,
        "top_k": top_k
    }
    model = TextGenerationModel.from_pretrained(model)
    response = model.predict(
        """"""+context+
        """"""+json.dumps(TEMPLATE)+
        """input: """+prompt+
        """"""+json.dumps(DATA)+
        """output:
        """,
            **parameters
    )
    # Return the response from the model to main.py
    return response.text
