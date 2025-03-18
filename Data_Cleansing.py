import csv

def load_data(file_name):
    """
    Load data from the CSV file while preserving the original format.
    Skips empty rows and rows that do not match the header length.
    Returns the header, a list of valid rows, and the detected CSV dialect.
    """
    data = []
    with open(file_name, 'r', newline='', encoding='utf-8', errors='replace') as file:
        # Read a sample to detect the dialect
        sample = file.read(1024)
        file.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            # Fallback to a default dialect if detection fails
            dialect = csv.get_dialect('excel')

        reader = csv.reader(file, dialect)

        try:
            header = next(reader)
        except StopIteration:
            print("Empty file.")
            return [], data, dialect

        for row in reader:
            # Skip completely empty rows.
            if not row or all(cell.strip() == "" for cell in row):
                print("Skipping empty row:", row)
                continue

            # Skip rows that do not match the header's column count.
            if len(row) != len(header):
                print("Skipping inconsistent row:", row)
                continue

            data.append(row)
    return header, data, dialect

def remove_duplicates(data):
    """
    Remove duplicate rows based on the entire row.
    """
    seen = set()
    unique_data = []
    for row in data:
        key = tuple(row)
        if key not in seen:
            seen.add(key)
            unique_data.append(row)
    return unique_data

def save_cleaned_data(header, data, output_file, dialect):
    """
    Save the cleaned data to a new CSV file using the same dialect.
    Creates a custom dialect using type() to ensure all attributes are set.
    """
    CustomDialect = type("CustomDialect", (csv.Dialect,), {
        "delimiter": dialect.delimiter if dialect.delimiter is not None else ',',
        "quotechar": dialect.quotechar if dialect.quotechar is not None else '"',
        "doublequote": dialect.doublequote if dialect.doublequote is not None else True,
        "skipinitialspace": dialect.skipinitialspace if dialect.skipinitialspace is not None else False,
        "lineterminator": dialect.lineterminator if dialect.lineterminator is not None else "\n",
        "quoting": dialect.quoting if dialect.quoting is not None else csv.QUOTE_MINIMAL,
        "escapechar": '\\' if (dialect.quoting == csv.QUOTE_NONE or dialect.escapechar is None) else dialect.escapechar
    })

    with open(output_file, 'w', newline='', encoding='utf-8', errors='replace') as file:
        writer = csv.writer(file, dialect=CustomDialect)
        writer.writerow(header)
        writer.writerows(data)

def main():
    # Load data from echonest.csv
    header, data, dialect = load_data('tracks.csv')

    if not header:
        print("No header found. Exiting.")
        return

    print(f"Loaded {len(data)} rows (excluding header).")

    # Remove duplicate rows.
    unique_data = remove_duplicates(data)
    print(f"Data after duplicate removal: {len(unique_data)} rows.")

    # Save the cleaned data to a new CSV file.
    save_cleaned_data(header, unique_data, 'cleaned_tracks.csv', dialect)

if __name__ == '__main__':
    main()
