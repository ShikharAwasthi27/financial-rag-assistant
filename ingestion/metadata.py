import re


def extract_metadata(file_name):

    # Example:
    # apple_2024_10k.pdf

    pattern = r'([a-zA-Z]+)_(\d{4})_(10k|10q)'

    match = re.search(pattern, file_name.lower())

    if match:
        return {
            "company": match.group(1),
            "year": match.group(2),
            "report_type": match.group(3)
        }

    return {}
