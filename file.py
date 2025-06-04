import os
import sys
import platform
import subprocess

def get_system_uptime():
    """
    Returns the system uptime as a string.
    Works on Linux, macOS, and Windows.
    """
    if platform.system() == "Windows":
        # Windows: Use 'net stats srv', parse for 'Statistics since'
        try:
            output = subprocess.check_output("net stats srv", shell=True, encoding='utf-8')
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime (Windows): {line.strip()}"
            return "Could not determine uptime on Windows."
        except Exception as e:
            return f"Error fetching uptime on Windows: {e}"
    elif platform.system() == "Darwin":
        # macOS: Use 'uptime' command
        try:
            output = subprocess.check_output(["uptime"], encoding='utf-8')
            return f"System uptime (macOS): {output.strip()}"
        except Exception as e:
            return f"Error fetching uptime on macOS: {e}"
    else:
        # Assume Linux or Unix-like: Read /proc/uptime or use 'uptime'
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                return f"System uptime (Linux): {hours}h {minutes}m {seconds}s"
        except FileNotFoundError:
            try:
                output = subprocess.check_output(["uptime"], encoding='utf-8')
                return f"System uptime (Unix): {output.strip()}"
            except Exception as e:
                return f"Error fetching uptime on Unix: {e}"

if __name__ == "__main__":
    print(get_system_uptime())
