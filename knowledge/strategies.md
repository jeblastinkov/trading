# Trading Strategies

## Strategy Overview

Four core strategies for MES day trading, designed for a small account ($1,100) with strict risk management. Each strategy has specific session windows, setup criteria, entry/exit rules, and conditions when it should NOT be used.

---

## Strategy 1: Opening Range Breakout (ORB)

### Concept
Wait for the first 15-30 minutes of a session to form a range, then trade the breakout in either direction.

### When to Use
- London open: 09:00-09:30 CET (15-min range)
- NY open: 15:30-16:00 CET (30-min range)
- Best on days with a catalyst (economic data, overnight gap, strong trend context)

### Setup Rules
1. Mark the high and low of the first 15 min (London) or 30 min (NY)
2. Wait for a candle to CLOSE above/below the range (not just wick)
3. Minimum range width: 3 points (below this, it's too tight and likely to chop)
4. Maximum range width: 8 points (above this, stop is too large for our account)

### Entry
- **Long**: Enter on the close of the candle that breaks above the range high
- **Short**: Enter on the close of the candle that breaks below the range low
- Use a limit order 0.25 points above/below the breakout candle close for better fill

### Stop
- Place stop on the opposite side of the range
- If range is 3-5 points: stop = opposite side of range (3-5 point risk) ✅
- If range is 6-8 points: stop = midpoint of range (3-4 point risk) ⚠️
- If range > 8 points: **skip the trade** ❌

### Target
- Primary target: 1.5× the range width
- Secondary target: 2× the range width (move stop to breakeven after primary hit)
- Or target the next key level (PDH, PDL, ONH, ONL)

### Filters (Don't Trade ORB When)
- Range forms entirely inside prior day's range (consolidation likely to continue)
- Major news event scheduled within 30 min of breakout
- Overnight range was extremely large (>30 points) — market may be exhausted
- Third attempt at a breakout in the same direction (fading momentum)

### Example
```
NY Open 15:30-16:00 CET:
Range: High 5852, Low 5846 (6 points)
Breakout: Candle closes above 5852 at 16:05
Entry: 5852.25 (long)
Stop: 5849 (midpoint of range, 3.25 points = $16.25 risk)
Target 1: 5861 (1.5× range = 9 points above range low)
Target 2: 5864 (2× range = move stop to 5852.25 breakeven)
R:R = 2.7:1 ✅
```

---

## Strategy 2: VWAP Mean Reversion

### Concept
When price deviates significantly from VWAP during ranging/rotational conditions, enter toward VWAP expecting a reversion to the mean.

### When to Use
- London core: 10:30-14:00 CET (after the opening move settles)
- NY midday: 16:30-19:00 CET (lunchtime chop)
- Best on range days, NOT on trend days

### Setup Rules
1. Identify that the market is in a range (no clear trend on 15-min chart)
2. Price has moved 4+ points away from VWAP
3. Momentum is fading (smaller candles, wicks forming at the extreme)
4. Volume is declining on the push away from VWAP

### Entry
- **Long** (when price is below VWAP): Enter on a bullish reversal candle (hammer, engulfing) at least 4 points below VWAP
- **Short** (when price is above VWAP): Enter on a bearish reversal candle at least 4 points above VWAP
- Confirmation: 1-min or 5-min candle closes back toward VWAP

### Stop
- 2-3 points beyond the extreme (beyond the lowest low / highest high of the deviation)
- Typical risk: 2-4 points ($10-20) ✅

### Target
- Primary: VWAP itself
- Secondary: Slight overshoot past VWAP (1-2 points beyond)
- Take profit at VWAP unless strong momentum carries through

### Filters (Don't Trade Mean Reversion When)
- Market is trending strongly (higher highs and higher lows, or vice versa)
- It's the first 30 min after a session open (let direction establish first)
- Price deviation from VWAP is due to a news event (new information = new fair value)
- VWAP is flat AND price is near it (no trade needed)

### Identifying Range vs. Trend
- **Range day signs**: Price crosses VWAP multiple times, initial balance is narrow (< 8 points), no follow-through after breaks
- **Trend day signs**: Price stays on one side of VWAP, initial balance expands, buyers/sellers in control from open

---

## Strategy 3: Trend Continuation (Pullback Entry)

### Concept
In a trending market, wait for a pullback to a support/resistance level, then enter in the direction of the trend.

### When to Use
- London-NY overlap: 14:00-17:30 CET (strongest trends develop here)
- NY afternoon: 19:00-21:00 CET (trend completion)
- Only when a clear trend is established (higher highs/lows or lower highs/lows on 5-min chart)

### Setup Rules
1. Confirm the trend: at least 2 higher highs and higher lows (uptrend) or 2 lower highs and lower lows (downtrend) on the 5-min chart
2. Wait for a pullback to one of: prior swing high/low, 20 EMA on 5-min, VWAP (in trend's direction)
3. Pullback should retrace 40-60% of the last impulse move
4. Pullback should be on lower volume than the impulse

### Entry
- **Long (uptrend)**: Enter when price bounces off support level with a bullish candle
- **Short (downtrend)**: Enter when price rejects resistance level with a bearish candle
- Trigger: 5-min candle closes in the trend direction at the pullback level

### Stop
- Below the pullback low (longs) or above the pullback high (shorts)
- Add 1-2 ticks (0.25-0.50 points) buffer beyond the level
- Typical risk: 3-5 points ($15-25) ✅

### Target
- Prior swing high/low (conservative)
- Measured move: impulse distance projected from pullback (aggressive)
- Move stop to breakeven after price makes a new swing high/low in your direction

### Filters (Don't Trade Pullbacks When)
- Pullback is deeper than 75% of the impulse (trend may be breaking)
- Pullback takes longer than the impulse in time (momentum exhaustion)
- Volume increases on the pullback (selling/buying pressure, not just profit-taking)
- Near end of session (don't start new trend trades after 21:30 CET)

---

## Strategy 4: Prior Day Level Reaction

### Concept
Key levels from the prior day act as support/resistance. Trade the reaction when price tests these levels.

### When to Use
- Any session, but best during London AM and NY open when these levels are first tested
- Works in any market condition (trend, range, or breakout)

### Key Levels (in order of importance)
1. **Prior Day Close (PDC)** — strongest single reference level
2. **Prior Day High (PDH)** and **Prior Day Low (PDL)** — range boundaries
3. **Overnight High (ONH)** and **Overnight Low (ONL)** — pre-session range
4. **Weekly High/Low** — broader context
5. **Round numbers** (5800, 5850, 5900) — psychological levels

### Setup: Level Rejection (Fade)
1. Price approaches a key level
2. First test: price touches/slightly overshoots the level
3. Rejection: strong wick / reversal candle forms at the level
4. Confirmation: next candle confirms the rejection direction

**Entry**: On the confirmation candle close
**Stop**: 2-3 points beyond the key level
**Target**: Next key level in the direction of the fade

### Setup: Level Break (Continuation)
1. Price approaches a key level
2. Candle CLOSES decisively beyond the level (not just a wick)
3. Volume confirms the break (higher than average)
4. Retest: price comes back to the broken level (now support/resistance)

**Entry**: On the retest, as the level holds as new support/resistance
**Stop**: 2-3 points back through the level
**Target**: Next key level, or measured move

### Filters
- Don't fade a level that has been tested 3+ times (it will likely break)
- Don't trade level breaks on low volume (likely a false breakout)
- Skip if multiple key levels are clustered within 3 points (messy zone)

---

## When NOT to Trade (Any Strategy)

### Hard No-Trade Rules
- ❌ Before and during FOMC announcements (no new trades from 19:00 CET until 30 min after)
- ❌ First 5 min after major economic releases (CPI, NFP, GDP, PPI)
- ❌ When approaching daily loss limit ($55)
- ❌ During daily halt (23:00-00:00 CET)
- ❌ On half-day/holiday sessions
- ❌ When feeling emotional, tired, or distracted
- ❌ After 2 consecutive losses without a break
- ❌ Last 30 min before daily halt if holding a position

### Yellow Flags (Reduce Size or Sit Out)
- ⚠️ Monday mornings (often directionless until NY open)
- ⚠️ Friday afternoons (reduced liquidity, profit-taking)
- ⚠️ NY midday (16:30-19:00 CET) — choppy
- ⚠️ When VIX is extremely low (< 12) — low volatility = tight ranges = hard to profit
- ⚠️ When VIX is extremely high (> 35) — wild swings = hard to manage risk

## Strategy Selection Flowchart

```
Is the market trending? (clear HH/HL or LH/LL on 5-min)
├── YES → Use Strategy 3 (Trend Continuation Pullback)
│         Is price near a key level?
│         ├── YES → Combine with Strategy 4 (Level Reaction)
│         └── NO → Pure pullback entry
└── NO → Is it the first 30 min of a session?
    ├── YES → Use Strategy 1 (Opening Range Breakout)
    └── NO → Is price 4+ points from VWAP?
        ├── YES → Use Strategy 2 (VWAP Mean Reversion)
        └── NO → Is price at a key prior day level?
            ├── YES → Use Strategy 4 (Prior Day Level Reaction)
            └── NO → NO TRADE — wait for a setup
```
