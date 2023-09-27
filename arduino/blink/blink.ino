int led1 = 13;
int blink_duration1 = 100;
int blink_duration2 = 500;
int led2 = 12; 
int C4 = 400;
int halfnote = 900;
int output = 13;
int D4 = 294;
int E4 = 330;
int F4 = 349;
int G4 = 392;
int dotquarter = 900;
int quarter = 667;
int sixteenth = 333;
int dothalf = 2000;
void setup() {
}

void loop() {
  // put your main code here, to run repeatedly:
  pinMode (13, led1); 
  digitalWrite (13, HIGH); 
  delay (blink_duration1);
  pinMode (13, led1);
  digitalWrite (13, LOW);
  delay (blink_duration1); 

    pinMode (12, led2); 
  digitalWrite (12, HIGH); 
  delay (blink_duration2);
  pinMode (12, led2);
  digitalWrite (12, LOW);
  delay (blink_duration2);
  for (int i = 0; i < 3; i++){
    // Measure 1, 2 seconds
    // C4
    tone(output, C4);    // tone(outputPin,frequency)
      delay(dotquarter);  //  delay(milliseconds) 
    noTone(output);
      delay(100);
    // C4
    tone(output, C4);   
      delay(dotquarter);   
    noTone(output);  
      delay(100);  
    // Measure 2, 2 seconds
    // C4
    tone(output, C4);    
      delay(quarter);  
    // D4
    tone(output, D4);    
      delay(sixteenth);  
    // E4
    tone(output, E4);    
      delay(dotquarter);   
    noTone(output);
      delay(100);
    // Measure 3, 2 seconds
    // E4
    tone(output, E4);    
      delay(quarter); 
    // D4 
    tone(output, D4);  
      delay(sixteenth); 
    // E4
    tone(output, E4);    
      delay(quarter); 
    // F4
    tone(output, F4);    
      delay(sixteenth); 
    // Measure 4, 2 seconds
    // G4
    tone(output, G4);    
      delay(dothalf); 
  
    // END
    noTone(output); // stop playing:
}}
