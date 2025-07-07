import json
import boto3

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
prompt = "대전 시청이 있는 동은 어디야?"

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024, 
    "temperature": 0,
    "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt 
                        }
                    ]
                }
            ],
})

response = bedrock.invoke_model(body=body, modelId=bedrock_model_id)
response_body = json.loads(response.get('body').read())
results = response_body.get("content")[0].get("text")

print(results)