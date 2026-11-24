#!/usr/bin/env python3

import platform
import os
import random
import argparse

FACES = [
    "¯*\\_*(ツ)_/¯",
    "ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧",
    "(˶>⩊<˶)",
    "(ᵕ—ᴗ—)",
    "( ◡̀  ̫ ◡́) ✧",
    "૮(◞ ‸ ◟ )ა",
    "(⸝⸝๑﹏๑⸝⸝)",
    "(¬`‸´¬)",
    "〜(꒪꒳꒪)〜",
    ".·°՞(っ-ᯅ-ς)՞°·.",
    "₍^ >⩊< ^₎Ⳋ",
    "(╯˙ᵕ˙ )╯︵ ┻━┻",
    "(｡•̀ ⤙ •́ ｡ꐦ)"
]


def get_distro():
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as file:
            for line in file:
                if line.startswith("PRETTY_NAME="):
                    return line.split("=", 1)[1].strip().strip('"')

    return platform.system()


def get_cpu_info():
    model = "Unknown"

    if os.path.exists("/proc/cpuinfo"):
        with open("/proc/cpuinfo", "r") as file:
            for line in file:
                if line.startswith("model name"):
                    model = line.split(":", 1)[1].strip()
                    break

    cores = os.cpu_count() or 0

    return model, cores


def get_short_cpu_name(full_model):
    if "Intel" in full_model:
        for prefix in ["i3-", "i5-", "i7-", "i9-"]:
            if prefix in full_model:
                return prefix + full_model.split(prefix, 1)[1].split()[0]

    if "Ryzen" in full_model:
        return "Ryzen " + full_model.split("Ryzen ", 1)[1].split()[0]

    return full_model


def get_ram_info():
    if not os.path.exists("/proc/meminfo"):
        return None, None, None

    meminfo = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":", 1)
            meminfo[key] = int(value.strip().split()[0])

    total = meminfo["MemTotal"]
    available = meminfo["MemAvailable"]
    used = total - available

    # Convertir de KB a GB
    total = round(total / 1024 / 1024, 2)
    used = round(used / 1024 / 1024, 2)
    available = round(available / 1024 / 1024, 2)

    return total, used, available


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="System information tool"
    )

    parser.add_argument(
        "-s", "--short",
        action="store_true",
        help="Show short system information"
    )

    return parser.parse_args()


def get_system_info(short=False):
    cpu_model, cpu_cores = get_cpu_info()
    ram_total, ram_used, ram_available = get_ram_info()

    print()
    print("       " + random.choice(FACES))
    print()

    print("distro:", get_distro())

    if not short:
        print("sys:", platform.system())
        print("host:", platform.node())

    if short:
        cpu_model = get_short_cpu_name(cpu_model)

    print("cpu:", cpu_model)

    if not short:
        print("cores:", cpu_cores)

    # RAM utilitzada / total
    if ram_total is not None:
        print(f"ram: {ram_used}/{ram_total} GB")
    else:
        print("ram: unavailable")


if __name__ == "__main__":
    args = parse_arguments()
    get_system_info(short=args.short)
