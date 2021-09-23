from typing import Dict, Generator, Literal, get_args
import csv
from typing_extensions import TypeGuard


HeadName = Literal[
    "PAGE", "SECTION", "MODIFICATION", "AUTHOR", "BEFORE", "AFTER", "URL"
]

head_names = get_args(HeadName)


def is_valid_row(row: Dict[str, str]) -> TypeGuard[Dict[HeadName, str]]:
    return all(row[name] != "" for name in head_names)


def load_issues() -> Generator[Dict[HeadName, str], None, None]:
    with open("./issues.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if not is_valid_row(row):
                raise Exception(
                    f"csv does not have all headers: {','.join(head_names)}"
                )

            yield row
