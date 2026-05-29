# Weekly Report: Setup and Run

This folder contains a lightweight prototype to generate a weekly report draft from sample data and an AI prompt template.

Prerequisites

- Python 3.8+
- (Optional) `openai` Python package and `OPENAI_API_KEY` environment variable to call the OpenAI API.

Install (optional):

```powershell
python -m pip install openai
```

Run locally with stub output:

```powershell
python scripts/generate_weekly_report.py --output draft.txt
type draft.txt
```

Run with OpenAI (set API key first):

```powershell
$Env:OPENAI_API_KEY = "sk-..."
python scripts/generate_weekly_report.py --output draft.txt
type draft.txt
```

Files added

- `prompts/weekly_report_prompt.md`: Prompt template used to ask the model for a draft report.
- `data/sample_jira.json`: Small synthetic Jira export.
- `data/sample_metrics.txt`: Simple metrics summary.
- `data/sample_slack.txt`: Slack recap.
- `scripts/generate_weekly_report.py`: Script that builds the prompt and calls OpenAI if configured.

Next steps

- Connect real Jira/Sheets export and adapt `scripts/generate_weekly_report.py` to fetch data via API.
- Add formatting/templating to publish directly to Google Docs or Notion.
