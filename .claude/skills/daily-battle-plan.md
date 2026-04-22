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
Output the plan in this exact format — concise, scannable, no fluff:

```markdown
# Battle Plan — [Day] [Date]

## Bias: [BULLISH / BEARISH / NEUTRAL] | Confidence: [High / Medium / Low]
[2-3 sentences max: what's driving the market today, what the overnight/gap tells you, and the one price level that invalidates the bias.]

---

## Key Levels (MES)
[Use 🔴 for resistance, 🟢 for support, ⚡ for the pivot. Mark levels as (likely reached), (possible), or (ceiling/floor) based on the day's context and range.]

🔴 ___ — [Label] ([likely reached / ceiling])
🔴 ___ — [Label] ([possible])
🔴 ___ — [Label] ([possible])
──────────────────────────────
⚡ ___ — [PDC / key pivot] ← PIVOT. [Above = bullish / Below = bearish]
──────────────────────────────
🟢 ___ — [Label] ([possible])
🟢 ___ — [Label] ([likely reached / floor])

Likely range today: ___ – ___

---

## News Today
| Time (CET) | Event | Action |
|------------|-------|--------|
| ___ | ___ | Trade normally / NO trades ±5 min / All flat before ___ |
[If FOMC within 7 days:]
| Apr __ | FOMC (__ days away) | [hawkish/dovish/neutral] tone — [one sentence on what to watch] |

---

## London (09:00–15:30) — Max 2 trades
- **09:00–09:15**: Do nothing. Mark the opening range high/low.
- **[Primary scenario]**: [Condition] → [Strategy + entry trigger] | stop ___ | target ___
- **[Secondary scenario]**: [Condition] → [Strategy + entry trigger] | stop ___ | target ___
- **Mid-morning**: [One sentence on what to do if market ranges or trends into afternoon]

## NY (15:30–22:00) — Max 2 trades
- **15:30–16:00**: Wait for ORB to form. Don't chase the open candle.
- **[Primary scenario]**: [Condition] → [entry trigger] | stop ___ | target ___
- **[Secondary scenario]**: [Condition] → [entry trigger] | stop ___ | target ___
- **Midday (16:30–19:00)**: [One sentence — sit out or specific exception]
- **Afternoon (19:00–21:30)**: [One sentence on what to watch for]
- **Hard exit**: All flat by 21:30 CET.

---

> [One sharp mindset note relevant to today's conditions — max 2 sentences.]

`$55 max loss | 4 trades max | 1 MES | 4-pt default stop | No overnight`

---
*Trading futures involves substantial risk of loss. Adapt as the market reveals new information.*
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
- **Be concise** — the entire plan should be scannable in under 60 seconds
- Be specific with prices — use actual levels from research, not placeholders
- If you cannot find a specific level, say so explicitly rather than leaving a blank or inventing a number
- Use 🔴/🟢/⚡ level markers and annotate each level as (likely reached), (possible), or (ceiling/floor)
- Session plans are bullet points only — no subheadings, no paragraphs
- Always include the risk footer line and disclaimer
