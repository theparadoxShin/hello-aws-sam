# hello-aws-sam

A minimal AWS SAM (Serverless Application Model) project that deploys a Python AWS Lambda function behind an API Gateway endpoint.

## Overview

- Runtime: Python 3.11
- Handler: `app.lambda_handler`
- Endpoint: `GET /hello`
- Response: `{ "message": "Hello from Lambda!" }`

## Project structure

```
.
├─ app.py              # Lambda handler source
├─ template.yaml       # SAM/CloudFormation template
├─ README.md
└─ LICENSE
```

## Prerequisites

- AWS account and credentials configured (run `aws configure` if needed)
- AWS SAM CLI installed
- Docker Desktop (recommended for `sam local` emulation)

Verify your setup:

```powershell
sam --version
aws --version
```

## Quick start

1) Build the project

```powershell
sam build
```

2) Run locally (API Gateway emulation)

```powershell
sam local start-api
# The local API will listen on http://127.0.0.1:3000
```

Test the endpoint from PowerShell:

```powershell
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:3000/hello"
```

3) Deploy to AWS (guided on first run)

```powershell
sam deploy --guided
```

After deployment, SAM prints the stack outputs. You’ll see the function ARN and the API endpoint URL

4) Cleanup (remove all deployed resources)

```powershell
sam delete
```

## How it works

`template.yaml` defines a single `AWS::Serverless::Function` with an API event:

- `CodeUri: ./` points to the current folder containing `app.py`.
- `Runtime: python3.11` sets the Lambda runtime.
- The `Events` section creates an API Gateway route `GET /hello` wired to the function.
- Basic execution role policy is attached for logging to CloudWatch.

The handler in `app.py` returns a JSON body with status code 200. You can customize the payload there.