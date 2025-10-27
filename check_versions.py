#!/usr/bin/env python3
import json, urllib.request, yaml
from datetime import datetime, timezone

def format_time_ago(timestamp):
    """Format a timestamp as 'XX minutes ago' or 'XX hours ago'"""
    if not timestamp:
        return "never"
    
    try:
        last_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        diff = now - last_time
        
        minutes = int(diff.total_seconds() / 60)
        hours = int(diff.total_seconds() / 3600)
        days = int(diff.total_seconds() / 86400)
        
        if minutes < 1:
            return "just now"
        elif minutes < 60:
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        elif hours < 24:
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        else:
            return f"{days} day{'s' if days != 1 else ''} ago"
    except:
        return "unknown"

with open("versions.yml") as f:
    versions = yaml.safe_load(f)

# Display last check time if available
last_checked = versions.get("last_checked")
if last_checked:
    time_ago = format_time_ago(last_checked)
    print(f"Last checked: {time_ago}\n")

outdated = []
errors = []
for name, meta in versions["plugins"].items():
    try:
        req = urllib.request.Request(meta["repo"])
        req.add_header('User-Agent', 'CS2-Plugin-Version-Checker')
        req.add_header('Accept', 'application/vnd.github.v3+json')
        response = urllib.request.urlopen(req)
        data = json.load(response)
        latest = data["tag_name"].lstrip("v")
        current = str(meta["current"])
        if current != latest:
            outdated.append((name, current, latest))
    except urllib.error.HTTPError as e:
        errors.append((name, f"HTTP {e.code}: {e.reason}"))
    except Exception as e:
        errors.append((name, str(e)))

# Update last_checked timestamp
versions["last_checked"] = datetime.now(timezone.utc).isoformat()
with open("versions.yml", "w") as f:
    yaml.safe_dump(versions, f, default_flow_style=False, sort_keys=False)

if errors:
    print("Errors checking the following plugins:\n")
    for name, error in errors:
        print(f"- {name}: {error}")
    print()

if outdated:
    print("Updates available:\n")
    for name, cur, new in outdated:
        print(f"- {name}: {cur} -> {new}")
    exit(1)   # mark workflow as failing so you get notified
else:
    print("All plugins up to date.")
