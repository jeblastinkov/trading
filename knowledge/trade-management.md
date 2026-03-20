# Trade Management

## Entry Techniques

### Limit Order Entry (Preferred)
- Place limit order at your target entry price
- Better fills, no slippage, defined risk from the start
- Risk: may not get filled if price doesn't reach your level
- Use for: Level reactions, mean reversion, pullback entries

### Stop Order Entry (Breakout)
- Place buy-stop above resistance or sell-stop below support
- Guarantees entry on breakout but may have 1-2 ticks slippage
- Use for: Opening Range Breakout, level break continuation

### Market Order (Emergency Only)
- Immediate fill at current price
- Worst fills, highest slippage
- Use ONLY when you need to exit immediately (stop hit, risk management)

## Stop Placement Rules

### Golden Rules
1. **ALWAYS set your stop BEFORE entering the trade** — no exceptions
2. **Never move your stop further from entry** — only tighter or to breakeven
3. **Place stops at logical levels, not arbitrary distances** — behind structure, not at a round dollar amount

### Stop Placement by Strategy

| Strategy | Stop Location | Typical Distance |
|----------|--------------|-----------------|
| Opening Range Breakout | Opposite side of range or midpoint | 3-5 points |
| VWAP Mean Reversion | Beyond the extreme of the deviation | 2-4 points |
| Trend Continuation | Below pullback low (long) / above pullback high (short) | 3-5 points |
| Prior Day Level Reaction | Beyond the key level | 2-3 points |

### Stop Buffer
Always add 0.50-1.00 points beyond the structure level. This accounts for:
- Stop hunting / liquidity grabs (common on MES)
- Slight overshoots before reversal
- Spread widening during volatile moments

Example: If PDH is at 5852.00 and you're shorting the rejection, don't put stop at 5852.25. Put it at 5853.00-5853.50.

## Target Setting

### Fixed Targets
- **Conservative**: 1.5× the risk distance
- **Standard**: 2× the risk distance
- **Aggressive**: 3× the risk distance (only on strong trend days)

### Dynamic Targets
- Next key level (PDH, PDL, VWAP, round number)
- Measured move (impulse distance from the breakout point)
- VWAP (for mean reversion trades)

### Target Selection Guide
| Market Type | Target Approach |
|-------------|----------------|
| Trend day | Use trailing stop, let winners run |
| Range day | Fixed target at opposite extreme of range |
| Breakout | Measured move + trail stop |
| Chop | Smallest target (1:1 to 1.5:1) or don't trade |

## Moving to Breakeven

### When to Move Stop to Breakeven
- After price has moved at least 1.5× your risk in your direction
- After hitting your first target (if scaling out)
- After a new structural high/low forms in your direction
- **Never before 1× risk** — you'll get stopped out on normal retracements

### How to Set Breakeven
- Move stop to entry price + 1-2 ticks (0.25-0.50 points)
- The extra ticks cover your commission ($0.84 round trip ≈ 0.17 points)
- This means your worst case is ~flat, not a loss

## Trailing Stops

### When to Trail
- Only on trend days when you have a clear directional move
- After price has moved 2× your initial risk
- During London-NY overlap when momentum is strong

### How to Trail
1. **Structure-based** (recommended): Move stop to below/above each new swing low/high on the 5-min chart
2. **Fixed distance**: Trail by X points below/above current price (e.g., 4-point trail)
3. **VWAP trail**: On trend days, trail stop to VWAP (stays wide but protects the trend)

### Trailing Stop Rules
- Only move in the direction of profit (tighten, never widen)
- Don't trail too tight — 2 points minimum trailing distance on MES
- Accept that trailing stops will always give back some profit — that's the cost of catching big moves

## Partial Exits (When Account Allows Multiple Contracts)

Not applicable at 1 contract. When you scale to 2+ contracts:
- Take half off at 1.5× risk (lock in profit)
- Move remaining stop to breakeven
- Trail the remainder for bigger move

## Time-Based Exits

| Situation | Action |
|-----------|--------|
| Trade in profit but stalling for 30+ min | Tighten stop to just below breakeven |
| Position open approaching 22:00 CET | Begin looking to exit (US RTH ending) |
| Position open approaching 22:30 CET | EXIT NOW — 30 min before daily halt |
| Holding into a news event | Exit before the event or tighten stop significantly |

## Trade Management Mistakes to Avoid

1. **Moving stop further away** — "just giving it more room" is how small accounts die
2. **Exiting too early** — trust your target. If the setup is valid, let it work
3. **Averaging down** — NEVER add to a losing position. One contract, one direction, one chance
4. **Revenge re-entry** — Got stopped out? Don't immediately re-enter. Wait for a new setup
5. **Hoping** — If the reason for your trade is gone, exit. Don't hope.
6. **Ignoring time** — A trade that takes too long is telling you something. Listen.
