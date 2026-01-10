# Tools Portfolio

Practical **Python-based IAM tools** — built for real-world **Identity & Access Management** challenges in enterprise environments.

Primarily focused on the **IBM Security IAM stack** and **SailPoint IdentityIQ**, with strong experience in **cloud provisioning**, **single sign-on (SSO)** federation, automated workflows, debugging, and data reconciliation — plus emerging experiments applying **Large Language Models** to security & identity problems.

This repository is my living portfolio: production-grade, clean, and useful code that solves actual engineering pain points while showcasing my evolution toward AI-assisted IAM solutions.

## Highlights

| Tool / Project                               | Purpose                                                                 | Main Technologies                          | Status      |
|----------------------------------------------|-------------------------------------------------------------------------|--------------------------------------------|-------------|
| IAM Config Deployment Automation             | Safe, repeatable, versioned deployment of policies/configs across envs | Python, IBM APIs, YAML, diff/patch, dry-run| Active      |
| Cloud Provisioning & Lifecycle Automation    | Automated joiner/mover/leaver, SCIM, account provisioning/deprovisioning | Python, SailPoint APIs, IBM Verify, REST   | Active      |
| Entitlement Comparison & Reconciliation      | Diff user roles, accounts, entitlements between systems or snapshots   | Python, Pandas, deepdiff, JSON/CSV         | Mature      |
| SSO Integration & Troubleshooting            | Federation setup, SAML/OIDC flow testing, SSO debug & validation       | Python, regex, SAML libraries, logging     | Active      |
| IAM Debug & Log Analysis Assistant           | Fast log parsing, query simulation, permission path tracing            | Python, regex, IBM logging patterns        | Active      |
| Multi-LLM Debate & Verification Research     | Multiple LLMs debate topics, cross-check facts, potential for policy QA| Python, OpenAI / other LLM APIs            | Experimental|

## Why These Tools?

They come directly from the repetitive, high-stakes, or tedious tasks I've tackled as an **IAM Architect and Engineer**:

- Manually reconciling thousands of entitlements across prod/dev/cloud? → Smart, automated diff + reconciliation reports  
- Safely rolling out policy changes across dozens of environments? → Versioned configs, dry-run, rollback safety  
- Onboarding/offboarding users in hybrid cloud setups? → Automated provisioning/deprovisioning with audit trails  
- Debugging SSO failures or obscure access denials? → Structured log analysis + quick lookup tools  
- Wondering if LLMs could reason about complex IAM policies? → Early multi-model debate & verification experiments

## Getting Started

```bash
git clone https://github.com/ghub-rwertheim/tools-portfolio.git
cd tools-portfolio

# Use the shared virtual environment (Python 3.9+ recommended)
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# or .venv\Scripts\activate        # Windows

pip install -r requirements.txt
