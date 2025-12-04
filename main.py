import base64
from io import BytesIO
from PIL import Image
import pyautogui

def capture_screenshot():
    """Capture a screenshot of the desktop"""
    try:
        screenshot = pyautogui.screenshot()
        return screenshot
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None

def image_to_base64(image):
    """Convert PIL Image to base64 string"""
    try:
        buffered = BytesIO()
        image.save(buffered, format="JPEG", quality=85)
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

def main():
    print("Capturing screenshot...")

    screenshot = capture_screenshot()
    if screenshot is None:
        print("Failed to capture screenshot. Exiting.")
        return
    
    print("Converting screenshot to Base64...")
    base64_str = image_to_base64(screenshot)
    
    if base64_str is None:
        print("Error converting image.")
        return
    
    print("\n=== BASE64 SCREENSHOT OUTPUT ===\n")
    print(base64_str)
    print("\n=== END OF BASE64 OUTPUT ===\n")
    print(f"Base64 length: {len(base64_str)} characters")

if __name__ == "__main__":
    try:
        import pyautogui
        from PIL import Image
    except ImportError:
        print("Required packages not found.")
        print("Install with:")
        print("pip install pillow pyautogui")
        exit(1)

    main()
