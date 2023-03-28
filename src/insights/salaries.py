from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_data = read(path)
    salaries = [
        job['max_salary'] for job in jobs_data if job['max_salary'].isdigit()
    ]
    int_salaries = list(map(int, salaries))

    return max(int_salaries)


def get_min_salary(path: str) -> int:
    jobs_data = read(path)
    salaries = [
        int(job['min_salary'])
        for job in jobs_data
        if job['min_salary'].isdigit()
    ]
    int_salaries = list(map(int, salaries))

    return min(int_salaries)


def is_salary_not_valid(salary: Union[int, str]) -> bool:
    try:
        int(salary)
        return False
    except (ValueError, TypeError):
        return True


def is_min_greater_than_max(
        minimum: Union[int, str], maximum: Union[int, str]) -> bool:
    try:
        return int(minimum) > int(maximum)
    except TypeError:
        return True


def are_fields_not_digits(
        minimum: Union[int, str], maximum: Union[int, str]) -> bool:
    try:
        return not str(minimum).isnumeric() or not str(maximum).isnumeric()
    except KeyError:
        return True


def do_fields_exist(job: Dict) -> bool:
    return 'min_salary' not in job or 'max_salary' not in job


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validation1 = do_fields_exist(job)
    validation2 = are_fields_not_digits(
        job.get('min_salary'), job.get('max_salary'))
    validation3 = is_min_greater_than_max(
        job.get('min_salary'), job.get('max_salary'))
    validation4 = is_salary_not_valid(salary)

    if validation1 or validation2 or validation3 or validation4:
        raise ValueError

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def is_salary_within_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        return matches_salary_range(job, salary)
    except ValueError:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary_range: Union[str, int]
) -> List[Dict]:
    filtered = [job for job in jobs if is_salary_within_range(
        job, salary_range)]
    return filtered
