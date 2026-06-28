# Python Projects

A collection of small Python utility projects, GUI apps, command-line programs, and one simple C program. These projects are useful for practicing Python basics, Tkinter GUI development, file conversion, simple chatbot logic, and AI image captioning.

## Projects

| File | Type | Description |
|---|---|---|
| `calculator.py` | Python / Tkinter | A scientific calculator GUI with arithmetic operators, trigonometric functions, logarithms, constants, and a styled button layout. |
| `chatbot.py` | Python CLI | A small rule-based mood chatbot called Sunny. It responds to feelings such as lonely, sad, anxious, and happy with supportive prompts. |
| `converter.py` | Python Utility | Office document to PDF converter using multiple Windows-friendly conversion methods such as `docx2pdf` and Word COM automation. |
| `image_caption.py` | Python / AI / Tkinter | Instagram-style image caption generator using BLIP image captioning, image analysis, caption templates, and a GUI file picker. |
| `evaluation.c` | C Program | Simple menu-based C program that asks the user to choose a BTech branch and prints the selected option. |
| `text.txt` | Text File | Plain text file included with the project collection. |

## Requirements

- Python 3.10 or newer
- Tkinter for GUI apps  
  Tkinter usually comes installed with Python on Windows.
- Optional: GCC or another C compiler for `evaluation.c`

Basic scripts use only the Python standard library:

```bash
python chatbot.py
```

GUI scripts:

```bash
python calculator.py
```

## Run The Projects

Open a terminal inside the repository:

```bash
cd python_projects
```

Run the calculator:

```bash
python calculator.py
```

Run the chatbot:

```bash
python chatbot.py
```

Run the document converter:

```bash
python converter.py
```

Run the image caption generator:

```bash
python image_caption.py
```

Compile and run the C program:

```bash
gcc evaluation.c -o evaluation
./evaluation
```

On Windows PowerShell, run the compiled C program with:

```powershell
.\evaluation.exe
```

## Advanced Dependencies

### Document Converter

`converter.py` may install or require:

```bash
python -m pip install docx2pdf comtypes
```

For best results on Windows, Microsoft Word should be installed because some conversion methods use Word automation.

### Image Caption Generator

`image_caption.py` uses heavier AI/image-processing libraries:

```bash
python -m pip install torch transformers opencv-python pillow requests numpy
```

The first run may take time because the BLIP model is downloaded from Hugging Face:

```text
Salesforce/blip-image-captioning-large
```

## Repository Structure

```text
python_projects/
├── calculator.py
├── chatbot.py
├── converter.py
├── evaluation.c
├── image_caption.py
├── text.txt
└── README.md
```

## Notes

- `calculator.py` and `image_caption.py` open desktop GUI windows.
- `chatbot.py` runs in the terminal.
- `converter.py` is designed mainly for Windows document conversion workflows.
- `image_caption.py` requires more system resources than the other scripts because it loads a machine learning model.

This repository is focused on learning Python through practical mini projects and utilities.
