#!/usr/bin/env python3
"""Print the funniest auto-reply an AI ever sent."""

from pathlib import Path


def load_reply() -> str:
    here = Path(__file__).resolve().parent
    return (here / "entry.txt").read_text(encoding="utf-8").strip()


def render(reply: str) -> str:
    return reply.strip()


def main() -> None:
    print(render(load_reply()))


if __name__ == "__main__":
    main()
