import re

def parse_constraints(text):
    constraints = {}

    size_match = re.search(r'(\d+)\s*MB', text, re.IGNORECASE)
    if size_match:
        constraints["max_size_mb"] = int(size_match.group(1))

    formats_match = re.search(r'Only ([A-Za-z ,]+) formats', text)
    if formats_match:
        formats = formats_match.group(1)
        constraints["formats"] = [f.strip().upper() for f in formats.split("and")]

    return constraints


def generate_test_cases(feature_text):
    constraints = parse_constraints(feature_text)
    tests = []

    # Functional test
    if "formats" in constraints and "max_size_mb" in constraints:
        tests.append({
            "test_case": f"Upload valid {constraints['formats'][0]} under {constraints['max_size_mb']}MB",
            "type": "Functional",
            "expected_result": "Upload succeeds and image is displayed"
        })

    # Edge case: size
    if "max_size_mb" in constraints:
        tests.append({
            "test_case": f"Upload file larger than {constraints['max_size_mb']}MB",
            "type": "Edge",
            "expected_result": "Error message is shown"
        })

    # Negative case: invalid format
    if "formats" in constraints:
        tests.append({
            "test_case": "Upload unsupported file format",
            "type": "Negative",
            "expected_result": "File type is rejected"
        })

    return tests


def main():
    with open("input/feature_description.txt") as f:
        feature_text = f.read()

    tests = generate_test_cases(feature_text)

    with open("output/test_cases.yaml", "w") as f:
        for t in tests:
            f.write(f"- test_case: {t['test_case']}\n")
            f.write(f"  type: {t['type']}\n")
            f.write(f"  expected_result: {t['expected_result']}\n\n")

    print("QA test cases generated automatically.")


if __name__ == "__main__":
    main()
