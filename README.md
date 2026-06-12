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

## Notes

- Knee servos control leg extension and compression.
- Hip servos control forward/backward leg movement.
- Servo numbering is fixed and should match the wiring configuration.