import json

from .bedrock import BedrockClient
from .models import JobDescription


SYSTEM_INSTRUCTIONS = """
You are a Job Description Analysis Agent.

Your job is to extract structured information from a job description.

Do not invent information.

If information is not explicitly available in the job description,
return null or an empty list.

Return ONLY valid JSON.

The JSON must follow this structure:

{
  "role_title": "string",
  "company": "string or null",
  "experience_min_years": "integer or null",
  "experience_max_years": "integer or null",
  "location": [],
  "must_have_skills": [],
  "good_to_have_skills": [],
  "responsibilities": [],
  "education_requirements": [],
  "employment_type": "string or null",
  "raw_text": "original job description"
}
"""


class JobDescriptionAnalyzer:

    def __init__(self, bedrock_client: BedrockClient):
        self.bedrock = bedrock_client

    def analyze(self, jd_text: str) -> JobDescription:

        prompt = f"""
{SYSTEM_INSTRUCTIONS}

JOB DESCRIPTION:

{jd_text}
"""

        response = self.bedrock.converse(prompt)

        data = json.loads(response)

        return JobDescription(**data)