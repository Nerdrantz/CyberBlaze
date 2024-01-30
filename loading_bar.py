# loading_bar.py

import sys



def loading_bar(total, current):
    progress = int((current / total) * 100)
    bar_length = 40
    bar_progress = int((bar_length * progress) / 100)

    sys.stdout.write("\r[")
    sys.stdout.write("=" * bar_progress)
    sys.stdout.write(" " * (bar_length - bar_progress))
    sys.stdout.write(f"] {progress}%")

    if current == total:
        sys.stdout.write("\n")
    sys.stdout.flush()


def loading_bar_expeditions(total, remaining):
    progress = int(((total - remaining) / total) * 100)
    bar_length = 40
    bar_progress = int((bar_length * progress) / 100)

    print("\r[", end="")
    print("=" * bar_progress, end="")
    print(" " * (bar_length - bar_progress), end="")
    print(f"] {progress}%", end="")

    if remaining == 0:
        print("\n")
    sys.stdout.flush()