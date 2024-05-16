import voice_automation
import hand_tracking

if __name__ == "__main__":
    while True:
        print("Checking for gesture...")
        hand_tracking.process_gesture()

        print("Checking for voice command...")
        command = voice_automation.recognize_speech().lower()
        if "hey" in command and "ayana" in command:
            voice_automation.respond("How can I assist you?")
            while True:
                next_command = voice_automation.recognize_speech().lower()
                if next_command and not voice_automation.process_command(next_command):
                    break
        elif "exit" in command:
            break
        else:
            print("Command not recognized")
