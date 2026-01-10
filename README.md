# Tools Portfolio

A collection of practical **Python tools** focused on **Identity & Access Management (IAM)** workflows, automation, debugging, and data comparison — built from real-world experience primarily with the **IBM Security Identity & Access Management** stack and **SailPoint IdentityIQ**, plus newer experiments with **Large Language Model APIs**.

This repository serves as a living portfolio showcasing clean, useful, production-oriented code I’ve written to solve actual IAM engineering problems — and my growing interest in applying AI/LLM techniques to security & identity challenges.

## Highlights

| Tool / Project                                 | Purpose                                                                 | Main Technologies                     | Status      |
|------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------|-------------|
| IAM Config Deployment Automation               | Safe, repeatable deployment of policy / config changes across envs     | Python, IBM APIs, YAML, diff/patch    | Active      |
| IAM Data Comparison & Reconciliation           | Compare user entitlements, roles, accounts between systems or snapshots| Python, Pandas, deepdiff, JSON/CSV    | Mature      |
| IAM Debug & Log Analysis Assistant             | Parse logs, simulate queries, find permission paths quickly            | Python, regex, IBM logging patterns   | Active      |
| Multi-LLM Debate & Cross-Verification Research | Two (or more) LLMs debate a topic and fact-check each other            | Python, OpenAI API / other LLM APIs   | Experimental|

## Why These Tools?

Most were born from repetitive, error-prone, or time-consuming tasks I encountered while working as an IAM engineer/developer:

- Manually comparing thousands of entitlements between prod and dev? → Automated diff with smart reporting
- Rolling out policy changes across environments? → Versioned configs + dry-run + rollback safety
- Chasing obscure access issues in logs? → Structured parsing + quick lookup
- Curious whether LLMs could help validate complex IAM policy decisions? → Early experiments with debate/verification loops

## Getting Started

```bash
git clone https://github.com/ghub-rwertheim/tools-portfolio.git
cd tools-portfolio

# Most tools use a virtual environment + recent Python (3.9+)
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
