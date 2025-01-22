# dymo_datastamp

This project uses a Dymo LabelWriter printer and a Raspberry Pi with a simple Python script to create a timestamp picture and send it to the printer. The printer uses the CUPS Dymo driver to print the label, which is used to mark the open date for food in the fridge.

## Requirements

- Raspberry Pi
- Dymo LabelWriter 450 DUO Label printer
- CUPS (Common Unix Printing System)
- Python 3
- Python libraries: `cups`, `Pillow`, `RPi.GPIO`

## Installation

1. Install CUPS on your Raspberry Pi:
    ```sh
    sudo apt-get update
    sudo apt-get install cups
    ```

2. Add your user to the `lpadmin` group:
    ```sh
    sudo usermod -aG lpadmin pi
    ```

3. Install the required Python libraries:
    ```sh
    pip install pycups Pillow RPi.GPIO
    ```

4. Connect your Dymo LabelWriter printer to the Raspberry Pi and configure it using the CUPS web interface (`http://localhost:631`).

## Usage

1. Connect a button to GPIO pin 23 on the Raspberry Pi.
2. Run the Python script:
    ```sh
    python3 print_label.py
    ```
3. Press the button to create and print a label with the current date and time.

## Script Details

The script performs the following steps:
1. Sets up the GPIO pin for the button.
2. Waits for the button to be pressed.
3. When the button is pressed, it creates a label with the current date and time.
4. Sends the label to the Dymo LabelWriter printer using CUPS.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](http://_vscodecontentref_/1) file for details.

![Image description](<pics/Screenshot 2025-01-22 at 22.44.10.png>)
![Image description](<pics/photo_5805460822913303966_y.jpg>)

