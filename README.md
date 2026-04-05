# 🖼️ Image to PDF Converter App (Python)

## 📌 Overview

The **Image to PDF Converter App** is a simple yet powerful Python application that allows users to convert one or multiple image files into a single PDF document. This tool is useful for creating documents from scanned images, photos, or screenshots.

The application is designed to be lightweight, easy to use, and efficient for both beginners and developers.

---

## 🚀 Features

* 📂 Convert single or multiple images into a PDF
* 🖼️ Supports common image formats (JPG, PNG, JPEG)
* 📑 Merge multiple images into one PDF file
* ⚡ Fast and efficient processing
* 🧑‍💻 Simple command-line interface (CLI)
* 🖥️ Optional GUI support (if implemented with Tkinter)

---

## 🛠️ Technologies Used

* Python 3.x
* Pillow (PIL) – Image processing
* ReportLab / img2pdf (optional)
* Tkinter (optional GUI)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash id="p6z9x2"
git clone https://github.com/your-username/Image-to-PDF-Converter.git
cd Image-to-PDF-Converter
```

### 2. Install Dependencies

```bash id="n8k4q1"
pip install -r requirements.txt
```

Or install manually:

```bash id="v5d1m7"
pip install pillow img2pdf
```

---

## ▶️ Usage

### 🔹 Convert a Single Image

```bash id="x7c2r9"
python main.py image.jpg
```

### 🔹 Convert Multiple Images

```bash id="z2m8p4"
python main.py image1.jpg image2.png image3.jpeg
```

### 🔹 Output

* The generated PDF will be saved in the `output/` folder.

---

## 🧠 How It Works

1. Load image(s) using Pillow
2. Convert images to RGB format
3. Merge images (if multiple)
4. Save as a single PDF file

---

## 🧪 Example

```bash id="c4f8w0"
python main.py img1.jpg img2.jpg
```

➡️ Output: `output/converted.pdf`

---

## 📈 Future Improvements

* Drag-and-drop GUI
* Image resizing and compression
* PDF page orientation settings
* Add watermark or password protection
* Cloud upload support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature/new-feature`)
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed by **Your Name**

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!
