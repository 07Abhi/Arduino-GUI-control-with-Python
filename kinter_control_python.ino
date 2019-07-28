int led1=2, led2=3, ked3=4;
char comm;
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
}

void loop() {
  if(Serial.available()>0)
  {
    comm = Serial.read();
    if(comm=='1')
    {
      digitalWrite(2, HIGH);
      
      }
      if(comm=='a')
      {
        digitalWrite(2, LOW);
        }
      if(comm=='2')
      {
        digitalWrite(3, HIGH);
        }
       if(comm=='b')
       {
        digitalWrite(3, LOW);
        }
       if(comm=='3')
       {
        digitalWrite(4, HIGH);
        }
        if(comm=='c')
        {
          digitalWrite(4, LOW);

          }
         if(comm=='4')
         {
          digitalWrite(2,LOW);
          digitalWrite(3,LOW);
          digitalWrite(4,LOW);
          }
         if(comm=='5')
         {
          digitalWrite(2,HIGH);
          digitalWrite(3,HIGH);
          digitalWrite(4,HIGH);
          }
     
    }
  }
