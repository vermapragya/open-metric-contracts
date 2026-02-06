⚠️ **Status:** Experimental (v0.1). Actively seeking feedback and real-world use cases.

# Open Metric Contracts

> Metrics are not numbers. They are promises.

**Open Metric Contracts** is a lightweight, opinionated specification for defining business metrics as *contracts* — explicit agreements between data producers, analytics teams, and business consumers.

This project introduces a simple, human-readable way to define what a metric **means**, **how it should be used**, and **what guarantees it provides** — before it ever appears in a dashboard or an AI system.

---

## Why This Exists

Most analytics failures are not caused by bad SQL.

They are caused by:
- Metrics that mean different things to different teams
- Dashboards that silently drift over time
- No clear ownership when numbers stop making sense
- Semantic layers that describe *how* to compute metrics, but not *what they promise*

When metrics are undocumented or ambiguous, trust erodes — and analytics teams are blamed for business confusion.

**Metric Contracts treat metrics like APIs**:
- Explicit definitions
- Clear ownership
- Declared assumptions
- Known limitations

---

## What Is a Metric Contract?

A Metric Contract is a declarative specification that defines:
- What a metric represents (business meaning)
- At what grain it is valid
- Who owns it
- What freshness and quality guarantees exist
- How it is expected to be consumed

It is **not** a SQL query.
It is **not** a dashboard.
It is the agreement that sits *above* both.

---

## Example

```yaml
name: monthly_active_users
description: Number of unique users who performed at least one qualifying action in a calendar month.
grain: user_id x month
owner: growth_analytics
source_tables:
  - events.user_activity
freshness_sla: 24h
dimensions:
  - platform
  - country
caveats:
  - Excludes users marked as internal_test_accounts
  - Backfills may change historical values
```

---

## Setup (Python)

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run validation against an example contract:

```bash
python cli.py examples/metrics.yaml
```
