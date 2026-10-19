# SovernStack API Examples

Examples and scripts for automating AI infrastructure with the [SovernStack](https://www.sovernstack.com) API.

Use the API to manage your development environments and GPU resources programmatically, without having to perform every action manually through the dashboard.

**Full API documentation:** [docs.sovernstack.com](https://www.sovernstack.com/docs)

## What you can do

- **Launch Jupyter environments:** Provision environments for interactive development.
- **Launch SSH environments:** Work with your compute environment through your preferred tools.
- **Allocate GPU resources:** Configure VRAM allocations for your workloads.
- **Automate your workflow:** Trigger infrastructure operations from Python or any language that can make HTTP API requests.

## Getting started

### 1. Get your API key

Sign in to SovernStack and obtain an API key through the platform.

Keep your API key private. Never commit credentials to GitHub or include them in screenshots, logs, or public examples.

### 2. Clone this repository

```bash
git clone https://github.com/YOUR-ORG/sovernstack-api-examples.git
cd sovernstack-api-examples
```

Replace `YOUR-ORG` with the GitHub organization or username hosting this repository.

### 3. Configure your credentials

Store your API key in an environment variable rather than hardcoding it in your script.

```bash
export SOVERNSTACK_API_KEY="your-api-key"
```

For Windows PowerShell:

```powershell
$env:SOVERNSTACK_API_KEY="your-api-key"
```

### 4. Run an example

Choose an example from the repository and follow its instructions.

Each script should document its prerequisites, required parameters, and how to execute it.

For endpoint details, authentication requirements, request parameters, and response formats, refer to the [full SovernStack API documentation](https://www.sovernstack.com/docs).

> **Note:** API availability, supported operations, and required parameters depend on the current SovernStack API implementation.

## Examples

This repository can include examples for:

| Example | Description |
|---|---|
| Jupyter environment | Create and manage a Jupyter environment programmatically |
| SSH environment | Provision an environment accessible over SSH |
| GPU allocation | Request a specific VRAM allocation for a workload |
| Workflow automation | Combine infrastructure operations into a repeatable script |

Examples will be added as the API evolves.

## Using other programming languages

You are not limited to Python. Any language capable of making HTTP requests can integrate with the SovernStack API.

You can use the same API operations from JavaScript, Go, cURL, or your preferred development environment.

## Security

- Never commit API keys or other secrets.
- Use environment variables or a secrets manager for credentials.
- Avoid printing API keys in logs.
- Revoke and replace any key that has been exposed.

## Contributing

Found an issue or have an example you'd like to see? Open an issue or submit a pull request.

Contributions that make SovernStack easier to use, automate, and integrate into developer workflows are welcome.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.
