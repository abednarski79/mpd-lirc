#include "ControlPanel.h"
#include "LiquidCrystal.h"
#include "Timer.h"
#include <CmdMessenger.h>

//// RGB LED - RGB led ////
// RGB LED constants
static const int LED_BLUE_PIN 	= 2;
static const int LED_RED_PIN 	= 3;
static const int LED_GREEN_PIN 	= 4;

// Relay pins
static const int RELAY_PIN = 5;

// Monitor pins
static const int MONITOR_PIN = A0;
static const int MONITOR_SWITCH_VALUE = 550;
// Id of the event controlling the MONITOR
int monitorEvent;

/// LCD screen ///
// LCD screen constants
/*
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 */
/*static const int LCD_RS_PIN 	= 8;
static const int LCD_ENABLE_PIN = 9;
static const int LCD_D4_PIN 	= 4;
static const int LCD_D5_PIN 	= 5;
static const int LCD_D6_PIN 	= 6;
static const int LCD_D7_PIN 	= 7;
static const char LCD_EMPTY_LINE[] = "                ";
int lcdColumn = 0;
int lcdRow = 0;
char* lcdText;*/
// Initialize the library with the numbers of the interface pins
// LiquidCrystal lcd(LCD_RS_PIN, LCD_ENABLE_PIN, LCD_D4_PIN, LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

//// Timer - events scheduling ////
// Timer object
Timer timer;
// Id of the event controlling the LED
int ledEvent; 

//// CmdMessenger - communication with host device ////
// Mustnt conflict / collide with our message payload data.
char field_separator = ','; 
char command_separator = ';';
char commandBuffer[100] = {'\0'};
// Attach a new CmdMessenger object to the default Serial port
CmdMessenger cmdMessenger = CmdMessenger(Serial, field_separator, command_separator); 
// Commands we send from the Arduino to be received on the PC
enum
{
  kCOMM_ERROR    = 000, // Lets Arduino report serial port comm error back to the PC (only works for some comm errors)
  kACK           = 001, // Arduino acknowledges cmd was received
  kARDUINO_READY = 002, // After opening the comm port, send this cmd 02 from PC to check arduino is ready
  kERR           = 003, // Arduino reports badly formatted cmd, or cmd not recognised
  kSHUT_DOWN     = 004, // Arduino requests PC shutdown
  kSEND_CMDS_END, // Mustnt delete this line
};

// function prototypes
void ledRedBlink();
void monitorRun();

char* getStringParameter() {
	if(cmdMessenger.available()) {
		cmdMessenger.copyString(commandBuffer, 100);
		char message[200] = "Parameter value: ";
		strcat(message, commandBuffer);
		cmdMessenger.sendCmd(kACK, message);
	} else {
		commandBuffer[0] = '\0';
		cmdMessenger.sendCmd(kACK, "Parameter is empty");
	}
	return commandBuffer;
}

long getIntParameter() {
	int intParameter = 0;
	char* buffer = getStringParameter();
	if(buffer[0]) {
		intParameter = atoi(buffer);
	}
	return intParameter;
}

long getLongParameter() {
	long delay = 0;
	char* buffer = getStringParameter();
	if(buffer[0]) {
		delay = strtol(buffer, NULL, 10);
	}
	return delay;
}

void ledEventReset() {
	//char message[] = "ledEventReset: resetting led event";
	//cmdMessenger.sendCmd(kACK, message);
	timer.stop(ledEvent);
}

void ledSetup() {
	pinMode(LED_RED_PIN, OUTPUT);
	pinMode(LED_GREEN_PIN, OUTPUT);
}

void relaySetup() {
	pinMode(RELAY_PIN, OUTPUT);
}

void monitorSetup() {
	monitorEvent = timer.every(500, monitorRun);
}

void monitorRun() {
	int sensorValue = analogRead(MONITOR_PIN);
	if(sensorValue < MONITOR_SWITCH_VALUE) {
		timer.stop(monitorEvent);
		cmdMessenger.sendCmd(kSHUT_DOWN, "Requesting shut down procedure");
		ledRedBlink();
	}
}

/*void lcdSetup() {
	// set up the LCD's number of columns and rows:
	// lcd.begin(16, 2);
	// Display the LCD cursor: an underscore (line) at the position to which the next character will be written.
	// lcd.cursor();
	// lcd.print("hello, world!");
}*/

void ledReset() {
	ledEventReset();
	digitalWrite(LED_RED_PIN, LOW);
	digitalWrite(LED_GREEN_PIN, LOW);
	//char message[] = "ledReset";
	//cmdMessenger.sendCmd(kACK, message);
}

/*void lcdReset() {
	lcd.clear();
}*/

void ledOn(int ledPin) {
	ledReset();
	digitalWrite(ledPin, HIGH);   // turn the led ON (HIGH is the voltage level)
	//char ledPinString[10];
	//ltoa(ledPin, ledPinString, 10);
	//char message[100] = "ledOn: turning led ON, pin: ";
	//strcat(message, ledPinString);
	//cmdMessenger.sendCmd(kACK, message);
}

/*void lcdPrintTextAt(int column, int row, char text[]) {
	lcd.setCursor(column, row);
	lcd.print(LCD_EMPTY_LINE);
	lcd.setCursor(column, row);
	lcd.print(text);
}*/

/*void lcdPrintText() {
	lcdPrintTextAt(lcdColumn, lcdRow, lcdText);
}*/

void relayOff() {
	digitalWrite(RELAY_PIN, LOW);
}

void relayOn() {
	digitalWrite(RELAY_PIN, HIGH);
}

void ledChange(int ledPin) {
	char message[100] = "ledChange: switching led state, pin: ";
	char ledPinString[10];
	ltoa(ledPin, ledPinString, 10);
	strcat(message, ledPinString);
	//cmdMessenger.sendCmd(kACK, message);
	boolean ledState = digitalRead(ledPin);
	if(ledState == LOW) {
		//char message[100] = "ledChange: turning led ON, pin: ";
		//strcat(message, ledPinString);
		//cmdMessenger.sendCmd(kACK, message);
		digitalWrite(ledPin, HIGH);   // turn the led ON (HIGH is the voltage level)
	} else {
		//char message[] = "ledChange: turning led OFF, pin: ";
		//strcat(message, ledPinString);
		//cmdMessenger.sendCmd(kACK, message);
		digitalWrite(ledPin, LOW);   // turn the led OFF (LOW is the voltage level)
	}
}

void ledRedOn() {
	ledOn(LED_RED_PIN);
}

void ledGreenOn() {
	ledOn(LED_GREEN_PIN);
}

void ledRedChange() {
	ledChange(LED_RED_PIN);
}

void ledRedBlink() {
	ledReset();
	ledEvent = timer.every(500, ledRedChange);
}

void ledGreenChange() {
	ledChange(LED_GREEN_PIN);
}

void ledGreenBlink() {
	ledReset();
	ledEvent = timer.every(500, ledGreenChange);
}

void ledResetCommand() {
	timer.after(getLongParameter(), ledReset);
	cmdMessenger.sendCmd(kACK, "ledResetCommand");
}

void ledRedOnCommand() {
	timer.after(getLongParameter(), ledRedOn);
	cmdMessenger.sendCmd(kACK, "ledRedOnCommand");
}

void ledGreenOnCommand() {
	timer.after(getLongParameter(), ledGreenOn);
	cmdMessenger.sendCmd(kACK, "ledGreenOnCommand");
}

void ledRedBlinkCommand() {
	timer.after(getLongParameter(), ledRedBlink);
	cmdMessenger.sendCmd(kACK, "ledRedBlinkCommand");
}

void ledGreenBlinkCommand() {
	timer.after(getLongParameter(), ledGreenBlink);
	cmdMessenger.sendCmd(kACK, "ledGreenBlinkCommand");
}

void lcdResetCommand() {
	//timer.after(getLongParameter(), lcdReset);
	//cmdMessenger.sendCmd(kACK, "lcdResetCommand");
}

void lcdPrintCommand() {
	/*long delay = getLongParameter();
	lcdColumn = getIntParameter();
	lcdRow = getIntParameter();
	lcdText = getStringParameter();
	timer.after(delay, lcdPrintText);
	cmdMessenger.sendCmd(kACK, "lcdPrintCommand");*/
}

void relayOffCommand() {
	timer.after(getLongParameter(), relayOff);
	cmdMessenger.sendCmd(kACK, "relayOffCommand");
}

void relayOnCommand() {
	timer.after(getLongParameter(), relayOn);
	cmdMessenger.sendCmd(kACK, "relayOnCommand");
}

void arduinoReadyCommand() {
	// In response to ping. We just send a throw-away Acknowledgement to say "im alive"
	cmdMessenger.sendCmd(kACK, "arduinoReadyCommand: arduino ready");
}

void notRecognizedCommand() {
	// Default response for unknown commands and corrupt messages
	char message[] = "notRecognizedCommand: unknown command";
	cmdMessenger.sendCmd(kERR, message);
}

// ------------------ E N D  C A L L B A C K  M E T H O D S ------------------

// Commands we send from the host and want to recieve on the Arduino.
// We must define a callback function in our Arduino program for each entry in the list below vv.
// They start at the address kSEND_CMDS_END defined ^^ above as 004
messengerCallbackFunction messengerCallbacks[] =
{
  ledResetCommand, 		// 5
  ledRedOnCommand, 		// 6
  ledGreenOnCommand,	// 7
  ledRedBlinkCommand, 	// 8
  ledGreenBlinkCommand,	// 9
  lcdResetCommand, 		// 10
  lcdPrintCommand, 		// 11
  relayOffCommand, 		// 12
  relayOnCommand, 		// 13
  NULL
};

// ------------------ S E T U P ----------------------------------------------

void attachCallbacks(messengerCallbackFunction* callbacks)
{
  int i = 0;
  int offset = kSEND_CMDS_END;
  while(callbacks[i])
  {
    cmdMessenger.attach(offset+i, callbacks[i]);
    i++;
  }
}

// the setup routine runs once when you press reset:
void setup() {
	// Listen on serial connection for messages from the pc
	  // Serial.begin(57600);  // Arduino Duemilanove, FTDI Serial
	  Serial.begin(115200); // Arduino Uno, Mega, with AT8u2 USB
	  // cmdMessenger.discard_LF_CR(); // Useful if your terminal appends CR/LF, and you wish to remove them
	  cmdMessenger.print_LF_CR();   // Make output more readable whilst debugging in Arduino Serial Monitor

	  // Attach default / generic callback methods
	  cmdMessenger.attach(kARDUINO_READY, arduinoReadyCommand);
	  cmdMessenger.attach(notRecognizedCommand);

	  // Attach my application's user-defined callback methods
	  attachCallbacks(messengerCallbacks);

	  ledSetup();
	  // lcdSetup();
	  relaySetup();

	  arduinoReadyCommand();

	  ledRedBlink();
	  monitorSetup();
	  relayOn();
	  // lcdPrintTextAt(0, 0, "Booting ...");
}

// ------------------ M A I N ( ) --------------------------------------------


void loop()
{
  // Process incoming serial data, if any
  cmdMessenger.feedinSerialData();
  timer.update();
}

