#include "AudioTools.h"
#include "AudioCodecs/CodecMP3Helix.h"
#include "config.h"


URLStream url(WIFI_SSID,WIFI_PASSWORD);
AnalogAudioStream out; 
EncodedAudioStream dec(&out, new MP3DecoderHelix());
StreamCopy copier(dec, url); 


void setup(){
  Serial.begin(115200);
  pinMode(23, INPUT_PULLUP); //Connected to switch for pause/unpause
  AudioLogger::instance().begin(Serial, AudioLogger::Info);  

  auto config = out.defaultConfig(TX_MODE);
  out.begin(config);

  dec.begin();
  
  url.begin(STREAM_URL,"audio/mp3");

}

void loop(){
  //Check if Radio is supposed to be turned on
  if(digitalRead(23) == HIGH)
  {
    int received_bytes = copier.copy();
    Serial.println(received_bytes);
    if(received_bytes == 0)
    {
      //If stream ends, try restarting/reconnecting
      Serial.println("Stream failed... retrying...");
      delay(500);
      url.begin(STREAM_URL, "audio/mp3");
    }

  }
  else
  {
    //If radio is supposed to be turned off, pause stream
    delay(100);
    Serial.println("Stream Paused");
  }
}