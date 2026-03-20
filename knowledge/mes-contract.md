# MES Contract Specifications

## Micro E-mini S&P 500 Futures (MES)

| Specification | Value |
|---------------|-------|
| **Symbol** | MES |
| **Exchange** | CME Globex |
| **Underlying** | S&P 500 Index |
| **Contract Multiplier** | $5 per index point |
| **Tick Size** | 0.25 index points |
| **Tick Value** | $1.25 per tick |
| **Point Value** | $5.00 per point (= 4 ticks) |
| **Settlement** | Cash settled |
| **Contract Months** | H (Mar), M (Jun), U (Sep), Z (Dec) |

## Quick Dollar Reference

| Move | Ticks | Points | Dollar P&L (1 contract) |
|------|-------|--------|------------------------|
| 1 tick | 1 | 0.25 | $1.25 |
| 4 ticks | 4 | 1.0 | $5.00 |
| 10 points | 40 | 10.0 | $50.00 |
| 20 points | 80 | 20.0 | $100.00 |
| 50 points | 200 | 50.0 | $250.00 |

## Trading Hours

| Timezone | Open | Close | Daily Halt |
|----------|------|-------|------------|
| **ET (Eastern)** | Sun 6:00 PM | Fri 5:00 PM | 5:00–6:00 PM daily |
| **CT (Central/Chicago)** | Sun 5:00 PM | Fri 4:00 PM | 4:00–5:00 PM daily |
| **CET (our timezone)** | Mon 00:00 | Sat 00:00 | 23:00–00:00 daily |

Note: CET is UTC+1 (winter) / CEST is UTC+2 (summer). US and EU DST switches happen on different dates, which can shift schedules by 1 hour temporarily.

## Relationship to ES (E-mini S&P 500)

- MES = 1/10th the size of ES
- ES multiplier: $50/point vs. MES: $5/point
- Use ES charts for analysis (more liquid), execute on MES
- MES follows ES tick-for-tick

## Contract Roll Schedule

Contracts expire on the 3rd Friday of the contract month. Roll to the next contract ~1 week before expiry (the Thursday before expiration Friday).

### 2026 Roll Calendar
| Contract | Symbol | Expiration | Roll By |
|----------|--------|------------|---------|
| March 2026 | MESH6 | Mar 20, 2026 | ~Mar 12 |
| June 2026 | MESM6 | Jun 19, 2026 | ~Jun 11 |
| September 2026 | MESU6 | Sep 18, 2026 | ~Sep 10 |
| December 2026 | MESZ6 | Dec 18, 2026 | ~Dec 10 |

## Notional Value

At S&P 500 = 5,800: Notional = 5,800 × $5 = $29,000 per contract
At S&P 500 = 6,000: Notional = 6,000 × $5 = $30,000 per contract

## AMP Futures Commission Breakdown

| Fee Component | Per Side |
|---------------|----------|
| Exchange (CME) | $0.25 |
| CQG Order Routing | $0.10 |
| NFA | $0.02 |
| AMP Clearing | $0.05 |
| **Total per side** | **$0.42** |
| **Round trip** | **$0.84** |

Commission impact: $0.84 round trip = 0.67 ticks. On a 16-tick ($20) target, commission is ~4.2% of profit.

## Margin Requirements (AMP Futures)

| Type | Amount |
|------|--------|
| Day Trade Margin | ~$50 |
| Overnight/Maintenance Margin | ~$2,455 |

**Critical**: With a $1,100 account, overnight positions are NOT possible (margin $2,455 > account $1,100). All positions must be closed before the daily halt at 23:00 CET.
