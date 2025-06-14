# Lesson 8 month4 setup automatic control of zigbee module from python

## Todo


1. Create a Long-Lived Access Token
Open Home Assistant in your browser (e.g. http://"http://localhost:8123).

Click your user avatar (bottom of the left sidebar).

Scroll down to Long-Lived Access Tokens, then click Create Token.

Give it a name (e.g. sonoff_script) and click OK.

Copy the token string that appears—you won’t be able to see it again.

Store it safely (e.g. in a password manager); you’ll paste this into your Python script’s TOKEN variable.

2. Find Your Zigbbe’s Entity ID
Every device in HA is exposed as one or more “entities” (lights, switches, sensors, etc.) with names like switch.sonoff_abc123.

In Home Assistant’s sidebar, go to Developer Tools (the hammer 🔨 icon).

Select the States tab.

In the Filter entities box, type part of your Sonoff’s name (e.g. “sonoff”).

You’ll see a list like:

Entity ID	State	Attributes
switch.sonoff_lamp_1234	off	friendly_name: “Lamp”
sensor.sonoff_temp_1234	21.7	unit_of_measurement: “°C”

Copy the exact Entity ID you want to control (e.g. switch.sonoff_lamp_1234).

3. Replace your Token and entity ID in Zigbee_control.py (as described in the video)

Run the test code, it must toggle the switch
```bash
python zigbee_control.py
```


4. Install requierments for tflite

```bash
./install.sh
```

5. Run the code
```bash
python tflite_object_detection_live_security_cam_zigbee.py
```

Now you must be able to toggle the light when a person enter to the ROI