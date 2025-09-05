# ASCII Artify 🎨

Convert images and webcam feeds into beautiful ASCII art! This tool supports both traditional grayscale ASCII art and colorful RGB ASCII art using various character ramps.

## Features ✨

- 📁 **File-based conversion**: Convert any image file to ASCII art
- 📷 **Webcam support**: Live webcam feed or single snapshots
- 🌈 **Color support**: RGB colored ASCII art using the Rich library
- ⚙️ **Customizable**: Adjustable width and character ramps
- 🎯 **Multiple modes**: Grayscale or full-color output

## Requirements 📋

### System Requirements
- Python 3.7+
- Webcam (optional, for webcam features)
- Terminal with color support (for RGB mode)

### Python Dependencies
- `Pillow` (PIL) - Image processing
- `rich` - Colored terminal output
- `opencv-python` (cv2) - Webcam capture
- `numpy` - Array operations

## Installation 🚀

### 1. Clone or Download
```bash
git clone <your-repo-url>
cd ASCII-Artify
```

### 2. Install Dependencies

#### Option A: Using pip
```bash
pip install Pillow rich opencv-python numpy
```

#### Option B: Using requirements.txt (if available)
```bash
pip install -r requirements.txt
```

#### Option C: Using virtual environment (recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install Pillow rich opencv-python numpy
```

### 3. Verify Installation
Test with a simple command:
```bash
python main.py --help
```

## Usage 📖

### Basic Usage

#### Convert Image File to ASCII
```bash
python main.py path/to/your/image.jpg
```

#### Adjust Width
```bash
python main.py path/to/your/image.jpg --width 50
```

#### Use Custom Character Ramp
```bash
python main.py path/to/your/image.jpg --chars " .:-=+*#%@"
```

#### Enable RGB Colors
```bash
python main.py path/to/your/image.jpg --color
```

### Webcam Features

#### Take Single Webcam Snapshot
```bash
python main.py --webcam --snapshot
```

#### Live Webcam Feed
```bash
python main.py --webcam --live --width 30
```

#### Colored Webcam ASCII
```bash
python main.py --webcam --snapshot --color --width 40
```

### Advanced Examples

#### High-detail Grayscale
```bash
python main.py image.jpg --width 120 --chars " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
```

#### Colored Live Feed
```bash
python main.py --webcam --live --color --width 50
```

#### Quick Preview
```bash
python main.py image.jpg --width 20 --color
```

## Command Line Arguments 🛠️

| Argument | Type | Description | Default |
|----------|------|-------------|---------|
| `image_path` | string | Path to image file (optional with webcam) | None |
| `--width` | integer | Width of ASCII art (controls line length) | 100 |
| `--chars` | string | Character ramp for grayscale mode | ".:-=+*#%@" |
| `--color` | flag | Enable RGB colored output | False |
| `--webcam` | flag | Use webcam instead of file | False |
| `--snapshot` | flag | Take single webcam photo (with --webcam) | False |
| `--live` | flag | Continuous webcam feed (with --webcam) | False |

## Examples Gallery 🖼️

### File Conversion
```bash
# Basic conversion
python main.py ./assets/logo.jpg

# Small width for quick preview
python main.py ./assets/logo.jpg --width 30

# Large detailed output
python main.py ./assets/logo.jpg --width 100 --color
```

### Webcam Usage
```bash
# Take a quick selfie in ASCII
python main.py --webcam --snapshot --width 40

# Live ASCII webcam (great for demos!)
python main.py --webcam --live --color --width 25

# High-quality webcam snapshot
python main.py --webcam --snapshot --color --width 80
```

## Troubleshooting 🔧

### Common Issues

#### "ModuleNotFoundError"
Make sure all dependencies are installed:
```bash
pip install Pillow rich opencv-python numpy
```

#### "Could not open webcam"
- Check if your webcam is connected and working
- Close other applications using the webcam
- Try running as administrator (Windows)

#### "File not found"
- Check the image path is correct
- Use absolute paths if relative paths don't work
- Ensure the image file exists and is readable

#### Colors not showing
- Ensure your terminal supports color output
- Try a different terminal (Windows Terminal, iTerm2, etc.)
- Some older terminals may not support RGB colors

### Performance Tips

#### For Better Performance
- Use smaller `--width` values for faster processing
- For live webcam feed, width 20-40 works well
- Close unnecessary applications when using webcam

#### For Better Quality
- Use larger `--width` values (80-120)
- Experiment with different character ramps
- Use `--color` for more detailed representation

## Character Ramps 🎭

The script uses character ramps to map brightness levels to characters. Here are some options:

### Default Ramp
```
".:-=+*#%@"
```

### Detailed Ramp
```
" .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
```

### Simple Ramp
```
" .:-=#"
```

### Custom Ramp
You can create your own! Order from lightest to darkest characters.

## Tips for Best Results 💡

1. **Start Small**: Begin with `--width 30` to get quick results
2. **Experiment**: Try different character ramps and widths
3. **Use Color**: The `--color` flag often produces more recognizable results
4. **Good Lighting**: For webcam use, ensure good lighting for better contrast
5. **Terminal Size**: Make sure your terminal is large enough for the output
6. **High Contrast Images**: Work best for ASCII conversion

## Contributing 🤝

Feel free to contribute improvements, bug fixes, or new features!

---

**Happy ASCII Art Creating!** 🎨✨

For questions or issues, please check the troubleshooting section or create an issue in the repository.
