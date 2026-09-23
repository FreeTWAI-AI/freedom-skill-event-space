"""Validate a public synthetic collaboration plan; never perform external actions."""
import json
import sys
from pathlib import Path


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["plan must be an object"]
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        errors.append("title is required")
    if data.get("data_classification") != "synthetic":
        errors.append("public examples must be synthetic; private records stay outside this repo")
    expected_kind = 'event-space'
    if data.get("kind") != expected_kind:
        errors.append("kind must be " + expected_kind)
    check(data, errors)
    return errors


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def records(data, key, errors):
    value = data.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, dict) for item in value):
        errors.append(key + " must contain at least one object")
        return []
    return value


def unique_ids(items, label, errors):
    identifiers = [item.get("id") for item in items]
    if any(not isinstance(value, str) or not value.strip() for value in identifiers):
        errors.append(label + " ids must be nonempty strings")
        return set()
    if len(set(identifiers)) != len(identifiers):
        errors.append(label + " ids must be unique")
    return set(identifiers)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def check(data, errors):
    count, capacity = data.get("expected_attendees"), data.get("venue_capacity")
    if not number(count) or not number(capacity) or count <= 0 or capacity <= 0 or int(count) != count or int(capacity) != capacity:
        errors.append("attendance and capacity must be positive integers")
    elif count > capacity:
        errors.append("attendance exceeds the stated venue capacity")
    roles = data.get("roles", [])
    if not isinstance(roles, list) or not all(text(role) for role in roles):
        errors.append("roles must be a list of nonempty names")
        roles = []
    end = 0
    for item in records(data, "agenda", errors):
        start, duration = item.get("start_minute"), item.get("duration_minutes")
        if not number(start) or not number(duration) or start < 0 or duration <= 0:
            errors.append("agenda timing must be nonnegative with a positive duration")
            continue
        if start < end:
            errors.append("agenda entries overlap or are out of order")
        end = start + duration
        if item.get("owner_role") not in roles:
            errors.append("each agenda item needs a listed owner role")
        if not text(item.get("title")):
            errors.append("agenda title is required")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 scripts/validate.py <plan.json>")
    try:
        problems = validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(str(error))
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("PASS: structural checks only; no real-world activity or results verified")
