import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from js import window, document
from pyodide.ffi import create_proxy
import warnings

warnings.filterwarnings('ignore')

def calculate_statistics(data):
    """Calculate descriptive statistics for the marks data."""
    stats = {
        'Count': len(data),
        'Mean': np.mean(data),
        'Median': np.median(data),
        'Std Dev': np.std(data, ddof=1),
        'Min': np.min(data),
        'Max': np.max(data),
        'Q1': np.percentile(data, 25),
        'Q3': np.percentile(data, 75),
    }
    return stats

def create_histogram(data):
    """Create a histogram using matplotlib."""
    plt.figure(figsize=(10, 6))
    
    # Create histogram
    n, bins, patches = plt.hist(data, bins=20, edgecolor='black', alpha=0.7, 
                                 color='#667eea')
    
    # Customize the plot
    plt.xlabel('Marks (%)', fontsize=12, fontweight='bold')
    plt.ylabel('Frequency', fontsize=12, fontweight='bold')
    plt.title('Distribution of Marks', fontsize=14, fontweight='bold', pad=20)
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Add mean and median lines
    mean_val = np.mean(data)
    median_val = np.median(data)
    
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {mean_val:.2f}%')
    plt.axvline(median_val, color='green', linestyle='--', linewidth=2, 
                label=f'Median: {median_val:.2f}%')
    
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    # Display the plot
    display(plt, target="histogram")
    plt.close()

def display_statistics(stats):
    """Display statistics as cards in the HTML."""
    stats_html = ""
    
    for label, value in stats.items():
        if label in ['Count']:
            formatted_value = f"{int(value)}"
        else:
            formatted_value = f"{value:.2f}"
            if label not in ['Std Dev']:
                formatted_value += "%"
        
        stats_html += f"""
        <div class="stat-card">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{formatted_value}</div>
        </div>
        """
    
    stats_grid = document.getElementById('stats-grid')
    stats_grid.innerHTML = stats_html

def validate_csv_data(df):
    """Validate the CSV data format and content."""
    if df.shape[1] < 2:
        raise ValueError("CSV must contain at least 2 columns (Index and Marks)")
    
    # Use the second column as marks data
    marks_column = df.iloc[:, 1]
    
    # Try to convert to numeric
    try:
        marks_data = pd.to_numeric(marks_column, errors='coerce')
    except Exception as e:
        raise ValueError(f"Could not parse marks data: {str(e)}")
    
    # Check for NaN values
    if marks_data.isna().any():
        nan_count = marks_data.isna().sum()
        raise ValueError(f"Found {nan_count} invalid/missing values in marks column")
    
    # Check if values are reasonable for percentages
    if marks_data.min() < 0 or marks_data.max() > 100:
        raise ValueError("Marks should be between 0 and 100 (percentages)")
    
    if len(marks_data) == 0:
        raise ValueError("No valid data found in the CSV file")
    
    return marks_data.values

def process_csv(csv_content):
    """Main function to process CSV and display results."""
    try:
        # Parse CSV content
        df = pd.read_csv(StringIO(csv_content))
        
        # Validate and extract marks data
        marks_data = validate_csv_data(df)
        
        # Calculate statistics
        stats = calculate_statistics(marks_data)
        
        # Display statistics
        display_statistics(stats)
        
        # Create and display histogram
        create_histogram(marks_data)
        
        # Show results section
        results_div = document.getElementById('results')
        results_div.style.display = 'block'
        
        # Hide loading and show success message
        window.showLoading(False)
        window.showSuccess(f"Successfully processed {len(marks_data)} records!")
        
    except Exception as e:
        window.showLoading(False)
        window.showError(f"Error: {str(e)}")
        print(f"Error details: {str(e)}")

# Create a proxy for the process_csv function to be called from JavaScript
process_csv_proxy = create_proxy(process_csv)

# Make the function available to JavaScript
window.processCSV = process_csv_proxy
