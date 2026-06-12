#include "BluetoothSerial.h"

BluetoothSerial SerialBT;
QueueHandle_t commandQueue;

const int LED_PIN   = 13;
const int BTN_FWD   = 12;
const int BTN_BACK  = 5;
const int BTN_LEFT  = 4; 
const int BTN_RIGHT = 27;

bool lastFwd   = false;
bool lastBack  = false;
bool lastLeft  = false;
bool lastRight = false;

void sendIfChanged(int pin, bool &lastState, const char *onMsg, const char *offMsg) {
  bool pressed = digitalRead(pin) == LOW;

  if (pressed != lastState) {
    const char *cmd;
    if (pressed) {
      cmd = onMsg;
    } else {
      cmd = offMsg;
    }
    if (xQueueSend(commandQueue, &cmd, 0) != pdPASS) {
      Serial.println("Queue full");
    }

    lastState = pressed;
  }
}

void buttonTask(void *argument) {
  while (true) {
    sendIfChanged(BTN_FWD,   lastFwd,   "FWD_ON",   "FWD_OFF");
    sendIfChanged(BTN_BACK,  lastBack,  "BACK_ON",  "BACK_OFF");
    sendIfChanged(BTN_LEFT,  lastLeft,  "LEFT_ON",  "LEFT_OFF");
    sendIfChanged(BTN_RIGHT, lastRight, "RIGHT_ON", "RIGHT_OFF");

    bool anyPressed = lastFwd || lastBack || lastLeft || lastRight;
    digitalWrite(LED_PIN, anyPressed ? HIGH : LOW);

    vTaskDelay(pdMS_TO_TICKS(20));
  }
}

void bluetoothTask(void *argument) {
  const char *cmd;

  while (true) {
    if (xQueueReceive(commandQueue, &cmd, portMAX_DELAY)) {
      SerialBT.println(cmd);
      Serial.println(cmd);
    }
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println(LED_PIN);

  pinMode(BTN_FWD, INPUT_PULLUP);
  pinMode(BTN_BACK, INPUT_PULLUP);
  pinMode(BTN_LEFT, INPUT_PULLUP);
  pinMode(BTN_RIGHT, INPUT_PULLUP);

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);


  SerialBT.begin("Controller");
  Serial.println("Bluetooth started");

  commandQueue = xQueueCreate(10, sizeof(const char *));

  xTaskCreatePinnedToCore(buttonTask, "Button Task", 4096, NULL, 2, NULL, 1);
  xTaskCreatePinnedToCore(bluetoothTask, "Bluetooth Task", 4096, NULL, 1, NULL, 0);
}

void loop() {
}