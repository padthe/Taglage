from fetch_data import fetch_train_announcements
from parse_data import parse_train_data
from print_data import print_train_data
from config import api_key


def main():
    data = fetch_train_announcements(api_key)
    if data:
        trains = parse_train_data(data)
        print_train_data(trains)


if __name__ == "__main__":
    main()
