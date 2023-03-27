from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_data = read(path)
    industries_types = set(
        industry['industry'] for industry in jobs_data if industry['industry'])

    return list(industries_types)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered = [job for job in jobs if job["industry"] == industry]
    return filtered
