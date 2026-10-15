"""Programme de départ public, volontairement limité au français."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Salutation de démonstration.")
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    print(f"Bonjour, {args.name}!")


if __name__ == "__main__":
    main()
