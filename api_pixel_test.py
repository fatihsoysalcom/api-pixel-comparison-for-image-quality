import io
import sys
from PIL import Image

def compare_images(img1_path, img2_path):
    """Compares two images pixel by pixel and returns the difference count."""
    try:
        img1 = Image.open(img1_path).convert('RGB')
        img2 = Image.open(img2_path).convert('RGB')
    except FileNotFoundError as e:
        print(f"Error: Image file not found - {e}", file=sys.stderr)
        return -1 # Indicate error
    except Exception as e:
        print(f"Error opening or processing images: {e}", file=sys.stderr)
        return -1 # Indicate error

    if img1.size != img2.size:
        print(f"Error: Image dimensions differ. {img1.size} vs {img2.size}", file=sys.stderr)
        return -1 # Indicate error

    diff_pixels = 0
    width, height = img1.size
    pixels1 = img1.load()
    pixels2 = img2.load()

    for y in range(height):
        for x in range(width):
            # Compare RGB values for each pixel
            if pixels1[x, y] != pixels2[x, y]:
                diff_pixels += 1

    return diff_pixels

if __name__ == "__main__":
    # --- Configuration ---
    # Replace with actual paths to your reference and API-generated images
    REFERENCE_IMAGE = "reference.png"
    API_GENERATED_IMAGE = "api_output.png"
    # Define a tolerance for acceptable pixel differences (e.g., due to compression artifacts)
    # A value of 0 means exact pixel match is required.
    PIXEL_DIFFERENCE_TOLERANCE = 0
    # ---------------------

    print(f"Comparing '{REFERENCE_IMAGE}' with '{API_GENERATED_IMAGE}'...")

    # Simulate creating dummy images for demonstration if they don't exist
    try:
        Image.new('RGB', (60, 30), color = 'red').save(REFERENCE_IMAGE)
        Image.new('RGB', (60, 30), color = 'red').save(API_GENERATED_IMAGE)
        print("Created dummy reference.png and api_output.png for demonstration.")
    except Exception as e:
        print(f"Could not create dummy images: {e}. Please ensure you have reference.png and api_output.png.", file=sys.stderr)
        sys.exit(1)

    differences = compare_images(REFERENCE_IMAGE, API_GENERATED_IMAGE)

    if differences == -1:
        print("Image comparison failed due to errors.")
        sys.exit(1)

    if differences <= PIXEL_DIFFERENCE_TOLERANCE:
        print(f"\nSUCCESS: Images are visually identical or within tolerance. {differences} pixel differences found.")
        # In a real API test, this would be a passing assertion.
        sys.exit(0)
    else:
        print(f"\nFAILURE: Images have significant visual differences. {differences} pixel differences found.")
        # In a real API test, this would be a failing assertion.
        sys.exit(1)
