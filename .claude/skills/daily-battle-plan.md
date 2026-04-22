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

Run all fetches in parallel for speed. If any WebFetch returns an error, fall back to the WebSearch alternative listed.

#### 1A — ES Futures Price (primary data — use these numbers for all key levels)
WebFetch `https://finance.yahoo.com/quote/ES=F/`
- Extract: current price, previous close (= futures PDC), day range high/low (= ONH/ONL), open, volume
- **This gives exact MES/ES futures levels — do not estimate from SPX cash + carry premium**
- Fallback: WebSearch `"ES futures" "S&P 500 futures" price high low close [current date]`

#### 1B — Economic Calendar (structured events, exact times)
WebFetch `https://www.investing.com/economic-calendar/`
- Extract all US events for today with: time (convert to CET), event name, impact (High/Medium/Low), forecast, previous
- Filter: only keep High and Medium impact events — discard Low
- **This replaces the generic WebSearch for economic calendar and gives precise times**
- Fallback: WebSearch `"economic calendar" [current date] US "high impact" data releases CET`

#### 1C — Overnight News & Market Context
WebFetch `https://feeds.content.dowjones.io/public/rss/mw_marketpulse` — quick price data points and market moves
WebFetch `https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines` — breaking market news in chronological order
- Extract: any overnight/pre-market moves, geopolitical events, earnings reactions, Fed commentary
- Fallback: WebSearch `"stock market news" [current date]` and `"S&P 500 futures overnight" [current date]`

#### 1D — Commodities Context (conditional)
Only fetch if oil, gold, or a commodity is a macro driver today (geopolitical tension, OPEC, inflation data):
WebFetch `https://www.investing.com/rss/commodities_Fundamental.rss`
- Extract: key oil/gold developments affecting equity market sentiment

#### 1E — FOMC Context (conditional — only if FOMC meeting is within 7 days)
Check if FOMC is within 7 days. If yes:
WebFetch `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm` to confirm the meeting date
WebSearch `Federal Reserve FOMC statement [most recent meeting date] full text key phrases`
- Extract: rate decision, key language on inflation, labor market, and forward guidance
- Note the tone (hawkish / dovish / neutral) — this sets the context for any surprise at the upcoming meeting
- Add a "FOMC Watch" line to the Economic Calendar section of the plan

#### 1F — COT Positioning (conditional — only on Mondays)
Only on Mondays, add institutional positioning context for the week:
WebSearch `CFTC "S&P 500" COT commitments traders "leveraged funds" net position latest`
- Extract: net long/short position of Leveraged Funds (hedge funds/CTAs) on S&P 500 futures
- Note whether positioning is extreme (crowded long = squeeze risk, crowded short = squeeze potential)
- Add one sentence to the "Broader Context" line in the plan

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
- **Current Price**: ___ ES / ~___ MES (as of ___ CET) | Volume: ___
- **Gap**: +/-___ pts from PDC / No gap
- **Broader Context**: [1-2 sentences on weekly/trend context. On Mondays add: COT — Leveraged Funds net [long/short] [X]K contracts ([extreme/normal/crowded])]

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

| Time (CET) | Event | Impact | Forecast | Previous | Action |
|------------|-------|--------|----------|----------|--------|
| ___ | ___ | High/Medium/Low | ___ | ___ | Trade normally / Avoid 5 min / No new trades until after |

[If FOMC within 7 days, add:]
> **FOMC Watch** — Meeting [date]. Prior statement tone: [hawkish/dovish/neutral]. Key phrase to watch: "[quote]". A surprise [hike/cut/hold] or language shift would [expected market reaction].

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

### Data Quality Rules
- **Always use ES=F Yahoo Finance data for key levels** — never estimate MES levels by adding a carry premium to SPX cash; get the real futures price
- If Yahoo Finance ES=F fetch fails, note it clearly and use cash SPX + estimated carry (label all such estimates)
- The economic calendar must come from Investing.com or a structured source — not a generic web search; include Forecast and Previous values
- All times must be in CET. The Investing.com calendar defaults to browser timezone — explicitly extract and convert to CET

### Day-Type Rules
- If it's a weekend or US market holiday, say so and don't generate a trading plan
- If markets are closed, note the next open time
- Wednesday: note whether it's an FOMC day (check the calendar). Even non-FOMC Wednesdays can be range-bound pre-announcement
- Thursday: always check for Initial Jobless Claims at 14:30 CET
- Friday first of month: check for NFP at 14:30 CET

### Conditional Steps Reminder
- **FOMC within 7 days** → run Step 1E, add FOMC Watch block to Economic Calendar
- **Monday** → run Step 1F, add COT sentence to Broader Context
- **Oil/gold driving the market** → run Step 1D, add commodity context to Market Context

### Output Rules
- Be specific with prices — use actual levels from research, not placeholders
- If you cannot find a specific level, say so explicitly rather than leaving a blank or inventing a number
- Always include the risk disclaimer
