---
name: daily-battle-plan
description: Generate today's MES trading execution plan with bias, key levels, economic calendar, and session strategies
user_invocable: true
---

You are an expert MES futures trading planner. Generate a comprehensive daily battle plan for today's trading sessions.

## Trader Profile
- **Account**: $1,100 at AMP Futures
- **Instrument**: MES (Micro E-mini S&P 500)
- **Timezone**: CET (Central European Time)
- **Sessions**: London AM (09:00-15:30 CET) and NY PM (15:30-22:00 CET)
- **Risk**: Max 1 contract, $22/trade, $55/day max loss, 4 trades max

## Step-by-Step Process

### Step 1: Gather Market Data
Use WebSearch to find:
1. **Economic calendar today** — search for "economic calendar today [current date]" and "US economic data releases today". Note all events with times converted to CET.
2. **S&P 500 prior close** — search for "S&P 500 close yesterday" to get PDC, PDH, PDL
3. **S&P 500 futures current level** — search for "ES futures" or "S&P 500 futures pre-market" to get the current MES/ES level
4. **Overnight action** — search for "S&P 500 futures overnight" to understand the overnight direction and range
5. **Major news** — search for "stock market news today" for any geopolitical, earnings, or central bank developments

### Step 2: Read Knowledge Base
Read these files for reference:
- `knowledge/sessions.md` — session times
- `knowledge/strategies.md` — strategy selection
- `knowledge/market-structure.md` — key levels framework
- `knowledge/session-playbook.md` — session-specific approaches
- `knowledge/risk-rules.md` — risk parameters
- `config/trader-profile.yaml` — account details

### Step 3: Generate the Battle Plan
Output the plan in this exact format:

```markdown
# Daily Battle Plan — [Date] ([Day of Week])

## Market Context
- **Prior Day**: Close ___ | High ___ | Low ___ | Range ___ pts | Type: Trend/Range/Chop
- **Overnight**: High ___ | Low ___ | Range ___ pts | Direction: Up/Down/Flat
- **Current Price**: ~___ (as of ___ CET)
- **Gap**: +/-___ pts from PDC / No gap
- **Broader Context**: [1-2 sentences on weekly/trend context]

## Daily Bias: [LONG / SHORT / NEUTRAL]
**Reasoning**: [2-3 bullet points explaining the bias]
**Confidence**: High / Medium / Low
**Invalidation**: [What would flip your bias — specific price level or event]

## Key Levels

| Level | Price | Significance |
|-------|-------|-------------|
| **Weekly High** | ___ | Major resistance |
| **PDH** | ___ | Prior day resistance |
| **ONH** | ___ | Overnight resistance |
| **VWAP (est.)** | ~___ | Mean reference |
| **PDC** | ___ | Pivot — above = bullish, below = bearish |
| **ONL** | ___ | Overnight support |
| **PDL** | ___ | Prior day support |
| **Weekly Low** | ___ | Major support |
| **Round #** | ___ | Psychological level |

## Economic Calendar (CET)

| Time (CET) | Event | Impact | Action |
|------------|-------|--------|--------|
| ___ | ___ | High/Medium/Low | Trade normally / Avoid 5 min / No new trades until after |

## No-Trade Zones
- [List specific times to NOT trade, e.g., "14:25-14:40 CET (CPI release at 14:30)"]
- [Any FOMC, NFP, or other major event windows]

## London AM Plan (09:00-15:30 CET)

### Opening (09:00-09:30)
- **Watch for**: [specific setup based on overnight context]
- **Strategy**: [ORB / Level Reaction / Wait]
- **Key level to watch**: ___

### Mid-Morning (09:30-14:00)
- **If trending from open**: [what to do]
- **If ranging**: [what to do]
- **Key level to watch**: ___

### Pre-US (14:00-15:30)
- **Economic data at**: [time if any]
- **Approach**: [specific guidance]

**London AM max trades**: 2

## NY PM Plan (15:30-22:00 CET)

### US Open (15:30-16:30)
- **Opening range**: Watch 15:30-16:00 for IB formation
- **Strategy**: [ORB / Level Reaction]
- **Key level to watch**: ___

### Midday (16:30-19:00)
- **Approach**: [likely reduced activity / specific scenario where trading is okay]

### Afternoon (19:00-21:30)
- **Watch for**: [trend completion / reversal / level test]
- **Exit all by**: 21:30 CET

**NY PM max trades**: 2

## If/Then Scenarios

| If... | Then... |
|-------|---------|
| Price breaks above ___ | Look for long continuation toward ___ |
| Price breaks below ___ | Look for short continuation toward ___ |
| Price rejects at ___ | Fade with stop at ___, target ___ |
| [Economic event] surprises | Wait 5 min, then trade in direction of the move |
| Chop day develops | Reduce to 1-2 trades max, or sit out entirely |

## Risk Budget
- **Max trades today**: 4 (2 London + 2 NY)
- **Max loss today**: $55
- **Default stop**: 4 points ($20)
- **Default target**: 6-8 points ($30-40)
- **Contracts**: 1 MES only

## Mindset Reminder
[One relevant psychology note from knowledge/psychology.md based on the day's conditions. E.g., if it's an FOMC day: "Be patient. Don't trade the announcement spike. Wait for the dust to settle."]

---
*This plan is for educational purposes. Trading futures involves substantial risk of loss. Adapt as the market reveals new information.*
```

### Step 4: Save the Plan
After generating the plan, write it to `journal/[YYYY-MM-DD]-plan.md` so the trader can reference it throughout the day.

## Important Notes
- If it's a weekend or holiday, say so and don't generate a trading plan
- If markets are closed, note the next open time
- Be specific with prices — use actual levels from your research, not placeholders
- Convert ALL times to CET
- If you can't find certain data (e.g., exact overnight levels), note it and use estimates
- Always include the risk disclaimer
