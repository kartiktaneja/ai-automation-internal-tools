import csv
import json
from collections import Counter

USE_REAL_AI = False


def load_issues(path):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def analyze_issues(issues):
    counter = Counter(issue["issue_type"] for issue in issues)
    return dict(counter)


def generate_ai_insight(stats):
    if USE_REAL_AI:
        from openai import OpenAI
        client = OpenAI()

        prompt = f"""
        You are an operations analyst.

        Given the issue statistics below, generate:
        1. Summary of main problems
        2. Possible root causes
        3. Actionable recommendations

        Statistics:
        {json.dumps(stats, indent=2)}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    else:
        # Mock AI output (still derived from stats)
        top_issue = max(stats, key=stats.get)
        return f"""
Main issue identified: {top_issue}

Recommendation:
Investigate recurring causes related to {top_issue.lower()} and prioritize fixes.
"""


def main():
    issues = load_issues("input/issues.csv")
    stats = analyze_issues(issues)
    insight = generate_ai_insight(stats)

    with open("output/ops_report.md", "w") as f:
        f.write("# Operations Insight Report\n\n")
        f.write("## Issue Statistics\n")
        f.write(json.dumps(stats, indent=2))
        f.write("\n\n## AI-Generated Insights\n")
        f.write(insight)

    print("Operations insight report generated.")


if __name__ == "__main__":
    main()
