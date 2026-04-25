import pandas as pd
import sys

def analyze_inventory(filepath):
    """
    Analyze inventory data to identify items below reorder threshold.
    Handles missing and inconsistent data gracefully.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(filepath)
        
        # Clean and convert stock_level to numeric, coercing errors to NaN
        df['stock_level'] = pd.to_numeric(df['stock_level'], errors='coerce')
        
        # Filter for items below reorder threshold
        below_threshold = df[df['stock_level'] < df['reorder_threshold']]
        
        # Display results
        print("=" * 60)
        print("SUPPLY CHAIN RISK ANALYSIS - ITEMS REQUIRING REORDER")
        print("=" * 60)
        
        if below_threshold.empty:
            print("No items below reorder threshold.")
        else:
            print(f"\nFound {len(below_threshold)} items that need reordering:\n")
            print(f"{'Product ID':<12} {'Category':<15} {'Stock Level':<15} {'Threshold':<12}")
            print("-" * 60)
            
            for _, row in below_threshold.iterrows():
                stock = row['stock_level']
                # Handle NaN values for display
                stock_display = f"{stock:.0f}" if pd.notna(stock) else "N/A"
                print(f"{row['product_id']:<12} {row['category']:<15} {stock_display:<15} {row['reorder_threshold']:<12}")
        
        print("\n" + "=" * 60)
        return below_threshold
        
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Analyze the inventory
    analyze_inventory('inventory_data.csv')