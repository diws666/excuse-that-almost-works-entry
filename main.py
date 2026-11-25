import os

ENTRY_TEXT = "Sorry boss, the plumber is coming to fix the leak under my sink sometime between 9 and 5."


def entry_line() -> str:
    return ENTRY_TEXT


def write_entry(output_dir: str) -> None:
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry_line())


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
