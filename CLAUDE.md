# MES Trading Advisor Project

This project is a trading advisor for MES (Micro E-mini S&P 500) futures.

## Project Structure
- `knowledge/` — Trading knowledge base (contract specs, strategies, risk rules, sessions, etc.)
- `config/trader-profile.yaml` — Personal trading parameters
- `.claude/skills/` — Claude Code skills for trading advice
- `journal/` — Daily trade journals and battle plans

## Key Context
- **Trader**: EU-based, CET timezone
- **Broker**: AMP Futures
- **Account**: $1,100
- **Instrument**: MES (Micro E-mini S&P 500)
- **Sessions**: London AM (09:00-15:30 CET) and NY PM (15:30-22:00 CET)
- **Max risk**: 1 contract, $22/trade (2%), $55/day (5%)
- **No overnight holds** (margin exceeds account)

## Available Skills
- `/trading-advisor` — General MES trading advice, trade review, risk checks
- `/daily-battle-plan` — Morning execution plan with bias, key levels, economic calendar

## Rules
- Always reference knowledge base files when giving trading advice
- Always enforce risk rules from `knowledge/risk-rules.md`
- All times should be in CET unless otherwise specified
- Never encourage the trader to exceed their risk limits
- If the trader reports approaching daily loss limit, tell them to STOP
