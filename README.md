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

## Bluetooth Setup

### Raspberry Pi

Release any existing RFCOMM connections:

```bash
sudo rfcomm release all
```

Connect to the ESP32:

```bash
sudo rfcomm connect hci0 0C:8B:95:95:29:FE 1
```

### ESP32 Dev Board

Flash the ESP32 firmware before attempting to connect from the Raspberry Pi.

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

## Notes

- Knee servos control leg extension and compression.
- Hip servos control forward/backward leg movement.
- Servo numbering is fixed and should match the wiring configuration.