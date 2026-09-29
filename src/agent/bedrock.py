import json
import os

import boto3
from dotenv import load_dotenv


load_dotenv()


class BedrockClient:
    def __init__(self):
        self.region = os.getenv("AWS_REGION", "ap-south-1")
        self.model_id = os.getenv(
            "BEDROCK_MODEL_ID",
            "amazon.nova-2-lite-v1:0",
        )

        self.client = boto3.client(
            "bedrock-runtime",
            region_name=self.region,
        )

    def converse(self, prompt: str) -> str:
        response = self.client.converse(
            modelId=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ],
                }
            ],
        )

        return response["output"]["message"]["content"][0]["text"]

    def converse_json(self, prompt: str) -> dict:
        response = self.converse(prompt)

        return json.loads(response)