# This module accepts 3 json files and uses text-bison to convert supplied data to a standard json data structure
#
# The following modules are used in this service
# vertexai - Interacts with various GCP Vertex AI services, primarily the text-bison GenAI model
# json - Used to interact with json files and data passed to the web service

import vertexai
from vertexai.language_models import TextGenerationModel
import json


# The GetData function uses paramerters provided by the user to interact with a backend GenAI model
def GetData(PARAMETERS, TEMPLATE, DATA):

	# Define the needed parameters provided in the parameters.json file.
	project_id = PARAMETERS['project_id']
	location = PARAMETERS['location']
	model = PARAMETERS['model']
	c_count = PARAMETERS['parameters']['candidate_count']
	max_output = PARAMETERS['parameters']['max_output_tokens']
	temp = PARAMETERS['parameters']['temperature']
	top_p = PARAMETERS['parameters']['top_p']
	top_k = PARAMETERS['parameters']['top_k']
	context = PARAMETERS['context']
	prompt = PARAMETERS['prompt']


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
