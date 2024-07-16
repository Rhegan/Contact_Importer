```markdown
# CSV to VCF Converter

This Python script converts contacts stored in a CSV file to a VCF (vCard) file.

## CSV Structure

To use this script, ensure your CSV file meets the following requirements:

- **Filename**: `contacts.csv`
- **Headers**: The CSV file should have the following headers with exact spelling and case:
  - `Address`
  - `Name`
  - `Surname`
  - `Phone`

### Example CSV

```csv
Address,Name,Surname,Phone
123 Main St,John,Doe,+27831234567
456 Elm St,Jane,Smith,0831234567
789 Oak St,Bob,Brown,27831234567
```

## Phone Number Formats

Phone numbers will be accepted in the following formats and will be converted to the international format `+27`:
- `+27831234567`
- `0831234567`
- `27831234567`

## Usage

### Running the Script

1. Ensure your CSV file is named `contacts.csv` and follows the specified structure.
2. Place the CSV file in the same directory as the script.
3. Run the script to generate a `contacts.vcf` file.

### Creating an Executable

To create an executable from the Python script, follow these steps:

1. **Install PyInstaller** (if not already installed):

    ```bash
    pip install pyinstaller
    ```

2. **Convert the Python script to an executable**:

    ```bash
    pyinstaller --onefile convert.py
    ```

### Using the Executable

1. Move the generated executable (`convert.exe`) into a folder with the `contacts.csv` file you want to convert.
2. Run the executable to generate a `contacts.vcf` file.
3. Move the `contacts.vcf` file out of the folder or rename it, as the converter will replace it on subsequent runs.

### Using the Batch File

For straightforward use, you can use a batch file to run the converter:

1. Create a batch file named `convert_contacts_to_vcf.bat`.
2. Place the batch file, executable, and `contacts.csv` in the same folder.
3. Double-click the batch file to run the converter.

## Notes

- Ensure there are no leading or trailing white spaces in the headers of the CSV file.
- The `contacts.csv` file must always be present in the same folder as the executable or script.

By following these instructions, you can easily convert your contacts from CSV to VCF format.
```