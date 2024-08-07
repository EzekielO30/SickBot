import serial
import speech_recognition as sr

# Initialize serial connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's COM port

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source)

    try:
        # Using the recognition service
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def send_command(command):
    print(f"Sending command: {command}")
    ser.write((command + '\n').encode())

def main():
    while True:
        command = recognize_speech()
        if 'yes' in command:
            send_command('drive_to_zoey's')
        elif 'go' in command:
            send_command('drive_to_ava's')
        else:
            send_command('command_not_recognized')

if __name__ == '__main__':
    main()
