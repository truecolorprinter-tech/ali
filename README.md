# Wi-Fi Scanner

A small command-line app that scans for nearby Wi-Fi networks using the OS tooling that is
already available on your machine.

## Usage

```bash
python3 wifi_scan.py
```

Output JSON instead:

```bash
python3 wifi_scan.py --json
```

## Requirements

- Linux: `nmcli` (NetworkManager)
- macOS: built-in `airport` tool
- Windows: `netsh`

If none of those tools are present, the script will exit with an error.
