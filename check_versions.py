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

def update_readme(updates_dict, versions):
    """Update the README.md file with new versions for multiple plugins
    
    Args:
        updates_dict: Dictionary mapping plugin names to new versions
        versions: The versions dictionary containing plugin metadata
    
    Returns:
        Dictionary mapping plugin names to boolean success status
    """
    results = {}
    try:
        with open("README.md", "r") as f:
            content = f.read()
        
        original_content = content
        
        # Update README last updated timestamp
        readme_updated_pattern = r"(_Last updated: )([^_\n]+)(_)"
        readme_time_ago = format_time_ago(versions.get("last_checked"))
        content = re.sub(readme_updated_pattern, rf"\g<1>{readme_time_ago}\g<3>", content)
        
        # Apply all updates to the content
        for plugin_name, new_version in updates_dict.items():
            # Pattern to match the version line for the plugin
            pattern = rf"(### ✅ {re.escape(plugin_name)}.*?- \*\*Current Version\*\*: )([^\n]+)"
            
            # Use re.sub and check if content changed to determine success
            updated_content = re.sub(pattern, rf"\g<1>{new_version}", content, flags=re.DOTALL)
            
            if updated_content != content:
                content = updated_content
                results[plugin_name] = True
            else:
                print(f"Warning: Plugin '{plugin_name}' not found in README.md")
                results[plugin_name] = False
        
        # Update last_updated timestamp for each plugin
        for plugin_name in versions["plugins"].keys():
            last_updated = versions["plugins"][plugin_name].get("last_updated")
            time_ago = format_time_ago(last_updated)
            
            # Pattern to match the last updated line for the plugin
            pattern = rf"(### ✅ {re.escape(plugin_name)}.*?- \*\*Last Updated\*\*: )([^\n]+)"
            content = re.sub(pattern, rf"\g<1>{time_ago}", content, flags=re.DOTALL)
        
        # Only write the file if content changed
        if content != original_content:
            with open("README.md", "w") as f:
                f.write(content)
            
    except Exception as e:
        print(f"Error updating README: {e}")
        for plugin_name in updates_dict:
            results[plugin_name] = False
    
    return results

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
    
    # Update versions.yml with new versions and last_updated timestamps
    updates_dict = {}
    current_time = datetime.now(timezone.utc).isoformat()
    for name, cur, new in outdated:
        versions["plugins"][name]["current"] = new
        versions["plugins"][name]["last_updated"] = current_time
        updates_dict[name] = new
    
    # Update README.md with all new versions at once
    readme_results = update_readme(updates_dict, versions)
    
    # Save updated versions
    with open("versions.yml", "w") as f:
        yaml.safe_dump(versions, f, default_flow_style=False, sort_keys=False)
    
    print("\nVersions updated in versions.yml")
    
    # Report README update results
    readme_updated = [name for name, success in readme_results.items() if success]
    readme_failed = [name for name, success in readme_results.items() if not success]
    
    if readme_updated:
        print(f"README.md updated for: {', '.join(readme_updated)}")
    if readme_failed:
        print(f"README.md not updated for: {', '.join(readme_failed)} (plugin sections not found in README)")
else:
    print("All plugins up to date.")
    # Still update README with latest timestamps even when no version updates
    update_readme({}, versions)
    # Still save the timestamp update even when no updates
    with open("versions.yml", "w") as f:
        yaml.safe_dump(versions, f, default_flow_style=False, sort_keys=False)
