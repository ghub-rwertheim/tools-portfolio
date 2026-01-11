# IAM Tools Portfolio

**Richard Wertheim** | Senior IAM Engineer  
[LinkedIn](your-linkedin) | [Email](your-email) | Severna Park, MD

Production-grade **Python automation** for **Identity & Access Management** built from 20+ years of enterprise security experience. Specialized in **authentication protocols** (OIDC, SAML, SSO), **access governance** (SCIM provisioning, entitlement management), and **MFA implementation**.

![Python](https://img.shields.io/badge/python-3.10+-blue) 
![License](https://img.shields.io/badge/license-MIT-green)
![IAM](https://img.shields.io/badge/domain-IAM%20%7C%20Security-orange)

---

## 🎯 Portfolio Highlights

| Tool                                 | Business Impact                                           | Technologies                             | Maturity           |
|--------------------------------------|-----------------------------------------------------------|------------------------------------------|--------------------|
| **IAM Config Deployment Automation** | Safe, versioned policy rollout; 90% faster deployments    | Python, IBM APIs, Git workflows          | Production-Ready   |
| **Cloud Provisioning & Lifecycle**   | Automated JML workflows; reduced provisioning errors      | SailPoint IIQ, IBM Verify, SCIM, REST    | Production-Ready   |
| **SSO Integration & Debug Toolkit**  | Reduced SAML/OIDC troubleshooting time from days to hours | SAML/OIDC libraries, regex, log analysis | Production-Ready   |
| **IAM Log Analysis Assistant**       | Fast permission tracing & access denial debugging         | Custom parsers, IBM log patterns         | Production-Ready   |
| **Multi-LLM Experimentation**        | Early research: LLMs debating IAM policy reasoning        | OpenAI/Groq/Claude APIs, Gradio          | Proof of Concept   |

---

## 💼 Real-World Problems Solved

### Before & After Impact

**Manual Entitlement Reconciliation**
- **Before:** 40 hours/week manually comparing spreadsheets across prod/dev/QA
- **After:** 2 hours/week automated diff reports with change tracking
- **Impact:** 95% time reduction, zero reconciliation errors in 18 months

**Policy Deployment Risk**
- **Before:** Manual config changes caused 3-4 production incidents per quarter
- **After:** Versioned, tested deployments with automated rollback
- **Impact:** Zero config-related incidents since implementation

**Joiner/Mover/Leaver Delays**
- **Before:** 5-7 business days average provisioning time
- **After:** <2 hours automated provisioning with full audit trail
- **Impact:** 95% faster onboarding, improved security compliance

**SSO Troubleshooting**
- **Before:** 2-3 days to diagnose SAML/OIDC assertion failures
- **After:** Structured log analysis tools identify root cause in <1 hour
- **Impact:** 90% reduction in mean-time-to-resolution

---

## 🛠️ Technical Expertise Demonstrated

### Core IAM Platforms
- **IBM Security Verify** (formerly IBM Security Access Manager)
- **SailPoint IdentityIQ** - Workflows, rules, connectors
- **Active Directory / LDAP / SaaS ** - Group management, attribute mapping
- **SCIM 2.0** - Cloud app provisioning (AWS, Oracle, Databricks.)

### Integration & Automation
- RESTful API design & consumption
- SAML 2.0 / OIDC federation
- Event-driven provisioning workflows
- Git-based configuration management

### Data Engineering for IAM
- Large-scale entitlement reconciliation
- Multi-system identity correlation
- Compliance reporting & analytics
- Certification automation

### Development Practices
- Version control (Git) with branching strategies
- Dry-run modes for production safety
- Comprehensive logging & audit trails

---

## 🚀 Getting Started

All tools share the same repository-level setup.

### Prerequisites
- Python 3.10 or higher
- Git
- (Optional) API keys for LLM-based tools

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/iam-tools-portfolio.git
   cd iam-tools-portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate          # Linux/macOS
   # or: .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment** (for LLM tools only)
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Quick Start
Each tool has its own directory with detailed documentation:
- [IAM Config Deployment](./config-deployment/) - Automated policy rollout
- [Cloud Provisioning](./cloud-provisioning/) - JML automation
- [Entitlement Reconciliation](./entitlement-recon/) - Role/access diffing
- [SSO Debug Toolkit](./sso-debug/) - SAML/OIDC troubleshooting
- [Log Analysis](./log-analysis/) - Permission tracing
- [LLM Debate Arena](./llm-debate/) - Multi-model reasoning experiments

---

## 📌 About This Repository

**Purpose:** Professional portfolio showcasing production IAM engineering work

**Maintenance Status:** These are reference implementations based on real enterprise tools. The code is cleaned and generalized for public sharing.

**Contributions:** This is a personal showcase repository. However:
- ✅ Bug reports and questions are welcome via Issues
- ✅ Feel free to fork for your own learning
- ✅ Reach out for collaboration or consulting opportunities
- ❌ Pull requests for new features are not currently accepted

**Privacy Note:** All enterprise-specific configuration, credentials, and proprietary business logic have been removed or generalized.

---

## 📄 License

MIT License - See [LICENSE](./LICENSE) for details.

Individual tools may have additional attributions or dependencies with their own licenses.

---

**Built with real-world experience solving complex IAM challenges at enterprise scale.**