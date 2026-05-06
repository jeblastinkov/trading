#!/usr/bin/env python3
"""
Daily Battle Plan — automated generator + Gmail sender.
Reads the daily-battle-plan skill, calls Claude API with web tools,
saves the plan to journal/, and emails it as styled HTML.
"""

import os
import sys
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import anthropic
import markdown as md_lib

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
KNOWLEDGE = ROOT / "knowledge"
SKILLS = ROOT / ".claude" / "skills"
JOURNAL = ROOT / "journal"
CONFIG = ROOT / "config" / "trader-profile.yaml"


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"[Could not read {path}: {e}]"


# ---------------------------------------------------------------------------
# Tool implementations
# ---------------------------------------------------------------------------

def tool_web_fetch(url: str, prompt: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; TradingPlanBot/1.0)"}
        resp = requests.get(url, headers=headers, timeout=12)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        # Keep the first 7000 chars to stay within tool result limits
        return text[:7000]
    except Exception as e:
        return f"Fetch failed ({url}): {e}"


def tool_web_search(query: str) -> str:
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=6))
        if not results:
            return "No results found."
        lines = []
        for r in results:
            lines.append(f"**{r['title']}**\n{r['href']}\n{r.get('body', '')}\n")
        return "\n".join(lines)[:6000]
    except Exception as e:
        return f"Search failed: {e}"


TOOLS = [
    {
        "name": "web_fetch",
        "description": "Fetch and extract text content from a URL.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url":    {"type": "string", "description": "Full URL to fetch"},
                "prompt": {"type": "string", "description": "What to extract from the page"},
            },
            "required": ["url", "prompt"],
        },
    },
    {
        "name": "web_search",
        "description": "Search the web and return a summary of top results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
            },
            "required": ["query"],
        },
    },
]


def dispatch_tool(name: str, inputs: dict) -> str:
    if name == "web_fetch":
        return tool_web_fetch(inputs["url"], inputs.get("prompt", ""))
    if name == "web_search":
        return tool_web_search(inputs["query"])
    return f"Unknown tool: {name}"


# ---------------------------------------------------------------------------
# Claude API — agentic loop
# ---------------------------------------------------------------------------

def generate_plan(today: date) -> str:
    skill_text = _read(SKILLS / "daily-battle-plan.md")

    # System prompt embeds the full knowledge base so Claude can reference it
    # without a file-system tool. Cache control keeps costs low on repeat runs.
    system = [
        {
            "type": "text",
            "text": f"""You are an expert MES futures trading planner. Today is {today.isoformat()} ({today.strftime('%A')}).

## Knowledge Base

### sessions.md
{_read(KNOWLEDGE / 'sessions.md')}

### strategies.md
{_read(KNOWLEDGE / 'strategies.md')}

### risk-rules.md
{_read(KNOWLEDGE / 'risk-rules.md')}

### market-structure.md
{_read(KNOWLEDGE / 'market-structure.md')}

### session-playbook.md
{_read(KNOWLEDGE / 'session-playbook.md')}

### psychology.md
{_read(KNOWLEDGE / 'psychology.md')}

### trader-profile.yaml
{_read(CONFIG)}
""",
            "cache_control": {"type": "ephemeral"},  # cache the static knowledge base
        }
    ]

    user_prompt = (
        f"Today is {today.strftime('%A, %B %d, %Y')}.\n\n"
        "Follow the skill instructions below exactly. Use the web_fetch and web_search tools "
        "to gather live market data as specified. Then output ONLY the complete battle plan "
        "in the required markdown format — no preamble, no explanation.\n\n"
        f"{skill_text}"
    )

    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": user_prompt}]

    print("Calling Claude API...", flush=True)

    for iteration in range(25):  # safety ceiling on tool-use rounds
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            system=system,
            tools=TOOLS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return "Error: Claude returned no text."

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"  Tool call: {block.name}({list(block.input.keys())})", flush=True)
                    result = dispatch_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })
            messages.append({"role": "user", "content": tool_results})
        else:
            return f"Error: unexpected stop_reason={response.stop_reason}"

    return "Error: tool-use loop exceeded safety limit."


# ---------------------------------------------------------------------------
# HTML email formatting
# ---------------------------------------------------------------------------

def to_html(plan_md: str, today: date) -> str:
    body = md_lib.markdown(plan_md, extensions=["tables", "fenced_code", "nl2br"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    font-size: 15px; line-height: 1.6; color: #1a1a1a;
    max-width: 780px; margin: 0 auto; padding: 24px 20px;
    background: #f7f7f7;
  }}
  .card {{
    background: #fff; border-radius: 8px; padding: 28px 32px;
    box-shadow: 0 2px 8px rgba(0,0,0,.08);
  }}
  h1 {{
    color: #0d1b2a; font-size: 22px; margin-top: 0;
    border-bottom: 3px solid #e63946; padding-bottom: 10px;
  }}
  h2 {{
    color: #1d3557; font-size: 17px; margin-top: 28px;
    border-bottom: 1px solid #e0e0e0; padding-bottom: 5px;
  }}
  h3 {{ color: #457b9d; font-size: 15px; margin-top: 20px; }}
  table {{
    border-collapse: collapse; width: 100%;
    margin: 14px 0; font-size: 13.5px;
  }}
  th {{
    background: #1d3557; color: #fff;
    padding: 8px 12px; text-align: left;
  }}
  td {{ padding: 7px 12px; border-bottom: 1px solid #e8e8e8; }}
  tr:nth-child(even) td {{ background: #f4f8fc; }}
  blockquote {{
    background: #fff8e1; border-left: 4px solid #f4a261;
    margin: 14px 0; padding: 10px 16px; border-radius: 0 6px 6px 0;
    font-size: 13.5px;
  }}
  code {{
    background: #f0f0f0; padding: 2px 6px;
    border-radius: 3px; font-family: 'Courier New', monospace; font-size: 13px;
  }}
  pre {{
    background: #0d1b2a; color: #e0e0e0; padding: 14px 18px;
    border-radius: 6px; overflow-x: auto; font-size: 12.5px;
  }}
  strong {{ color: #e63946; }}
  .footer {{
    margin-top: 28px; padding-top: 12px; border-top: 1px solid #e0e0e0;
    font-size: 12px; color: #999; text-align: center;
  }}
</style>
</head>
<body>
<div class="card">
{body}
<div class="footer">
  Auto-generated · {today.strftime('%B %d, %Y')} · MES Trading Advisor · AMP Futures
</div>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Gmail SMTP sender
# ---------------------------------------------------------------------------

def send_email(subject: str, html_body: str, plain_body: str) -> None:
    gmail_from = os.environ["GMAIL_FROM"]
    app_password = os.environ["GMAIL_APP_PASSWORD"]
    gmail_to = os.environ["GMAIL_TO"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"MES Trading Advisor <{gmail_from}>"
    msg["To"] = gmail_to

    msg.attach(MIMEText(plain_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    print(f"Sending email to {gmail_to}...", flush=True)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_from, app_password)
        server.sendmail(gmail_from, gmail_to, msg.as_string())
    print("Email sent.", flush=True)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    today = date.today()

    # Skip weekends (redundant with cron schedule, but safe to have)
    if today.weekday() >= 5:
        print(f"Today is {today.strftime('%A')} — no trading. Exiting.")
        sys.exit(0)

    # Check required env vars upfront
    missing = [v for v in ("ANTHROPIC_API_KEY", "GMAIL_FROM", "GMAIL_APP_PASSWORD", "GMAIL_TO")
               if not os.environ.get(v)]
    if missing:
        print(f"ERROR: missing environment variables: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    # Skip if journal already exists (prevents double-send on re-run)
    journal_path = JOURNAL / f"{today.isoformat()}-plan.md"
    if journal_path.exists():
        print(f"Plan already exists at {journal_path} — skipping generation.")
        # Still send the email if you want; remove the next line to re-send
        sys.exit(0)

    plan_md = generate_plan(today)

    # Save to journal
    JOURNAL.mkdir(exist_ok=True)
    journal_path.write_text(plan_md, encoding="utf-8")
    print(f"Saved: {journal_path}")

    # Build and send email
    day_str = today.strftime("%A %b %d")
    subject = f"MES Battle Plan — {day_str}"
    html_body = to_html(plan_md, today)
    send_email(subject, html_body, plan_md)


if __name__ == "__main__":
    main()
