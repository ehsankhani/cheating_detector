# Cheating Detection System

A comprehensive Python-based plagiarism detection system designed to identify similarities and potential cheating in programming assignments. The system uses multiple algorithms including text similarity, AST (Abstract Syntax Tree) comparison, machine learning, and various code analysis techniques to detect code plagiarism.

## Features

### Core Detection Algorithms
- **Text Similarity Analysis**: Uses difflib's SequenceMatcher for basic text comparison
- **AST Comparison**: Analyzes code structure by comparing normalized Abstract Syntax Trees
- **Tokenization Analysis**: Enhanced tokenizer for code comparison
- **Levenshtein Distance**: String similarity measurement for code comparison
- **Machine Learning Detection**: Trained ML model for intelligent plagiarism detection
- **Block Permutation Detection**: Detects reordered code blocks
- **Cyclomatic Complexity Analysis**: Measures code complexity patterns

### Advanced Features
- **Multi-feature Analysis**: Combines multiple detection methods for improved accuracy
- **Function and Variable Counting**: Analyzes code structure patterns
- **Comment Ratio Analysis**: Examines commenting patterns
- **GUI Interface**: User-friendly PyQt6-based graphical interface
- **Excel Export**: Generate detailed reports for instructors and students
- **Side-by-side Code Comparison**: Visual comparison dialog for detected similarities

### User Interface
- **Folder Selection**: Easy selection of homework directories
- **Real-time Detection**: Run detection analysis with progress feedback
- **Interactive Results**: Click on detection results to view detailed comparisons
- **Export Options**: Multiple export formats for different audiences

## Requirements

### Python Version
- Python 3.8 or higher (tested with Python 3.13.3)

### Dependencies

The required Python packages are listed in `requirements.txt`. Key dependencies include:
```
astunparse==1.6.3
colorama==0.4.6
et_xmlfile==2.0.0
joblib==1.5.1
mando==0.7.1
numpy==2.2.6
openpyxl==3.1.5
pandas==2.3.1
PyQt6==6.9.1
PyQt6-Qt6==6.9.1
PyQt6_sip==13.10.2
python-dateutil==2.9.0.post0
pytz==2025.2
radon==6.0.1
scikit-learn==1.7.1
scipy==1.15.3
six==1.17.0
threadpoolctl==3.6.0
tzdata==2025.2
xgboost==3.0.2
```

## Installation

First, clone the repository:
```bash
git clone <repository-url>
cd cheating-detection-system
```

You can set up the project environment using either `venv` or `conda`.

### Using venv

1.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

2.  **Activate the environment**:
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Using Conda

1.  **Create a conda environment**:
    ```bash
    conda create --name cheating-detector python=3.10 -y
    ```

2.  **Activate the environment**:
    ```bash
    conda activate cheating-detector
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

1. **Start the GUI application**:
   ```bash
   python main.py
   ```

2. **Using the Interface**:
   - Click "Select Folder" to choose a directory containing student submissions
   - Click "Run Detection" to analyze the files for similarities
   - Click on any result to view a detailed side-by-side comparison
   - Use "To Excel" to export detailed results for instructors
   - Use "Excel for students" to export student-friendly reports

### File Structure Requirements

The system expects Python files (.py) in the selected folder with the naming convention:
```
StudentName_StudentID.py
```

Example:
```
john_doe_12345.py
jane_smith_67890.py
```

### Command Line Usage

For programmatic usage, you can import and use the detection classes:

```python
from algorithms.cheating_detector import CheatingDetector

# Initialize detector with folder path
detector = CheatingDetector("/path/to/homework/folder")

# Run analysis
results = detector.analyze()

# Get detailed report
report = detector.get_cheating_report()
```

## Project Structure

```
├── main.py                          # Main GUI application entry point
├── algorithms/                      # Core detection algorithms
│   ├── cheating_detector.py        # Main detection coordinator
│   ├── similarity_detector.py      # Text similarity analysis
│   ├── ast_comparator.py          # AST-based code structure comparison
│   ├── tokenizer.py               # Enhanced tokenization for code analysis
│   ├── levenshtein.py             # Levenshtein distance calculation
│   ├── extra_features.py          # Additional feature extraction
│   ├── block_permutation_detector.py # Detects reordered code blocks
│   ├── code_comparison_dialog.py   # GUI dialog for code comparison
│   └── ML/                        # Machine learning components
│       ├── cheating_detector_model.pkl # Trained ML model
│       ├── scaler.pkl             # Feature scaler
│       ├── extract_features.py    # Feature extraction for ML
│       └── dump_model.py          # Model training script
├── utils/                          # Utility modules
│   ├── file_reader.py             # File reading utilities
│   └── excel_exporter.py          # Excel export functionality
├── homeworks/                      # Sample homework files for testing
├── DataSet/                        # Training dataset and submissions
│   ├── cheating_dataset.csv       # Labeled training data
│   ├── cheating_features_dataset.csv # Feature-based training data
│   └── submission*.py             # Sample submissions (174 files)
└── outputs/                        # Generated reports and outputs
    ├── student.xlsx               # Student report
    └── test.xlsx                  # Test report
```

## Algorithm Details

### 1. Text Similarity Detection
- Uses Python's `difflib.SequenceMatcher`
- Calculates similarity ratio between code files
- Threshold: 0.5 (50% similarity triggers detection)

### 2. AST Comparison
- Parses code into Abstract Syntax Trees
- Normalizes variable and function names
- Compares structural similarity regardless of naming

### 3. Machine Learning Detection
- Trained model using scikit-learn
- Features include:
  - AST similarity scores
  - Token similarity scores
  - Levenshtein distances
  - Function/variable counts
  - Comment ratios
  - Cyclomatic complexity

### 4. Enhanced Tokenization
- Advanced tokenization specifically designed for code analysis
- Handles programming language constructs effectively

### 5. Block Permutation Detection
- Identifies cases where code blocks have been reordered
- Useful for detecting sophisticated plagiarism attempts

## Export Features

### Instructor Report
- Detailed similarity scores for all algorithm types
- Student identification information
- Confidence levels and recommendations
- Comprehensive analysis results

### Student Report
- Student-friendly format
- Summary of findings
- Guidance for academic integrity

## Dataset Information

The system includes a comprehensive dataset with:
- **174 sample submissions** for testing and validation
- **Labeled training data** with binary classification (cheating/not cheating)
- **Feature-based dataset** for machine learning model training

## Configuration

### Detection Thresholds
You can modify detection sensitivity by adjusting thresholds in:
- `algorithms/similarity_detector.py` - Text similarity threshold
- `algorithms/cheating_detector.py` - ML model confidence threshold

### ML Model Retraining
To retrain the machine learning model:
1. Prepare your labeled dataset in CSV format
2. Run `algorithms/ML/dump_model.py`
3. The new model will be saved automatically

## Troubleshooting

### Common Issues

1. **PyQt6 Installation Issues**:
   ```bash
   pip install --upgrade pip
   pip install PyQt6
   ```

2. **File Permission Errors**:
   - Ensure the selected folder has read permissions
   - Check that output directory is writable

3. **Memory Issues with Large Datasets**:
   - Process files in smaller batches
   - Increase system memory allocation

### Performance Optimization

- For large datasets, consider processing files in batches
- The system performs best with 10-100 files per analysis
- ML model inference is optimized for real-time detection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is designed for educational purposes and academic integrity enforcement.

## Academic Integrity Note

This tool is designed to assist educators in maintaining academic integrity. It should be used as part of a comprehensive approach to preventing and detecting plagiarism, not as the sole method of determination.

## Support

For issues, questions, or contributions, please refer to the project documentation or contact the development team.

---

**Note**: This system is designed for educational environments and should be used responsibly in accordance with institutional policies on academic integrity.
**p.s:** for further and complete information you can use *project report.pdf*; its complete and structured report about the cheating detector system in persian.