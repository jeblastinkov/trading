# PineScript Agent Prompt — MES Trading Strategies

## Task

Create a **TradingView PineScript v6 indicator/strategy** that implements all four MES (Micro E-mini S&P 500) day trading strategies described below. The output should be a single, well-commented PineScript file that can be copy-pasted into TradingView's Pine Editor.

---

## Context

- **Instrument**: MES (Micro E-mini S&P 500), which tracks ES exactly at 1/10th the contract size
- **Timeframe**: Designed for **5-min chart** as the primary execution timeframe
- **Timezone**: All session logic must use **CET (UTC+1 / UTC+2 DST)**
- **Account**: $1,100 small retail account — risk management is CRITICAL

---

## Four Strategies to Implement

---

### Strategy 1: Opening Range Breakout (ORB)

**Concept**: Form a range during the first 15–30 minutes of a session, then trade the breakout.

**Two ORB windows (CET)**:
- **London ORB**: 09:00–09:15 CET (15-min range)
- **NY ORB**: 15:30–16:00 CET (30-min range)

**Rules**:
1. Calculate the high/low of the range window
2. Entry signal fires when a 5-min candle **closes** above/below the range (not just a wick)
3. **Minimum range**: 3 points — if range < 3 pts, suppress the signal
4. **Maximum range**: 8 points — if range > 8 pts, suppress the signal (stop too large)
5. Long entry: candle close above range high
6. Short entry: candle close below range low

**Stop**:
- If range ≤ 5 pts → stop = opposite side of range
- If range 6–8 pts → stop = midpoint of range (to keep risk ≤ 4 pts)

**Target**:
- Target 1: 1.5× range width
- Target 2: 2.0× range width

**Visual**:
- Draw a horizontal box or lines for the ORB range during the window
- Mark entry, stop, and target levels with labels when signal fires
- Use green for long signals, red for short signals

---

### Strategy 2: VWAP Mean Reversion

**Concept**: When price deviates 4+ points from the anchored session VWAP during ranging conditions, trade back toward VWAP.

**Rules**:
1. Calculate session-anchored VWAP (reset at 09:00 CET for London, 15:30 CET for NY)
2. Signal fires when:
   - Price is **4+ points away** from VWAP, AND
   - A reversal candle forms (bearish engulfing above VWAP, bullish engulfing below VWAP), AND
   - The candle closes **back toward** VWAP
3. Long (below VWAP): entry on the reversal candle close when price ≥ 4 pts below VWAP
4. Short (above VWAP): entry on the reversal candle close when price ≥ 4 pts above VWAP

**Stop**: 2–3 points beyond the extreme candle high/low

**Target**: VWAP itself (plus 1–2 ticks overshoot)

**Filter — disable on trend days**:
- Suppress mean reversion signals when price has not crossed VWAP in the last 20 bars (strong trend = no mean reversion)

**Visual**:
- Plot VWAP line (session-anchored, reset per session)
- Plot upper band at VWAP + 4 and lower band at VWAP − 4
- Highlight the signal bar with an arrow label

---

### Strategy 3: Trend Continuation (Pullback Entry)

**Concept**: In a confirmed trend, enter on pullbacks to support/resistance.

**Trend confirmation** (on 5-min chart):
- **Uptrend**: at least 2 consecutive higher highs AND higher lows
- **Downtrend**: at least 2 consecutive lower highs AND lower lows

**Entry rules**:
1. Confirm trend per above criteria
2. Price pulls back to one of:
   - The 20-period EMA, OR
   - The VWAP, OR
   - A prior swing high/low that flipped to support/resistance
3. Pullback retraces 40–60% of the prior impulse
4. Entry: 5-min candle closes back **in the direction of the trend** from the pullback level

**Stop**: 1–2 ticks beyond the pullback extreme (the lowest low of the pullback for longs, highest high for shorts)

**Target**:
- Conservative: prior swing high/low
- Aggressive: measured move (impulse distance projected from the pullback)
- Move stop to breakeven once price creates a new swing high/low in the trade direction

**Filters**:
- Suppress if pullback retraces > 75% of the impulse (trend breaking down)
- No new trend trades after 21:30 CET

**Visual**:
- Color the 20 EMA line (green when uptrend confirmed, red when downtrend, gray = no trend)
- Mark swing highs and swing lows on the chart
- Show entry arrow with stop/target labels when signal fires

---

### Strategy 4: Prior Day Level Reaction

**Concept**: Key prior-day levels act as support/resistance — trade the reaction when price tests them.

**Key levels to calculate and plot**:
1. **PDC** — Prior Day Close (most important)
2. **PDH** — Prior Day High
3. **PDL** — Prior Day Low
4. **ONH** — Overnight High (from 22:00 CET previous day to 09:00 CET today)
5. **ONL** — Overnight Low
6. **Round numbers** — nearest 25-point intervals (e.g., 5800, 5825, 5850)

**Setup A — Level Rejection (Fade)**:
1. Price touches/wicks through a key level
2. A reversal candle forms at that level (strong wick rejection)
3. The next candle confirms in the rejection direction
4. **Entry**: on the confirmation candle close
5. **Stop**: 2–3 points beyond the key level
6. **Target**: next key level in the rejection direction

**Setup B — Level Break + Retest (Continuation)**:
1. A 5-min candle **closes** decisively beyond a key level (not just a wick)
2. Price pulls back to retest the broken level
3. The broken level now acts as support/resistance and holds
4. **Entry**: on the retest hold candle close
5. **Stop**: 2–3 points back through the level
6. **Target**: next key level, or measured move

**Filters**:
- Suppress fade signals if the level has been tested 3+ times already today (it will likely break)
- Suppress break signals on low volume (< 50% of 20-bar average volume)

**Visual**:
- Draw all key levels as **horizontal dashed lines** with labels (PDC, PDH, PDL, ONH, ONL)
- Color coding: PDC = white/gray, PDH = green, PDL = red, ONH = lime, ONL = orange
- Extend lines to the right across the session
- Highlight the level area with a subtle background color zone (± 1 point)

---

## Risk Management Rules to Enforce in the Code

These rules must be reflected as **visual warnings or signal filters** in the script:

| Rule | Value | Implementation |
|------|-------|----------------|
| Max stop distance | 5 points | Suppress any signal where calculated stop > 5 pts |
| Min R:R ratio | 1.5:1 | Suppress any signal where target/stop < 1.5 |
| Default stop | 4 points | Use as fallback if specific stop logic yields > 4 pts |
| MES point value | $5/point | Use for P&L calculations in labels |
| Max risk per trade | $22 (4.4 pts at $5/pt) | Show risk in dollar terms on signal labels |

---

## Session Boundaries (CET)

```
London AM : 09:00 – 15:30 CET
NY PM     : 15:30 – 22:00 CET
No trade  : 22:00 – 09:00 CET (overnight, platform halt)
```

**Critical no-trade times to mark with a background shade**:
- NY Midday: 16:30–19:00 CET (low activity warning — yellow background)
- Last 30 min of RTH: 21:30–22:00 CET (no new entries — red background)

---

## Display Requirements

### Information Panel (top-right table)
Show a table with the current session's stats:
- Session: London AM / NY PM / Closed
- Current strategy applicable: ORB / Mean Reversion / Trend / Level Reaction / None
- VWAP value
- Distance from VWAP (in points)
- PDC / PDH / PDL values

### Signal Labels
Each signal label should show:
- Strategy name (e.g., "ORB LONG")
- Entry price
- Stop price
- Target 1 and Target 2 prices
- Risk in points and dollars (at $5/point for MES)
- R:R ratio

### Visual Hierarchy
- Session backgrounds: subtle London (blue tint) / NY (green tint)
- No-trade zones: red/orange tint
- Key levels: dashed horizontal lines with labels
- ORB range: shaded box
- VWAP: solid line with bands
- 20 EMA: colored by trend direction
- Swing highs/lows: small triangles

---

## Strategy Selection Logic (Priority Order)

Implement a unified signal system that selects the **highest-priority active strategy**:

```
1. Is it within 30 min of a session open?
   → YES: Show ORB setup if range width is valid
   → NO: continue...

2. Is a clear trend confirmed (2 HH/HL or 2 LH/LL)?
   → YES: Show Trend Continuation pullback setup
   → NO: continue...

3. Is price 4+ points from VWAP in a ranging market?
   → YES: Show VWAP Mean Reversion setup
   → NO: continue...

4. Is price within 1.5 points of a key prior-day level?
   → YES: Show Level Reaction setup
   → NO: No signal — display "WAIT" in the panel
```

---

## Technical Requirements

- **Language**: PineScript version 6 (`//@version=6`)
- **Type**: Strategy (`strategy()`) so backtesting is available, with `overlay=true`
- **Strategy settings**:
  - `default_qty_type = strategy.fixed`
  - `default_qty_value = 1` (1 MES contract)
  - `commission_type = strategy.commission.cash_per_contract`
  - `commission_value = 0.42` (AMP Futures rate, one-way)
  - `initial_capital = 1100`
  - `currency = currency.USD`
- **Inputs** (user-configurable via Settings panel):
  - Enable/disable each strategy independently (checkboxes)
  - Min/max ORB range (default 3–8)
  - VWAP deviation threshold (default 4 pts)
  - Pullback retracement min/max % (default 40–75%)
  - Stop buffer in points (default 0.25)
  - Show/hide visual elements (levels, backgrounds, labels)

---

## Deliverable

A single `.pine` file that:
1. Compiles without errors in TradingView's Pine Editor
2. Works on the **5-minute MES/ES chart**
3. Implements all 4 strategies with proper entry/exit logic
4. Displays clean, readable visuals (not cluttered)
5. Has comments explaining each section of logic
6. Passes the risk filter (stops ≤ 5 pts, R:R ≥ 1.5) before generating any signal

---

*Based on the MES Trading Advisor knowledge base: strategies.md, risk-rules.md, session-playbook.md*
