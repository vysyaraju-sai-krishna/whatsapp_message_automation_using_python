import pywhatkit

try:
    pywhatkit.sendwhatmsg("+919010534121", 
                          "Hello Sai Krishna, Happy Birthday! 🎉🎂", 
                          22, 36)  # 10:30 PM
    print("Message Scheduled Successfully!")

except Exception as e:
    print("Error occurred:", e)
