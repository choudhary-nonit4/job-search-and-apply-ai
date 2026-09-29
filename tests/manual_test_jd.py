from src.agent.bedrock import BedrockClient
from src.agent.jd_analyzer import JobDescriptionAnalyzer


jd = """
Senior AWS Cloud Engineer

We are looking for a Senior AWS Cloud Engineer with 8+ years
of experience.

Requirements:
- Strong AWS experience
- AWS Lambda
- Terraform
- Python
- Kubernetes
- Docker
- CI/CD
- Experience with REST APIs

Location: Gurugram / Noida

Responsibilities:
- Design and develop cloud-native applications.
- Build serverless applications using AWS Lambda.
- Implement infrastructure using Terraform.
- Work with engineering teams on cloud modernization.
"""


def main():
    client = BedrockClient()

    analyzer = JobDescriptionAnalyzer(client)

    result = analyzer.analyze(jd)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()