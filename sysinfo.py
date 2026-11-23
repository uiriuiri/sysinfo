
#!/usr/bin/env python3

import platform
import os


def get_distro():
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as file:
            for line in file:
                if line.startswith("PRETTY_NAME="):
                    return line.split("=")[1].strip().strip('"')

    return "Unknown"


def get_system_info():
    print("==========================")
    print("        SYSINFO")
    print("==========================")

    print("Distribution:", get_distro())
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Hostname:", platform.node())


if __name__ == "__main__":
    get_system_info()
