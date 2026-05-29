#!/usr/bin/env python3
"""Generate a weekly report draft from sample data and a prompt template.

Usage:
  python scripts/generate_weekly_report.py --output draft.txt

If `OPENAI_API_KEY` is set and `openai` package installed, the script will attempt
to call the OpenAI API. Otherwise it will produce a local stub draft.
"""
import os
import json
import argparse


ROOT = os.path.dirname(os.path.dirname(__file__))


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def build_prompt(template, jira, metrics, slack):
    filled = template.replace('{{JIRA}}', json.dumps(jira, indent=2))
    filled = filled.replace('{{METRICS}}', metrics)
    filled = filled.replace('{{SLACK}}', slack)
    return filled


def call_openai(prompt_text):
    try:
        import openai
    except Exception:
        print('openai package not installed; skipping remote call.')
        return None

    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        print('OPENAI_API_KEY not set; skipping remote call.')
        return None

    openai.api_key = key
    model = os.environ.get('OPENAI_MODEL', 'gpt-4o-mini')
    try:
        resp = openai.ChatCompletion.create(
            model=model,
            messages=[{'role':'user','content':prompt_text}],
            max_tokens=600,
            temperature=0.2,
        )
        return resp['choices'][0]['message']['content'].strip()
    except Exception as e:
        print('OpenAI call failed:', e)
        return None


def make_local_stub(jira):
    lines = ['Summary: Weekly update generated locally.']
    lines.append('Highlights:')
    for i, item in enumerate(jira.get('issues', [])[:3], 1):
        lines.append(f'- {item.get("key")} {item.get("summary")}')
    lines.append('\nBlockers:')
    lines.append('- No blockers found in sample data')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', default='draft.txt')
    args = parser.parse_args()

    jira_path = os.path.join(ROOT, 'data', 'sample_jira.json')
    metrics_path = os.path.join(ROOT, 'data', 'sample_metrics.txt')
    slack_path = os.path.join(ROOT, 'data', 'sample_slack.txt')
    prompt_path = os.path.join(ROOT, 'prompts', 'weekly_report_prompt.md')

    jira = load_json(jira_path) if os.path.exists(jira_path) else {'issues': []}
    metrics = load_text(metrics_path) if os.path.exists(metrics_path) else 'No metrics available.'
    slack = load_text(slack_path) if os.path.exists(slack_path) else 'No slack recap available.'
    prompt_template = load_text(prompt_path)

    full_prompt = build_prompt(prompt_template, jira, metrics, slack)

    print('Built prompt; attempting to call OpenAI if configured...')
    ai_result = call_openai(full_prompt)

    if ai_result is None:
        print('Falling back to local stub generation.')
        ai_result = make_local_stub(jira)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(ai_result)

    print('Draft written to', args.output)


if __name__ == '__main__':
    main()
