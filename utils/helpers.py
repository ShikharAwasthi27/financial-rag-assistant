import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any


# -------------------------------
# Logging Configuration
# -------------------------------

def setup_logger(log_file: str = "app.log") -> logging.Logger:
    """
    Configure and return logger instance.
    """

    logger = logging.getLogger("financial_rag")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# -------------------------------
# Save JSON Utility
# -------------------------------

def save_json(data: Dict, filepath: str):
    """
    Save dictionary as JSON file.
    """

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# -------------------------------
# Load JSON Utility
# -------------------------------

def load_json(filepath: str) -> Dict:
    """
    Load JSON file.
    """

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# -------------------------------
# Ensure Directory Exists
# -------------------------------

def ensure_directory(path: str):
    """
    Create directory if it does not exist.
    """

    if not os.path.exists(path):
        os.makedirs(path)


# -------------------------------
# Timestamp Generator
# -------------------------------

def current_timestamp() -> str:
    """
    Return formatted timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# -------------------------------
# Format Sources
# -------------------------------

def format_sources(docs: List[Any]) -> List[str]:
    """
    Extract unique source names from retrieved documents.
    """

    sources = []

    for doc in docs:

        source = doc.metadata.get("source", "Unknown Source")

        page = doc.metadata.get("page", None)

        if page:
            source_text = f"{source} | Page {page}"
        else:
            source_text = source

        sources.append(source_text)

    return list(set(sources))


# -------------------------------
# Confidence Score
# -------------------------------

def calculate_confidence(similarity_scores: List[float]) -> float:
    """
    Calculate average confidence score.
    """

    if not similarity_scores:
        return 0.0

    return round(sum(similarity_scores) / len(similarity_scores), 3)


# -------------------------------
# Out-of-Scope Response
# -------------------------------

def out_of_scope_response() -> Dict:
    """
    Standard out-of-scope response.
    """

    return {
        "answer": (
            "This assistant only answers questions "
            "related to financial reports and filings."
        ),
        "sources": []
    }


# -------------------------------
# Insufficient Context Response
# -------------------------------

def insufficient_context_response() -> Dict:
    """
    Standard insufficient-context response.
    """

    return {
        "answer": (
            "Insufficient context available in the "
            "retrieved financial documents."
        ),
        "sources": []
    }
