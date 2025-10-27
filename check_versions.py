#!/usr/bin/env python3
import json, urllib.request, yaml

with open("versions.yml") as f:
    versions = yaml.safe_load(f)

outdated = []
for name, meta in versions["plugins"].items():
    req = urllib.request.urlopen(meta["repo"])
    data = json.load(req)
    latest = data["tag_name"].lstrip("v")
    current = str(meta["current"])
    if current != latest:
        outdated.append((name, current, latest))

if outdated:
    print("Updates available:\n")
    for name, cur, new in outdated:
        print(f"- {name}: {cur} -> {new}")
    exit(1)   # mark workflow as failing so you get notified
else:
    print("All plugins up to date.")
