import csv

# load the data
def load_data(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8', errors='replace') as file: # change to gb18030 if unicodeencodeerror persists
        reader = csv.reader(file, delimiter='\t')
        # process your rows
        for row in reader:

            # check if the row has at least 9 fields
            if len(row) < 9:
                print(f"Skipping incomplete row: {row}")
                continue # skip rows that don't have enough columns

                # safely convert rate to a float
            try:
                rate_value = float(row[6])
            except ValueError:
                rate_value = 0.0

            # Map each row to a dictionary with appropriate column names
            data.append({
                'video_id': row[0],
                'uploader': row[1],
                'age': int(row[2]) if row[2].isdigit() else None,
                'category': row[3],
                'length': int(row[4]) if row[4].isdigit() else None,
                'views': int(row[5]) if row[5].isdigit() else None,
                'rate': rate_value,
                'ratings': int(row[7]) if row[7].isdigit() else None,
                'comments': int(row[8]) if row[8].isdigit() else None,
                'related_ids': row[9:] # related video IDs can be an array of IDs
            })
    return data

# remove duplicates
def remove_duplicates(data):
    seen = set()
    unique_data = []

    for row in data:
        if row['video_id'] not in seen:
            seen.add(row['video_id'])
            unique_data.append(row)
    return unique_data


# cleanse data
def clean_data(data):
    cleaned_data = []

    for row in data:
        try:
            # Handle missing or incorrect values by providing defaults
            row['views'] = row['views'] if row['views'] is not None else 0
            row['ratings'] = row['ratings'] if row['ratings'] is not None else 0
            row['comments'] = row['comments'] if row['comments'] is not None else 0
            row['rate'] = row['rate'] if row['rate'] is not None else 0.0
            row['length'] = row['length'] if row['length'] is not None else 0
            row['age'] = row['age'] if row['age'] is not None else 0

            # add cleansed row to final dataset
            cleaned_data.append(row)
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
            continue
    return cleaned_data

# save cleaned data to a new file
def save_cleaned_data(cleaned_data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8', errors='replace') as file:
        writer = csv.writer(file, delimiter='\t')
        for row in cleaned_data:
            writer.writerow([
                row['video_id'], row['uploader'], row['age'], row['category'],
                row['length'], row['views'], row['rate'], row['ratings'], row['comments'],
                *row['related_ids']
            ])

def main():
    # load the data
    data = load_data('tracks.csv')

    # remove duplicates
    data = remove_duplicates(data)

    # clean data
    cleaned_data = clean_data(data)

    # save cleaned data
    save_cleaned_data(cleaned_data, 'cleaned_tracks.csv')

if __name__ == '__main__':
    main()

