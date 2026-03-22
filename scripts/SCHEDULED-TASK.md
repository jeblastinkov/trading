# MES Morning Briefing — Scheduled Task

## Task Description
**Name**: MES Morning Briefing Generator
**Purpose**: Automatically generate a daily executive trading briefing before the London session opens. Produces bias, key levels, economic calendar, and session game plans for MES futures trading.

## Schedule
- **Frequency**: Weekdays only (Mon–Fri)
- **Time**: 07:30 CET (06:30 UTC in winter / 05:30 UTC in summer)
- **Skip**: Weekends, US market holidays

## Crontab Entry

```bash
# MES Morning Briefing — runs weekdays at 07:30 CET
# Adjust UTC offset for DST: CET=UTC+1 (winter), CEST=UTC+2 (summer)

# Winter (Nov–Mar): 07:30 CET = 06:30 UTC
30 6 * 11,12,1,2,3 1-5 /home/user/trading/scripts/morning-briefing.sh

# Summer (Apr–Oct): 07:30 CEST = 05:30 UTC
30 5 * 4,5,6,7,8,9,10 1-5 /home/user/trading/scripts/morning-briefing.sh
```

## Installation

```bash
# Open crontab editor
crontab -e

# Paste the two cron lines above, save, and exit
# Verify with:
crontab -l
```

## What It Does
1. Runs `claude --print` with the `/morning-briefing` skill
2. Searches the web for current MES/ES levels, overnight action, and economic calendar
3. Reads the knowledge base (strategies, sessions, risk rules)
4. Writes a briefing to `journal/YYYY-MM-DD-briefing.md`
5. Logs execution to `journal/briefing-cron.log`

## Output Location
- **Briefing**: `journal/YYYY-MM-DD-briefing.md`
- **Log**: `journal/briefing-cron.log`

## Troubleshooting
- Check `journal/briefing-cron.log` for errors
- Ensure `claude` CLI is available at `/opt/node22/bin/claude`
- Ensure the script is executable: `chmod +x scripts/morning-briefing.sh`
- Test manually: `./scripts/morning-briefing.sh`
