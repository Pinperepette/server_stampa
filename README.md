# Share and Print Documents with Flask and Bootstrap

This web application, built with Flask and Bootstrap, allows users to upload documents and print them using a local printer. The application provides a simple and intuitive user interface for seamless document sharing and printing.

## Features

- **Document Upload**: Users can upload documents in various formats, including .txt, .pdf, .doc, and .docx.
- **Printer Selection**: Users can choose a local printer from the list of available printers on the system.
- **Document Printing**: Uploaded documents are sent to the selected printer for easy printing.

## Getting Started

### Prerequisites

- Python installed on your system
- Internet connection to load Bootstrap (if not using a local copy)

### Installation

1. **Clone the Repository:**

    ```
    git clone <repository-url>
    ```

2. **Create an Empty 'uploads' Folder:**

    Create an empty folder named 'uploads' in the same directory as your Flask application. This folder will be used to temporarily store uploaded documents before printing.

3. **Install Dependencies:**

    ```
    cd <project-folder>
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    ```
    python app.py
    ```

    Access the application through your browser at `http://localhost:5000`.

## Contributing

We welcome contributions! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** Don't forget to create the 'uploads' folder in your project directory before running the application. It's used to temporarily store uploaded documents.
