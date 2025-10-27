# CS2 Plugin Version Checker

This repository tracks and monitors version updates for Counter-Strike 2 plugins.

## Monitored Plugins

The following plugins are being monitored for version updates:

### ✅ CounterStrikeSharp
- **Current Version**: 1.0.343
- **Repository**: [roflmuffin/CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp)

### ✅ CS2-SimpleAdmin
- **Current Version**: build-1.7.8-beta-3
- **Repository**: [dliix66/cs2-simpleadmin](https://github.com/dliix66/cs2-simpleadmin)

### ✅ MatchZy
- **Current Version**: 0.8.15
- **Repository**: [shobhit-pathak/MatchZy](https://github.com/shobhit-pathak/MatchZy)

### ✅ WeaponPaints
- **Current Version**: build-399
- **Repository**: [Nereziel/cs2-weaponpaints](https://github.com/Nereziel/cs2-weaponpaints)

## Automatic Monitoring

The repository uses GitHub Actions to automatically check for plugin updates every 20 minutes. When a new version is detected, the workflow will automatically update the version information in both `versions.yml` and this README file.

### Status Badge

[![Check plugin versions](https://github.com/Bat-Ireedui/cs2-plugin-check-by-dizu/actions/workflows/check.yml/badge.svg)](https://github.com/Bat-Ireedui/cs2-plugin-check-by-dizu/actions/workflows/check.yml)

## How It Works

1. The `check.yml` workflow runs every 20 minutes (or can be triggered manually)
2. It reads plugin information from `versions.yml`
3. Compares current versions with the latest releases on GitHub
4. Automatically updates `versions.yml` and `README.md` when new versions are detected
5. Commits and pushes the changes back to the repository

## Update a Plugin Version

Plugin versions are automatically updated by the workflow when new releases are detected on GitHub. You can also manually update a plugin version by editing the `versions.yml` file and updating the `current` field for the relevant plugin.
