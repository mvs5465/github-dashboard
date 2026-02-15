#!/usr/bin/env python3
"""Validate JSON data files and HTML dashboards"""
import json
import sys
from pathlib import Path

def validate_json(file_path):
    """Validate JSON file is well-formed"""
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print(f"✓ {file_path} is valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {file_path} has invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"✗ Error validating {file_path}: {e}")
        return False

def validate_chess_data(file_path):
    """Validate chess data has required fields"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Check required top-level keys
        if 'champions' not in data or 'last_updated' not in data:
            print(f"✗ Chess data missing required fields")
            return False

        # Check champions array
        if not isinstance(data['champions'], list) or len(data['champions']) == 0:
            print(f"✗ Chess data has empty or invalid champions array")
            return False

        # Check each champion has required fields
        required_fields = ['name', 'title', 'country', 'ratings', 'max_rating']
        for champ in data['champions']:
            for field in required_fields:
                if field not in champ:
                    print(f"✗ Champion missing field: {field}")
                    return False

        print(f"✓ Chess data is valid ({len(data['champions'])} champions)")
        return True
    except Exception as e:
        print(f"✗ Error validating chess data: {e}")
        return False

def validate_builds_data(file_path):
    """Validate builds data has required fields"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        if 'builds' not in data or 'last_updated' not in data:
            print(f"✗ Builds data missing required fields")
            return False

        if not isinstance(data['builds'], list) or len(data['builds']) == 0:
            print(f"✗ Builds data has empty or invalid builds array")
            return False

        required_fields = ['name', 'class', 'difficulty', 'description', 'main_skill', 'rating']
        for build in data['builds']:
            for field in required_fields:
                if field not in build:
                    print(f"✗ Build missing field: {field}")
                    return False

        print(f"✓ Builds data is valid ({len(data['builds'])} builds)")
        return True
    except Exception as e:
        print(f"✗ Error validating builds data: {e}")
        return False

def validate_html(file_path):
    """Basic HTML validation (well-formedness)"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Check for basic HTML structure
        if '<html' not in content.lower() or '</html>' not in content.lower():
            print(f"✗ {file_path} missing HTML tags")
            return False

        if '<body' not in content.lower() or '</body>' not in content.lower():
            print(f"✗ {file_path} missing BODY tags")
            return False

        # Check for unclosed script tags in a simple way
        script_count = content.count('<script')
        script_close_count = content.count('</script>')
        if script_count != script_close_count:
            print(f"✗ {file_path} has mismatched script tags")
            return False

        print(f"✓ {file_path} is valid HTML")
        return True
    except Exception as e:
        print(f"✗ Error validating {file_path}: {e}")
        return False

def main():
    """Run all validations"""
    print("Running validation checks...\n")

    all_valid = True

    # Validate JSON data files
    print("Checking JSON data files:")
    data_files = {
        'data/chess-champions.json': validate_chess_data,
        'data/diablo4-builds.json': validate_builds_data,
    }

    for file_path, validator in data_files.items():
        if Path(file_path).exists():
            if not validator(file_path):
                all_valid = False
        else:
            print(f"⊘ {file_path} not found (skipping)")

    print("\nChecking HTML dashboards:")
    # Validate HTML files
    html_files = [
        'dashboards/chess-champions.html',
        'dashboards/diablo4-builds.html',
        'dashboards/weather.html',
        'index.html',
    ]

    for file_path in html_files:
        if Path(file_path).exists():
            if not validate_html(file_path):
                all_valid = False
        else:
            print(f"⊘ {file_path} not found (skipping)")

    print()
    if all_valid:
        print("✓ All validations passed!")
        sys.exit(0)
    else:
        print("✗ Some validations failed")
        sys.exit(1)

if __name__ == '__main__':
    main()
