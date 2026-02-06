import yaml

from validator.results import ValidationResult
from validator.rules import (
    validate_required_fields,
    validate_metric_name,
    validate_grain,
    validate_owner,
    validate_source_tables,
    warn_optional_fields,
)

def validate_metrics(file_path: str):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    metrics = data.get("metrics", [])
    errors = []
    warnings = []

    for metric in metrics:
        errors.extend(validate_required_fields(metric))
        errors.extend(validate_metric_name(metric))
        errors.extend(validate_grain(metric))
        errors.extend(validate_owner(metric))
        errors.extend(validate_source_tables(metric))
        warnings.extend(warn_optional_fields(metric))

    return ValidationResult(errors=errors, warnings=warnings)
