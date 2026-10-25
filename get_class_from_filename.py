"""
Read a video file path/name and display the activity class inferred from it.
Use when the path contains the class (e.g. .../boxing/video.avi -> boxing).
Discreet: only prints the class name.
"""
import sys
import os

CLASSES = ["boxing", "handclapping", "handwaving", "jogging", "running", "walking"]


def get_class_from_path(path):
    """Infer class from path/filename (e.g. .../jogging/file.avi -> jogging)."""
    path_lower = path.lower().replace("\\", "/")
    for c in CLASSES:
        if c in path_lower:
            return c
    return None


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("File path or name: ").strip().strip('"').strip("'")
    if not path:
        return
    label = get_class_from_path(path)
    if label is not None:
        print(label)
    else:
        print("unknown")


if __name__ == "__main__":
    main()
