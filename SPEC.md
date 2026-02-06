# Design Principles

**Clarity over completeness**: A partial but explicit definition is better than a perfect but implicit one.

**Business-first**: Contracts describe meaning, not implementation details.

**Lightweight by default**: No heavy governance, no required tooling.

**Composable**: Works alongside dbt, semantic layers, dashboards, and LLMs.


## What This Is (and Is Not)

### ✅ This is:
- A shared language for metrics
- A documentation and governance primitive
- A foundation for AI-ready analytics systems

### ❌ This is not:
- A replacement for dbt
- A metrics store
- A BI tool
- A silver bullet for bad data culture


## Intended Users
- Analytics Engineers
- Data Engineers working close to analytics
- Analytics Leaders who want consistency without bureaucracy
- Teams building AI systems on top of business metrics


### Project Status
- Spec version: v0.1
- Stability: Experimental
- Feedback: Actively encouraged

This project is intentionally small and opinionated.
The goal is to start a conversation — not to declare a final standard.

### Roadmap (Early)
Schema validation tooling
dbt integration examples
Metric lineage & dependency metadata
Community-driven extensions

### Contributing
Contributions are welcome — especially:
- Spec improvements
- Real-world metric examples
- Design critiques

If you’ve ever argued about what a metric “really means”, your feedback is valuable.