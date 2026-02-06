import re 

REQUIRED_FIELDS = [
    'name',
    'description',
    'grain',
    'owner',
    'source_tables'
]

OPTIONAL_FIELDS = [
    'freshness_sla',
    'dimensions',
    'caveats',
]

SNAKE_CASE_PATTERN = re.compile(r'^[a-z0-9_]+$')

def validate_required_fields(metric: dict):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in metric or metric[field] is None:
            errors.append(f"Metric {metric['name']} is missing required field: {field}")
    return errors 

def validate_metric_name(metric: dict):
    errors = []
    name = metric['name']
    if not SNAKE_CASE_PATTERN.match(name):
        errors.append(f"Metric {name} is not in snake_case format")
    return errors 

def validate_grain(metric: dict):
    errors = []
    grain = metric['grain']
    if not grain:
        errors.append(f"Metric {metric['name']} is missing required field: grain")
    return errors 

def validate_owner(metric: dict):
    errors = []
    owner = metric['owner']
    if not owner or str(owner).strip() == '':
        errors.append(f"Metric {metric['name']} is missing required field: owner")
    return errors 

def validate_source_tables(metric: dict):
    errors = []
    source_tables = metric['source_tables']
    if not source_tables:
        errors.append(f"Metric {metric['name']} is missing required field: source_tables")
    return errors 

def warn_optional_fields(metric: dict):
    warnings = [] 

    for field in OPTIONAL_FIELDS:
        if field not in metric or metric[field] is None:
            warnings.append(f"Metric {metric['name']} is missing optional field: {field}")
    return warnings