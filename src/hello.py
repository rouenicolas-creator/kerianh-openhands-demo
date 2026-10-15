"""Programme de départ public, avec salutation en français ou en anglais."""

import argparse

GREETINGS = {"fr": "Bonjour", "en": "Hello"}


def main():
    parser = argparse.ArgumentParser(description="Salutation de démonstration.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--lang", choices=("fr", "en"), default="fr")
    args = parser.parse_args()
    print(f"{GREETINGS[args.lang]}, {args.name}!")


if __name__ == "__main__":
    main()
