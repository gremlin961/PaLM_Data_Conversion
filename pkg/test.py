# This module accepts 3 json files and uses text-bison to convert supplied data to a standard json data structure
#
# The following modules are used in this service
# vertexai - Interacts with various GCP Vertex AI services, primarily the text-bison GenAI model
# SecurePrompt - Access prompt data from GCP Secret Manager
# json - Used to interact with json files and data passed to the web service

import vertexai
from vertexai.language_models import TextGenerationModel
from pkg import SecurePrompt 
import json


def runme():

    # Define the needed parameters provided in the parameters.json file.
    project_id = 'rkiles-demo-host-vpc'
    location = 'us-central1'
    model = 'text-bison'
    secret_id = 'secure_prompt-demo'
    secret_ver = 'latest'
    
    data = SecurePrompt.GetValue(project_id, secret_id, secret_ver)
    values = json.loads(data)

    return values['context']

#print(values['parameters']['candidateCount'])
#print(values['parameters']['tokenLimits'])
#print(values['parameters']['temperature'])
#print(values['parameters']['topP'])
#print(values['parameters']['topK'])
#print(values['parameters']['topK'])
#print(values['context'])
#print(values['testData'][0]['inputs'][0])