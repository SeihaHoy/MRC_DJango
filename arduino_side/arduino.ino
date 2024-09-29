#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "";         // Replace with your Wi-Fi SSID
const char* password = ""; // Replace with your Wi-Fi password

const char* serverUrl = "api";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  // Wait for Wi-Fi connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  
  // Seed the random number generator
  randomSeed(analogRead(0));
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    // Specify the URL
    http.begin(serverUrl);

    // Set content type to application/json
    http.addHeader("Content-Type", "application/json");

    // Randomize water_level between 0 and 6, and rain_fall between 0 and 100
    float water_level = random(0, 61) / 10.0;  // Generates a value between 0.0 to 6.0
    int rain_fall = random(0, 101);            // Generates a value between 0 to 100
    int sensor_id = 3;                         // Example sensor ID

    // Create JSON data
    String jsonData = "{\"water_level\": " + String(water_level, 1) +
                      ", \"rain_fall\": " + String(rain_fall) +
                      ", \"sensor_id\": " + String(sensor_id) + "}";

    // Send HTTP POST request
    int httpResponseCode = http.POST(jsonData);

    if (httpResponseCode > 0) {
      String response = http.getString();  // Get the response payload
      Serial.println(httpResponseCode);    // Print the HTTP response code
      Serial.println(response);            // Print the response
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    // End the HTTP connection
    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(10000);  // Send data every 10 seconds
}
