import sys
from validator.validate import validate_metrics

def main():
    if len(sys.argv) < 2:
        print("Usage: metric-contract validate <path_to_yaml>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = validate_metrics(file_path)

    if result.errors:
        print("❌ Metric Contract validation failed:\n")
        for error in result.errors:
            print(f"ERROR: {error}")

    if result.warnings:
        print("\n⚠️ Warnings:\n")
        for warning in result.warnings:
            print(f"WARNING: {warning}")

    if result.is_valid():
        print("\n✅ Metric Contracts are structurally valid")
        sys.exit(0)

    sys.exit(1)

if __name__ == "__main__":
    main()
