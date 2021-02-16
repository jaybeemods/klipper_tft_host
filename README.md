# klipper_tft_host
Python host to translate serial TFT to Moonraker

## How this will work:
Instead of connecting the TFT to the micro controller, the screen will be connected to either the serial port on the Raspberry Pi's GPIO pins or through a usb to serial TTL adapter. The GPIO pins will need a logic converter or at least a voltage divider to deal with the 3.3v vs 5v on the TFT. Ideally at phase 1 completion we’ll have close to factory functionality, with the screen acting as it’s own host independent of any web interface, phases 2 and 3 should allow for a more seamless integration with Moonraker. 

**This project should not be considered any kind of replacement for a proper web interface to Klipper, I happen to have a few of these Big Tree Tech screens and want to get them working**

### This project will work in 3 phases
1. Create a python serial to moonraker bridge to allow TFT screens to send gcode to Moonraker
2. Have the bridge intercept appropriate gcode commands from the TFT and replace them with Moonraker specific calls
3. Customize the firmware on the TFT to send more klipper appropriate commands (such as referencing gcode macros from the printer.cfg rather than hard coded marlin gcode)  <- will likely be in another repo

## Current status:
- Developing phase 1
- able to communicate with the TFT over a usb to TTL serial adapter
- framework of the host script at 50%
- will upload actual code once I have basic's working - for now just createing a git repo to work with.


## To Do:
- Implement the webhook to moonraker
- write gcode wrapping / unrapping functions

## Notes:
- Currently testing with a BTT TFT70
