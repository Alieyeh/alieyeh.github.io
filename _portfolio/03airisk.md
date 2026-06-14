---
title: "AI Privacy Risk Assessment and Safe Model Release"
category: research
excerpt: "Technical and policy contribution to DARE UK work evaluating privacy attacks, model safeguards and release decisions for AI trained on sensitive health data."
collection: portfolio
permalink: /research/safe-ai
---

<br/><img src="/images/aisafe.jpg" alt="Safe AI project illustration">

## Overview

This work formed part of a DARE UK initiative on how AI models can be developed, tested and shared responsibly when they are trained on sensitive healthcare data.

I contributed both technical experiments and policy-oriented recommendations. The practical question was not only whether a model performed well, but whether it could be released without creating an unacceptable risk of revealing information about the people represented in its training data.

## Technical Contribution

- Developed and compared dementia classification models using Random Forest, Support Vector Machine, XGBoost and neural-network approaches.
- Built baseline and safer model variants using AI-SDC safe-model tooling, including `SafeSVC`, alongside neural-network safety experiments.
- Evaluated models trained with synthetic-data variants to examine the trade-off between predictive utility and disclosure risk.
- Prototyped a Concrete-ML route for homomorphic-encryption-compatible model inference. This was exploratory work rather than a deployed encrypted service.
- Used AI-SDC and the Adversarial Robustness Toolbox to test how model type, training data and safeguards affected privacy risk.

## Attack Evaluation

The assessment went beyond conventional model accuracy. I ran and compared:

- Membership inference attacks, including black-box and LiRA-style likelihood testing
- Worst-case and likelihood-based disclosure attacks
- Attribute inference experiments
- Structural disclosure-risk checks
- Custom query and feature-permutation attack experiments
- Selected adversarial robustness and reconstruction-oriented experiments

The experiments compared predictive measures such as accuracy, precision, recall, F1 and ROC-AUC with attack outcomes and release-risk reports. This helped demonstrate why a high-performing health model may still be unsafe to release directly.

## Policy and Governance Contribution

The technical findings informed wider recommendations for AI development and model release in Trusted Research Environments. I contributed to discussions of synthetic data, model disclosure testing, safer wrappers, secure access, controlled querying and the circumstances in which a model should remain inside a secure environment.

This work recognises both sides of the problem: sensitive health data needs strong protection, while research teams need practical routes to develop and evaluate useful models.

## Outputs

- DARE UK report: *Perspectives and Recommendations on the Development of Safe AI in Sensitive Healthcare Data*.
- Related workshop output: *Privacy in Synthetic Data Workshop Findings*.
- Technical repository: [github.com/Alieyeh/AI-Privacy-Risk-Assessment](https://github.com/Alieyeh/AI-Privacy-Risk-Assessment)

**Tags:** Python, scikit-learn, TensorFlow, XGBoost, AI-SDC, Adversarial Robustness Toolbox, synthetic data, homomorphic encryption, membership inference, privacy attacks, AI governance, Trusted Research Environments
