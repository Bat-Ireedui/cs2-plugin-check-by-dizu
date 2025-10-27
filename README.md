# CS2 Plugin Version Checker

This repository tracks and monitors version updates for Counter-Strike 2 plugins.

## Monitored Plugins

The following plugins are being monitored for version updates:

### ✅ CounterStrikeSharp
- **Current Version**: 1.0.343
- **Repository**: [roflmuffin/CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp)

### ✅ CS2-Tags
- **Current Version**: 1.0.4c
- **Repository**: [daffyy/cs2-tags](https://github.com/daffyy/cs2-tags)

### ✅ CS2-SimpleAdmin
- **Current Version**: 1.7.8-beta-3
- **Repository**: [dliix66/cs2-simpleadmin](https://github.com/dliix66/cs2-simpleadmin)

### ✅ CS2_ExecAfter
- **Current Version**: 1.0.0
- **Repository**: [kus/cs2-exec-after](https://github.com/kus/cs2-exec-after)

### ✅ MatchZy
- **Current Version**: 0.8.15
- **Repository**: [shobhit-pathak/MatchZy](https://github.com/shobhit-pathak/MatchZy)

### ✅ WeaponPaints
- **Current Version**: 3.2a
- **Repository**: [Nereziel/cs2-weaponpaints](https://github.com/Nereziel/cs2-weaponpaints)

### ✅ PlayerSettingsCore
- **Current Version**: 0.9.3
- **Repository**: [NickFox/cs2-playersettings](https://github.com/NickFox/cs2-playersettings)

### ✅ MenuManagerCore
- **Current Version**: 1.4.1
- **Repository**: [NickFox/cs2-menumanager](https://github.com/NickFox/cs2-menumanager)

## Automatic Monitoring

The repository uses GitHub Actions to automatically check for plugin updates every 20 minutes. When a new version is detected, the workflow will fail to notify you.

### Status Badge

[![Check plugin versions](https://github.com/Bat-Ireedui/cs2-plugin-check-by-dizu/actions/workflows/check.yml/badge.svg)](https://github.com/Bat-Ireedui/cs2-plugin-check-by-dizu/actions/workflows/check.yml)

## How It Works

1. The `check.yml` workflow runs every 20 minutes (or can be triggered manually)
2. It reads plugin information from `versions.yml`
3. Compares current versions with the latest releases on GitHub
4. Reports any outdated plugins

## Update a Plugin Version

To update a plugin version, edit the `versions.yml` file and update the `current` field for the relevant plugin.
