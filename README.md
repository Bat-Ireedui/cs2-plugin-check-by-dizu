# CS2 Plugin Version Checker

This repository tracks and monitors version updates for Counter-Strike 2 plugins.

_Last updated: just now_

## Monitored Plugins

The following plugins are being monitored for version updates:

### ✅ CounterStrikeSharp
- **Current Version**: 1.0.344
- **Last Updated**: 2 days ago
- **Repository**: [roflmuffin/CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp)

### ✅ CS2-Tags
- **Current Version**: build-37
- **Last Updated**: never
- **Repository**: [daffyyyy/CS2-Tags](https://github.com/daffyyyy/CS2-Tags)

### ✅ CS2-SimpleAdmin
- **Current Version**: build-1.7.8-beta-4
- **Last Updated**: 51 minutes ago
- **Repository**: [daffyyyy/CS2-SimpleAdmin](https://github.com/daffyyyy/CS2-SimpleAdmin)

### ✅ CS2_ExecAfter
- **Current Version**: 1.0.0
- **Last Updated**: never
- **Repository**: [kus/CS2_ExecAfter](https://github.com/kus/CS2_ExecAfter)

### ✅ MatchZy
- **Current Version**: 0.8.15
- **Last Updated**: never
- **Repository**: [shobhit-pathak/MatchZy](https://github.com/shobhit-pathak/MatchZy)

### ✅ WeaponPaints
- **Current Version**: build-399
- **Last Updated**: never
- **Repository**: [Nereziel/cs2-WeaponPaints](https://github.com/Nereziel/cs2-WeaponPaints)

### ✅ PlayerSettingsCore
- **Current Version**: 0.9.3
- **Last Updated**: never
- **Repository**: [NickFox007/PlayerSettingsCS2](https://github.com/NickFox007/PlayerSettingsCS2)

### ✅ MenuManagerCore
- **Current Version**: 1.4.1
- **Last Updated**: never
- **Repository**: [NickFox007/MenuManagerCS2](https://github.com/NickFox007/MenuManagerCS2)

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
