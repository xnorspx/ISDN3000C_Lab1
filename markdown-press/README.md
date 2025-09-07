# MarkdownPress - A Simple Static Site Generator

This project converts Markdown files into a static HTML website.

## Setup

### 1. Create and activate a virtual environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (PowerShell)
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this command to allow local scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

## Usage

### 1. Add Markdown files

Place your `.md` files in the `source/` directory. Example files are already provided:
- `source/index.md`
- `source/about.md`

### 2. Generate the site

```powershell
python main.py
```

This will:
- Read all `.md` files from the `source/` folder
- Convert them to HTML using the first heading as the page title
- Save the HTML files to the `public/` folder

### 3. View the result

Open the generated HTML files in your browser:

```powershell
start public\index.html
```

## How it works

- The generator reads Markdown files from `source/` (default)
- Converts them to HTML using Python's `markdown` library
- Uses the first `# Heading` in each file as the HTML page title
- Outputs HTML files to `public/` (default)
- You can customize source and output directories by modifying `generator.py`