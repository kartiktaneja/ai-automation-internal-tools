# Knowledgebase Builder

This tool converts unstructured support text into structured knowledge
that can be reused by support and product teams.

## What it does
- Reads raw support text
- Extracts issues, symptoms, causes, and resolution steps
- Outputs structured JSON for internal use

## Why it exists
Support information often lives in emails and chat logs.
This tool demonstrates how that information can be organized automatically
into a consistent format.

## How to run
1. Place text in `input/raw_support_text.txt`
2. Run `python knowledgebase_builder.py`
3. View results in `output/structured_knowledge.json`

## Notes
The analysis layer is designed to be AI-assisted and can be connected
to a language model if required.
