#!/usr/bin/env python3
import json, urllib.request, yaml, re
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

def update_readme(plugin_name, new_version):
    """Update the README.md file with the new version for a plugin"""
    try:
        with open("README.md", "r") as f:
            content = f.read()
        
        # Pattern to match the version line for the plugin
        # Handles various plugin name formats in README
        pattern = rf"(### ✅ {re.escape(plugin_name)}.*?- \*\*Current Version\*\*: )([^\n]+)"
        
        match = re.search(pattern, content, re.DOTALL)
        if match:
            updated_content = re.sub(pattern, rf"\g<1>{new_version}", content, flags=re.DOTALL)
            with open("README.md", "w") as f:
                f.write(updated_content)
            return True
    except Exception as e:
        print(f"Warning: Could not update README for {plugin_name}: {e}")
    return False

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

if errors:
    print("Errors checking the following plugins:\n")
    for name, error in errors:
        print(f"- {name}: {error}")
    print()

if outdated:
    print("Updates available:\n")
    for name, cur, new in outdated:
        print(f"- {name}: {cur} -> {new}")
    
    # Update versions.yml and README.md with new versions
    for name, cur, new in outdated:
        versions["plugins"][name]["current"] = new
        update_readme(name, new)
    
    # Save updated versions
    with open("versions.yml", "w") as f:
        yaml.safe_dump(versions, f, default_flow_style=False, sort_keys=False)
    
    print("\nVersions updated in versions.yml and README.md")
else:
    print("All plugins up to date.")
    # Still save the timestamp update even when no updates
    with open("versions.yml", "w") as f:
        yaml.safe_dump(versions, f, default_flow_style=False, sort_keys=False)
