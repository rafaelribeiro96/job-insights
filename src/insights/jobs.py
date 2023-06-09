from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, newline='', encoding='utf-8') as file:
            data = csv.DictReader(file)
            jobs = list(data)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return []
    return jobs


def get_unique_job_types(path: str) -> List[str]:
    with open(path, newline='', encoding='utf-8') as file:
        data = csv.DictReader(file)
        types = set(data_row['job_type'] for data_row in data)
        return list(types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered = [job for job in jobs if job["job_type"] == job_type]
    return filtered
