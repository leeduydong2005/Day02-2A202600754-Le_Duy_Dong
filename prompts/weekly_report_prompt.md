Weekly Report Draft Prompt

Instructions for the AI:
- Read the provided Jira items, metrics summary and Slack recap.
- Produce a concise weekly report for engineering leadership with sections: Summary, Highlights, Metrics, Blockers, Risks, Next actions.
- Keep the tone professional and concise (3–6 short paragraphs). Use bullet points for Highlights and Next actions.

Template placeholders:
- {{JIRA}}
- {{METRICS}}
- {{SLACK}}

Example prompt to send to the model:

```
You are an assistant that writes a short weekly report for engineering leadership.

Input:
Jira items:
{{JIRA}}

Metrics summary:
{{METRICS}}

Slack recap:
{{SLACK}}

Output format:
1) Summary (1 short paragraph)
2) Highlights (3 bullets)
3) Metrics (2–3 bullets)
4) Blockers (bulleted list with owner)
5) Risks (1–2 bullets)
6) Next actions (2–3 bullets, with owners)

Keep it ≤ 250 words.
```
