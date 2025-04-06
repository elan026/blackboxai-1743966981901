


---

```markdown
# License Plate Detection Web Application

## Project Overview

This project is a web application built using Flask that allows users to upload images of vehicles, and it detects and extracts license plate information using Optical Character Recognition (OCR). The license plate detection is implemented using OpenCV and Tesseract.

## Installation

To set up the project on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Tesseract OCR (must be installed and configured)

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Install Dependencies

You can install the required Python packages using pip. Create a virtual environment and then install the packages listed below:

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt
```

### Install Tesseract

You need to install Tesseract OCR for the text recognition part of the application. Follow the installation instructions on the official [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).

### Configure Tesseract

Make sure Tesseract is added to your system's PATH. You can verify this by running `tesseract -v` in your terminal.

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
   
2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Upload an image containing a vehicle license plate and click on the submit button.

4. The application will return the detected license plate text and its coordinates.

## Features

- **Image Upload:** Users can upload images with .png, .jpg, or .jpeg formats.
- **License Plate Detection:** The application processes the image and detects the license plate.
- **OCR Integration:** Uses Tesseract to extract text from the detected license plate.
- **Error Handling:** Provides informative error messages for invalid uploads or processing issues.

## Dependencies

The project relies on the following Python packages which should be included in your `requirements.txt`:

- Flask
- OpenCV-Python
- pytesseract
- numpy

Make sure to have these installed in your environment using the command:

```bash
pip install Flask opencv-python pytesseract numpy
```

## Project Structure

The project contains the following important files:

- `app.py`: The main Flask application that handles requests and serves web pages.
- `alpr_model.py`: Contains the license plate detection logic using OpenCV and Tesseract.
- `static/uploads`: Directory where uploaded images are temporarily stored.
- `templates/index.html`: The HTML template for the user interface (not included in the code provided).

## Acknowledgements

This project utilizes OpenCV for image processing and Tesseract for text recognition. You can find more information about these libraries on their official documentation.

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV Documentation](https://opencv.org/)
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)

## License

This project is licensed under the MIT License. Please feel free to contribute or modify as necessary.
```
