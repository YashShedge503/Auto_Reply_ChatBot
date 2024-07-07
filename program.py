import pyautogui
import pyperclip
import time
from generate_response import OpenAI

client = OpenAI(
  api_key="sk-proj-WxS17ehGk2PnwmzCHcDwT3B1bkFJFMj6bYTk9jG1bqZaFTcj",
)

def is_last_message_from_sender(chat_history, sender_name="Rohan Das"):
    # Split the chat history into individual messages
    messages = chat_history.strip().split('/2024]')[-1]
    if sender_name in messages:
        return True
    return False
    
# Click on the icon at position (1379, 1049)
pyautogui.click(1379, 1049)

# Pause to give you time to switch to the correct window
time.sleep(2)


while True:
    
    # Pause for a moment to let any interface changes occur
    time.sleep(1)

    # Move to start position (612, 235)
    pyautogui.moveTo(620, 226)

    # Drag to end position (1900, 1000) to select the text
    pyautogui.dragTo(1012, 900, duration=1, button='left')

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')


    # Pause for a moment to ensure the clipboard has the data
    time.sleep(1)
    pyautogui.click(634, 328) #to deslect

    # Get the clipboard content
    chat_history = pyperclip.paste()

    # Print the text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and respond like Naruto. Output should be the next chat response as Naruto"},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Click on the desired position
        pyautogui.click(1491, 956)

        # Paste the text
        pyautogui.hotkey('ctrl', 'v')
 
        # Press Enter
        pyautogui.press('enter')

        # Verify by printing the response text to the console
        #print(response_text)


