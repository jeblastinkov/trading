# MES Trading Advisor

AI-powered trading advisor for MES (Micro E-mini S&P 500) futures, tailored for a CET-based trader using AMP Futures.

## Quick Start

### Daily Battle Plan
Ask Claude for your daily execution plan:
```
/daily-battle-plan
```
This fetches live market data, economic calendar, and generates a full trading plan with bias, key levels, session strategies, and if/then scenarios.

### Trading Advisor
Get real-time trading advice during your session:
```
/trading-advisor
```
Then ask things like:
- "Should I trade right now?"
- "I want to go long at 5850 with a stop at 5846, good idea?"
- "I'm down $40 today, should I keep trading?"
- "Review my trade: short at 5860, stopped out at 5864"
- "What key levels should I watch for NY open?"

## Setup

| Parameter | Value |
|-----------|-------|
| Account | $1,100 |
| Broker | AMP Futures |
| Instrument | MES (Micro E-mini S&P 500) |
| Timezone | CET |
| Sessions | London AM (09:00-15:30) + NY PM (15:30-22:00) |
| Max contracts | 1 |
| Risk/trade | $22 (2%) |
| Max daily loss | $55 (5%) |
| Max trades/day | 4 |

Edit `config/trader-profile.yaml` to update these parameters as your account grows.

## Project Structure

```
knowledge/        Trading knowledge base (strategies, risk rules, sessions, etc.)
.claude/skills/   Claude Code skills (trading-advisor, daily-battle-plan)
config/           Trader profile and parameters
journal/          Daily trade journals and battle plans
```

## Knowledge Base

| File | Contents |
|------|----------|
| `knowledge/mes-contract.md` | MES specs, tick values, margins, roll calendar |
| `knowledge/sessions.md` | Session times in CET, volume patterns |
| `knowledge/risk-rules.md` | Position sizing, daily limits, scaling plan |
| `knowledge/strategies.md` | 4 core strategies with entry/exit rules |
| `knowledge/market-structure.md` | Key levels, market types, bias framework |
| `knowledge/trade-management.md` | Stop placement, targets, trailing stops |
| `knowledge/session-playbook.md` | London AM and NY PM specific playbooks |
| `knowledge/psychology.md` | 10 Commandments, emotional management |
| `knowledge/checklist.md` | Pre/during/post session checklists |

## Risk Warning

Trading futures involves substantial risk of loss and is not suitable for all investors. Past performance is not indicative of future results. This project provides educational tools and analysis — not financial advice. Trade at your own risk.
