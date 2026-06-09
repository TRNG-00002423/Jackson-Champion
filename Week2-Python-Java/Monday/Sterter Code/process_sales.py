from __future__ import annotations
from pathlib import Path
import csv

"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").
"""


input_file = "sales.csv"
output_file = "summary.txt"
output_dir = Path("output")

def main() -> None:
    
    row_count = 0
    top_line_revenue = 0.0
    top_sku = None
    grand_total = 0.0
    bad_count = 0
    
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                units = int(row["units"])
                unit_price = float(row["unit_price"])
                sku = row["sku"]
                
                line_revenue = units * unit_price
                
                row_count += 1
                grand_total += line_revenue
                
                if top_sku is None or line_revenue > top_line_revenue:
                    top_sku = row["sku"]
                    top_line_revenue = line_revenue
                    
            except Exception (ValueError, KeyError) as e:
                print("Skipping Bad row: {row} {e}")
            
    if row_count > 0:
        average_line_revenue = grand_total / row_count
    else:
        average_line_revenue = 0.0

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"rows={row_count}\n")
        file.write(f"grand_total={grand_total:.2f}\n")
        file.write(f"average_line_revenue={average_line_revenue:.2f}\n")
        file.write(f"top_sku={top_sku}\n")
        file.write(f"top_line_revenue={top_line_revenue:.2f}\n")


if __name__ == "__main__":
    main()