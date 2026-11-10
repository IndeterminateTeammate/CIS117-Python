# CIS-117 Lab 3 
# This program will read a file of country names and filter them by region, i.e. Europe, Asia, Africa, etc.
# It will generate a new file for each region with the country names in that region. For example, Europe.CSV
# will contain all the countries in Europe, Asia.CSV will contain all the countries in Asia, etc. Each regions
# file will only contain the country names and region in each file.
# Name: Sean Fay
# Group: 9 
# Lab Partner: Gislaine Pires


import csv
import os
import sys


# .CSV read file function
def read_country_data(input_path):
    """
    Reads country_full.csv and returns a list of tuples.
    Includes exception handling for file reading errors.
    """
    records = []

    try:
        with open(input_path, mode="r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)

            if reader.fieldnames is None:
                raise ValueError("Input CSV is empty (no header row).")

            headers = {name.strip().lower(): name for name in reader.fieldnames}
            name_key = headers.get("name")
            region_key = headers.get("region")

            if name_key is None or region_key is None:
                raise ValueError(
                    "CSV must contain 'name' and 'region' columns. "
                    f"Found: {reader.fieldnames}"
                )

            for row in reader:
                country = (row.get(name_key) or "").strip()
                region = (row.get(region_key) or "").strip()

                if not country or not region:
                    continue

                records.append((country, region))
                
    except FileNotFoundError:
        print(f"ERROR: The file '{input_path}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"ERROR: Permission denied when reading '{input_path}'.")
        sys.exit(2)
    except Exception as e:
        print(f"ERROR reading file: {e}")
        sys.exit(3)

    return records


# File writing function
def write_region_files(records, output_dir="."):
    """
    Groups records by region and generates one .CSV file per region.
    Includes exception handling for file writing errors.
    """
    by_region = {}

    for country, region in records:
        if region not in by_region:
            by_region[region] = []
        by_region[region].append(country)

    written = []

    for region, countries in by_region.items():
        safe_region = region.replace(" ", "_")
        path = os.path.join(output_dir, f"{safe_region}.csv")

        try:
            with open(path, mode="w", newline="", encoding="utf-8") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(["Country", "Region"])
                
                for c in sorted(countries):
                    writer.writerow([c, region])
                    
            written.append(path)
            
        except PermissionError:
            print(f"ERROR: Permission denied when trying to write '{path}'.")
        except IOError as e:
            print(f"ERROR writing to '{path}': {e}")

    return written


# main method

def main():
    """
    Main function to read the input .CSV and write region-specific .CSV files.
    """
    # Designates the input file location and output directory for the region files
    input_path = "country_full.csv"
    output_dir = "."
    
    print("Starting program...")
    
    # Calls the read function
    all_records = read_country_data(input_path)
    print(f"Successfully loaded {len(all_records)} countries from CSV.")
    
    # Calls the write function
    files_created = write_region_files(all_records, output_dir)
    
    print(f"\nDone! Created {len(files_created)} region files:")
    for file in files_created:
        print(f" - {file}")


if __name__ == "__main__":
    main()