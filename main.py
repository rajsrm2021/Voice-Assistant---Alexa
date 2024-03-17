import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

# changing to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greeting():
    talk("Hi! I am jiya, your voice assistant. How can I help you today?")


def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print("Listening....")
            # Adjust the timeout to your preference
            voice = listener.listen(source, timeout=5)  # Waits for 5 seconds for user to speak
            command = listener.recognize_google(voice).lower()
            if 'jiya' in command:
                command = command.replace('jiya', '').strip()
                print(command)
    except sr.WaitTimeoutError:
        print("No input detected. Please try speaking again.")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run_jiya():
    command = take_command()

    if command:
        print(command)
        if 'play' in command:
            song = command.replace('play', '', 1).strip()
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print("Current time is " + time)
            talk("Current time is " + time)
        elif "how are you" in command:
            talk('I am fine how about you.')

        elif 'tell me about you' in command:
            talk(
                'I am jiya a voice assistant made by Raj kumar jaiswal. I can help you find answers get things done, and have fun')

        elif 'about' in command:
            # person = command.replace('about','')
            info = wikipedia.summary(command, 1)
            print(info)
            talk(info)
        elif 'who' in command:
            # person = command.replace('about','')
            info = wikipedia.summary(command, 1)
            print(info)
            talk(info)

        elif 'romantic date' in command:
            talk('I will go anywhere you take me')

        elif 'are you single' in command:
            talk('I am happy to say I feel whole all on my own')

        elif 'joke' in command:
            # print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        elif "stop" in command:
            talk("GoodBye")
            return False # Signal to stop the loop

        # elif 'send message' in command:
        #     talk('Whom do you want to send the message to?')
        #     recipient = take_command()
        #     talk('What is the message?')
        #     message = take_command()
        #     pywhatkit.sendwhatmsg_instantly(recipient, message)  # i have to resolve it
        #     talk('Message sent.')


    else:
        talk('Please say the command again.')
    return True  # Continue running


greeting()
keep_running = True

# Define attempts outside the loop
attempts = 0
max_attempts = 3  # Set the maximum number of attempts for no input

while attempts < max_attempts and keep_running:
    command_result = run_jiya()  # Adjusted to handle None differently
    if command_result is False:  # Explicit stop command detected
        break
    elif command_result is None:  # No input detected
        attempts += 1
        if attempts >= max_attempts:
            talk("No input detected multiple times. Goodbye.")
            break
    else:
        attempts = 0  # Reset attempts if a valid command was received

