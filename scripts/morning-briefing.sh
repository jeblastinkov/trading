#!/bin/bash
# Morning briefing runner — invoked by cron at 7:30 CET on weekdays
# Runs Claude Code with the /morning-briefing skill

cd /home/user/trading

# Log file for debugging
LOG="/home/user/trading/journal/briefing-cron.log"

echo "--- $(date) --- Running morning briefing ---" >> "$LOG"

# Run Claude with the morning-briefing skill, non-interactive
/opt/node22/bin/claude --print "Run /morning-briefing for today" \
  2>> "$LOG"

echo "--- $(date) --- Done ---" >> "$LOG"
