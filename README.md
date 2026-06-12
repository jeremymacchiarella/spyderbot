# SpyderBot

## Servo Mapping

| Servo | Function |
|--------|----------|
| 0 | Right Front Knee |
| 1 | Right Front Hip |
| 2 | Right Side Knee |
| 3 | Right Side Hip |
| 4 | Right Back Knee |
| 5 | Right Back Hip |
| 6 | Left Back Knee |
| 7 | Left Back Hip |
| 8 | Left Side Knee |
| 9 | Left Side Hip |
| 10 | Left Front Knee |
| 11 | Left Front Hip |

---

## Python Virtual Environment

Activate the virtual environment before running any scripts:

```bash
source ~/spyderbot-env/bin/activate
```

---

## Joint Angle Conventions

### Right-Side Hips
- Positive angle = forward rotation

### Left-Side Hips
- Positive angle = backward rotation

---

## Project Structure

### `util/`

Utility scripts for manually positioning the robot and preparing it for operation.

Recommended startup sequence:

```bash
python util/init_servo_pos.py
```

Other utility scripts:

| File | Purpose |
|--------|---------|
| `init_servo_pos.py` | Move the robot into its initial ready/standing position. |
| `60_servo_knees.py` | Set all knee servos to 60°. |
| `90_servo_hips.py` | Set all hip servos to 90°. |
| `reset.py` | Reset servos to a known state. |
| `set_servos_none.py` | Disable servo outputs / release servo control. |

Use these scripts when manually calibrating the robot or placing it into a known configuration before testing.

---

### `test/`

Scripts used to verify servo operation and hardware functionality.

| File | Purpose |
|--------|---------|
| `test_servos.py` | Verify that all servos respond correctly. |
| `test_knees.py` | Test knee servo movement and direction. |
| `test.py` | General testing and debugging script. |

Run the test scripts whenever:
- A servo has been rewired.
- Servo numbering has changed.
- Motion behavior appears incorrect.
- Hardware functionality needs to be verified.

The expected behavior is that each motor moves smoothly and in the correct direction according to the servo mapping and joint angle conventions described above.

---

## ESP32 Controller

The ESP32 controller firmware is located in:

```text
src/controller.cpp
```

To build and flash the controller:

1. Open `controller.cpp` in the Arduino IDE.
2. Install the ESP32 board package if it is not already installed:
   - Open **Boards Manager**
   - Search for **ESP32**
   - Install **ESP32 by Espressif Systems**
3. Select the appropriate ESP32 Dev Board.
4. Connect the ESP32 via USB.
5. Compile and upload the firmware.

> In normal operation, the controller should already be flashed. Reflashing is only necessary when updating the firmware.

---

## Running the Robot

### 1. SSH into the Raspberry Pi

```bash
ssh spyderbot@10.40.102.70
```

Password:

```text
password
```

### 2. Navigate to the Source Directory

```bash
cd src
```

### 3. Activate the Python Environment

```bash
source ~/spyderbot-env/bin/activate
```

### 4. Initialize the Robot

Run the initialization script to place the robot in its ready position:

```bash
python main.py
```

### 5. Power On the Controller

- Ensure the ESP32 controller has already been flashed.
- Flip the power switch to turn the robot on.

### 6. Connect Bluetooth

Open a **second terminal** and SSH into the Raspberry Pi again:

```bash
ssh spyderbot@10.40.102.70
```

Then run:

```bash
sudo rfcomm release all
sudo rfcomm connect hci0 0C:8B:95:95:29:FE 1
```

### 7. Operate the Robot

Once the Bluetooth connection is established, the robot should be ready for operation.

---

## Typical Startup Checklist

1. Power on the robot.
2. SSH into the Raspberry Pi.
3. Activate the virtual environment.
4. Run `main.py`.
5. Open a second SSH session.
6. Connect Bluetooth using `rfcomm`.
7. Verify movement and begin operation.

## Notes
- Knee servos control leg extension and compression.
- Hip servos control forward/backward leg movement.
- Servo numbering is fixed and should match the wiring configuration.