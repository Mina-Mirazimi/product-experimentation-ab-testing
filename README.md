# Product Experimentation: Should We Launch a New Rewards Feature?

End-to-end A/B testing project evaluating whether a new rewards feature improves conversion, engagement, and revenue without harming guardrail metrics.

## Business Question
> **Should the company launch the rewards feature to all users?**

Users are randomly assigned to Control or Treatment. The analysis covers experiment validity, causal effects, variance adjustment, heterogeneity, guardrails, and a ship/no-ship recommendation.

## Primary Metric
- Purchase conversion rate

## Secondary Metrics
- Orders per user
- Revenue per user
- 7-day engagement

## Guardrails
- Refund rate
- Support-contact rate

## Methods
Randomized experiments • SRM checks • Confidence intervals • CUPED-style covariate adjustment • Heterogeneous treatment effects • Product decision-making • Python • SQL

## Structure
```text
├── README.md
├── requirements.txt
├── src/
├── notebooks/
├── sql/
├── tests/
└── results/
```

This independent portfolio project uses fully synthetic data and contains no proprietary company data.
