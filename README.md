# JSON Data Converter using GenAI 
# Leverage GenAI to convert dissimilar json data files to a standard format


LLM’s provide application developers with the ability to augment and even replace large sections of their codebase with simple and intuitive prompts, which are natural-language queries that guides a model to produce a desired response. Instead of using numerous For loops, If blocks, and try-except statements, developers can harness LLM’s to produce a desired result simply by providing a level of context and a statement of the expected outcome.

In this example, a web service running FastAPI is provided a json template and a dissimilar JSON data file from a user. The service uses an LLM to return a json payload of the data file formatted in the json template.

This example uses the following files:
- Parameters file (./example_json_files/parameters.json) - Contains project specific attributes, such as the Project ID, region and GCP secret name/version for the prompt.
- Tempalte file (./example_json_files/template.json) - The desisried format that should be returned for the converted data json file.
- Source data file (./example_json_files/source_data.json) - An example data file that does not adhear to the desired format
- LLM prompt file (./example_json_files/Securte Prompt Secret.json) - The GenAI prompt that will be provided to the LLM. This example uses GCP's Secret Manager to security store and manage prompts as opposed to hard coding it in the application code.


# GCP Secret Manager

Developers can leverage existing services to ensure a high degree of security is applied to their LLM integrated applications. A vault or secrets management system such as GCP’s Secret Manager provides an ideal solution for application developers to use familiar tools to manage and control access to prompts for deployed services in the same way as their access keys and tokens. Secrets Manager can help ensure prompts are stored in a secure, immutable and encrypted environment only accessible to authorized services. Version control allows for easy updates and rollback for prompt configurations without the need to fully redeploy the application service. 

The "pkg" directory contains two python moduels. The module convert.py is called by main.py to interact with the LLM and return the correctly formatted JSON data. The convert.py module uses SecurePrompt.py to access the prompt information stored in GCP's Secret Manager.


# Summary

Large Lanquage Models can help application developers by replacing large sections of code with simple, natural-language prompts that guide the model to produce the desired result, reducing the need for complex coding (e.g., For loops, If blocks, try-except statements).
This example also leverages GCP Secret Manager to securely store and manage the LLM prompt, ensuring security and version control from outside the standard code base.

