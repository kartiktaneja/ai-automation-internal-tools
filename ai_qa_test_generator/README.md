# QA Test Case Generator

## Purpose
This tool demonstrates how QA test cases can be derived automatically from
natural-language feature descriptions.

## What it does
- Reads a plain-text feature description
- Identifies constraints and requirements
- Produces functional, edge, and negative test cases

## Why it exists
Writing QA test cases manually is repetitive and error-prone.
This tool shows how test planning can be automated from requirements.

## How to run
1. Edit `input/feature_description.txt`
2. Run `python qa_test_generator.py`
3. View results in `output/test_cases.yaml`

## Notes
The logic is deterministic and designed to be extended
with AI-based reasoning if needed.
