import argparse
import cv2
import numpy as np
from PIL import Image
from rich.console import Console
from rich.text import Text

# TODO: Define your character ramp
ASCII_CHARS = ".:-=+*#%@" 

def resize_and_grayscale(image: Image, new_width: int = 100) -> Image:
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)

    # Resize and convert to grayscale
    resized_image = image.resize((new_width, new_height))
    grayscale_image = resized_image.convert("L")

    return grayscale_image


def resize_rgb_image(image: Image, new_width: int = 100) -> Image:
    """Resize image while maintaining aspect ratio and keep RGB colors."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)

    # Resize and ensure RGB format
    resized_image = image.resize((new_width, new_height))
    rgb_image = resized_image.convert("RGB")

    return rgb_image


def create_rgb_ascii_art(image: Image, width: int = 100) -> None:
    """Create and display RGB ASCII art using rich library."""
    console = Console()
    
    # Resize image while maintaining aspect ratio
    rgb_image = resize_rgb_image(image, width)
    
    text = Text()
    
    for y in range(rgb_image.height):
        for x in range(rgb_image.width):
            r, g, b = rgb_image.getpixel((x, y))
            
            # Use full block character for better color display
            char = "█"
            
            # Add colored character
            text.append(char, style=f"rgb({r},{g},{b})")
        
        # Add newline after each row
        text.append("\n")
    
    console.print(text)


def map_pixel_to_char(pixel_value: int, char_ramp: str = '.:-=+*#%@') -> str:
    if not 0 <= pixel_value <= 255:
        raise ValueError("Pixel value must be between 0 and 255.")
    
    # Calculate the index in the character ramp
    ramp_index = int((pixel_value / 255) * (len(char_ramp) - 1))
    
    return char_ramp[ramp_index]


def capture_webcam_frame() -> Image:
    """Capture a single frame from the webcam and return as PIL Image."""
    cap = cv2.VideoCapture(0)  # 0 is usually the default camera
    
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")
    
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        raise RuntimeError("Error: Could not capture frame from webcam.")
    
    # Convert BGR (OpenCV format) to RGB (PIL format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Convert numpy array to PIL Image
    pil_image = Image.fromarray(frame_rgb)
    
    return pil_image


def webcam_ascii_live(width: int = 100, color: bool = False, chars: str = ASCII_CHARS):
    """Continuous webcam ASCII art display. Press 'q' to quit."""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    console = Console()
    
    print("Starting live webcam ASCII art. Press 'q' to quit.")
    print("Make sure the terminal window is focused to capture key presses.")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not capture frame.")
                break
            
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            
            # Clear screen (simple approach)
            console.clear()
            
            if color:
                create_rgb_ascii_art(pil_image, width)
            else:
                # Create grayscale ASCII
                grey_img = resize_and_grayscale(pil_image, width)
                pixels = grey_img.getdata()
                ascii_chars = [map_pixel_to_char(pixel, chars) for pixel in pixels]
                
                ascii_art_list = []
                for i in range(0, len(ascii_chars), grey_img.width):
                    ascii_art_list.append("".join(ascii_chars[i:i+grey_img.width]))
                
                ascii_art = "\n".join(ascii_art_list)
                print(ascii_art)
            
            print("\nPress Ctrl+C to quit")
            
            # Small delay to prevent overwhelming the terminal
            cv2.waitKey(100)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        cap.release()


def main():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image_path", nargs="?", help="Path to the image file (optional if using webcam)")
    parser.add_argument("--width", type=int, default=100, 
                       help="Width of the ASCII art (controls line length, default: 100)")
    parser.add_argument("--chars", type=str, default=ASCII_CHARS,
                       help=f"Character ramp to use (default: '{ASCII_CHARS}')")
    parser.add_argument("--color", action="store_true",
                       help="Display image in RGB colors using rich library")
    parser.add_argument("--webcam", action="store_true",
                       help="Use webcam input instead of image file")
    parser.add_argument("--live", action="store_true",
                       help="Continuous webcam feed (use with --webcam)")
    parser.add_argument("--snapshot", action="store_true",
                       help="Take single webcam snapshot (use with --webcam)")
    
    args = parser.parse_args()
    
    if args.webcam:
        if args.live:
            # Live webcam feed
            webcam_ascii_live(args.width, args.color, args.chars)
        elif args.snapshot:
            # Single snapshot
            try:
                print("Capturing webcam snapshot...")
                image = capture_webcam_frame()
                print("Snapshot captured! Converting to ASCII...")
                
                if args.color:
                    create_rgb_ascii_art(image, args.width)
                else:
                    grey_img = resize_and_grayscale(image, args.width)
                    pixels = grey_img.getdata()
                    ascii_chars = [map_pixel_to_char(pixel, args.chars) for pixel in pixels]
                    
                    ascii_art_list = []
                    for i in range(0, len(ascii_chars), grey_img.width):
                        ascii_art_list.append("".join(ascii_chars[i:i+grey_img.width]))
                    
                    ascii_art = "\n".join(ascii_art_list)
                    print(ascii_art)
                    
            except RuntimeError as e:
                print(f"Webcam error: {e}")
                return
        else:
            print("When using --webcam, please specify either --live or --snapshot")
            return
    else:
        # Original file-based functionality
        if not args.image_path:
            print("Error: image_path is required when not using webcam mode")
            return
            
        try:
            image = Image.open(args.image_path)
            # image.show()
        except FileNotFoundError:
            print(f"Error: File not found at '{args.image_path}'")
            return

        if args.color:
            # Use RGB color mode with rich
            create_rgb_ascii_art(image, args.width)
        else:
            # Use traditional grayscale ASCII art
            # Resize and convert the image using the specified width
            grey_img = resize_and_grayscale(image, args.width)

            # Get the pixel data and map to ASCII characters using the specified character ramp
            pixels = grey_img.getdata()
            ascii_chars = [map_pixel_to_char(pixel, args.chars) for pixel in pixels]
            
            # Build the ASCII string
            ascii_art_list = []
            for i in range(0, len(ascii_chars), grey_img.width):
                ascii_art_list.append("".join(ascii_chars[i:i+grey_img.width]))
            
            ascii_art = "\n".join(ascii_art_list)

            # Print the final art
            print(ascii_art)


if __name__ == "__main__":
    main()
