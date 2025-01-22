import cups
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import time

# GPIO setup
BUTTON_PIN = 23  # GPIO pin number where the button is connected

# Label dimensions in millimeters
label_width_mm = 51
label_height_mm = 12.5

# DPI of the DYMO LabelWriter (assume 300 DPI for this model)
dpi = 300
label_width_px = int((label_width_mm / 25.4) * dpi)
label_height_px = int((label_height_mm / 25.4) * dpi)

# Generate the label with date and time
def create_label(output_file):
    image = Image.new("RGB", (label_width_px, label_height_px), "white")
    draw = ImageDraw.Draw(image)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except IOError:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(current_time, font=font)
    x = (label_width_px - text_width) // 2
    y = (label_height_px - text_height) // 2
    draw.text((x, y), current_time, fill="black", font=font)

    image.save(output_file, "PNG")
    print(f"Label saved as {output_file}")

# Print the label using CUPS
def print_label(printer_name, label_file):
    conn = cups.Connection()
    printers = conn.getPrinters()

    if printer_name not in printers:
        print(f"Printer '{printer_name}' not found.")
        return

    conn.printFile(printer_name, label_file, "Label Print", {})
    print(f"Label sent to printer '{printer_name}'.")

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    printer_name = "DYMO_LabelWriter_450_DUO_Label"
    label_file = "/tmp/label.png"

    print("Waiting for button press... (Press Ctrl+C to exit)")

    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                print("Button pressed! Creating and printing label...")
                create_label(label_file)
                print_label(printer_name, label_file)
                time.sleep(0.5)  # Debounce delay
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        GPIO.cleanup()
