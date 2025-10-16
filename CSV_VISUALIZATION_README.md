# CSV Data Visualization - PyScript Web Application

A browser-based web application built with PyScript that allows users to upload CSV files containing marks data and visualize the distribution with an interactive histogram along with comprehensive statistical analysis.

## Features

### 📤 File Upload
- **Drag-and-Drop Interface**: Simply drag your CSV file onto the drop zone
- **File Browser**: Alternative option to browse and select files from your computer
- **Real-time Validation**: Immediate feedback on file format and data validity

### 📊 Data Visualization
- **Interactive Histogram**: Visual representation of marks distribution
- **Mean and Median Lines**: Overlay showing central tendency measures
- **Professional Styling**: Clean, modern interface with gradient themes

### 📈 Statistical Analysis
Displays the following descriptive statistics in attractive cards:
- **Count**: Total number of entries
- **Mean**: Average marks
- **Median**: Middle value of the distribution
- **Standard Deviation**: Measure of data spread
- **Minimum**: Lowest mark
- **Maximum**: Highest mark
- **Q1**: First quartile (25th percentile)
- **Q3**: Third quartile (75th percentile)

## Usage

### 1. Open the Application
Simply open the `csv_visualization.html` file in a modern web browser (Chrome, Firefox, Edge, or Safari).

**Note**: The application runs entirely in your browser - no server or installation required!

### 2. Prepare Your CSV File
Your CSV file should have the following format:
```csv
Index,Marks
1,85.5
2,92.0
3,78.5
...
```

**Requirements**:
- Two columns: Index (any identifier) and Marks (percentage values)
- Marks should be numeric values between 0 and 100
- No missing values in the marks column

### 3. Upload Your Data
- **Option A**: Drag and drop your CSV file onto the designated drop zone
- **Option B**: Click the "Browse Files" button and select your CSV file

### 4. View Results
Once uploaded, the application will:
1. Validate your data
2. Calculate statistical metrics
3. Display statistics in colorful cards
4. Generate and show a histogram with mean/median lines

## Sample Data

A sample CSV file (`sample_marks.csv`) is included with 50 student marks ranging from 75% to 96.5%. Use this to test the application.

## Technical Details

### Technologies Used
- **PyScript**: Python runtime in the browser
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Histogram generation
- **HTML/CSS/JavaScript**: Frontend interface

### Browser Compatibility
- Chrome 90+
- Firefox 90+
- Safari 14+
- Edge 90+

### Data Processing
The application:
1. Parses CSV content using pandas
2. Validates data format and ranges
3. Calculates statistics using numpy
4. Generates visualizations with matplotlib
5. Renders everything client-side (no server needed)

## Error Handling

The application includes comprehensive error handling for:
- Invalid file formats (non-CSV files)
- Missing or malformed data
- Values outside the 0-100 range
- Empty files
- Incorrect column structure

Error messages are displayed in a user-friendly format with specific details about what went wrong.

## Files

- `csv_visualization.html`: Main application file with HTML structure and styling
- `csv_analyzer.py`: Python script containing data processing and visualization logic
- `sample_marks.csv`: Sample data file for testing
- `CSV_VISUALIZATION_README.md`: This documentation file

## Development

### Modifying the Application

**To change the histogram appearance**, edit the `create_histogram()` function in `csv_analyzer.py`:
```python
def create_histogram(data):
    plt.figure(figsize=(10, 6))
    # Modify bins, colors, etc.
    n, bins, patches = plt.hist(data, bins=20, color='#667eea')
```

**To add more statistics**, update the `calculate_statistics()` function:
```python
def calculate_statistics(data):
    stats = {
        'Count': len(data),
        'Mean': np.mean(data),
        # Add your new statistics here
        'IQR': np.percentile(data, 75) - np.percentile(data, 25),
    }
    return stats
```

**To modify styling**, edit the `<style>` section in `csv_visualization.html`.

## Limitations

- Requires modern browser with WebAssembly support
- Initial load may take a few seconds as PyScript and packages are loaded
- Large CSV files (>10,000 rows) may take longer to process
- Runs entirely client-side - no data is sent to any server

## Privacy

All data processing happens entirely in your browser. No data is uploaded to any server, ensuring complete privacy and security of your data.

## License

This project is part of the bayesianLinearFit repository. Use freely for educational and research purposes.

## Support

For issues or questions, please refer to the main repository's issue tracker.

## Future Enhancements

Potential features for future versions:
- Support for multiple columns/datasets
- More chart types (box plots, scatter plots)
- Data filtering and transformation options
- Export results as PDF or images
- Comparison between multiple CSV files
- Advanced statistical tests
