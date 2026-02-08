#!/usr/bin/env python3
import argparse
import json
import platform
import shutil
import subprocess
from dataclasses import asdict, dataclass
from typing import List


@dataclass
class WifiNetwork:
    ssid: str
    bssid: str
    signal: str
    security: str
    frequency: str


def run_command(command: List[str]) -> str:
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Command failed")
    return result.stdout.strip()


def scan_with_nmcli() -> List[WifiNetwork]:
    output = run_command([
        "nmcli",
        "-t",
        "-f",
        "SSID,BSSID,SIGNAL,SECURITY,FREQ",
        "device",
        "wifi",
        "list",
    ])
    networks = []
    for line in output.splitlines():
        parts = line.split(":")
        if len(parts) < 5:
            continue
        ssid, bssid, signal, security, frequency = parts[:5]
        networks.append(
            WifiNetwork(
                ssid=ssid or "<hidden>",
                bssid=bssid,
                signal=signal,
                security=security or "open",
                frequency=frequency,
            )
        )
    return networks


def scan_with_airport() -> List[WifiNetwork]:
    output = run_command([
        "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
        "-s",
    ])
    networks = []
    for line in output.splitlines()[1:]:
        if not line.strip():
            continue
        ssid = line[:32].strip()
        rest = line[32:].split()
        if len(rest) < 4:
            continue
        bssid = rest[0]
        signal = rest[1]
        frequency = rest[2]
        security = " ".join(rest[3:])
        networks.append(
            WifiNetwork(
                ssid=ssid or "<hidden>",
                bssid=bssid,
                signal=signal,
                security=security,
                frequency=frequency,
            )
        )
    return networks


def scan_with_netsh() -> List[WifiNetwork]:
    output = run_command(["netsh", "wlan", "show", "networks", "mode=bssid"])
    networks = []
    current_ssid = ""
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("SSID "):
            current_ssid = stripped.split(":", 1)[-1].strip()
        elif stripped.startswith("BSSID "):
            bssid = stripped.split(":", 1)[-1].strip()
            networks.append(
                WifiNetwork(
                    ssid=current_ssid or "<hidden>",
                    bssid=bssid,
                    signal="unknown",
                    security="unknown",
                    frequency="unknown",
                )
            )
    return networks


def scan_wifi() -> List[WifiNetwork]:
    system = platform.system().lower()
    if shutil.which("nmcli"):
        return scan_with_nmcli()
    if system == "darwin":
        return scan_with_airport()
    if system == "windows":
        return scan_with_netsh()
    raise RuntimeError("No supported Wi-Fi scan command found on this system.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan nearby Wi-Fi networks.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON.",
    )
    args = parser.parse_args()

    networks = scan_wifi()
    if args.json:
        print(json.dumps([asdict(network) for network in networks], indent=2))
    else:
        for network in networks:
            print(
                f"{network.ssid} | {network.bssid} | {network.signal} | "
                f"{network.security} | {network.frequency}"
            )


if __name__ == "__main__":
    main()
