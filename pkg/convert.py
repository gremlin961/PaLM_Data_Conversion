import vertexai
from vertexai.language_models import TextGenerationModel
import json


def GetData(PARAMETERS, TEMPLATE, DATA):

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
	return response.text
