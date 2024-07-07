
# Move to start position (612, 235)
pyautogui.moveTo(612, 235)

# Drag to end position (1900, 1000) to select the text
pyautogui.dragTo(1900, 1000, duration=1, button='left')

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Pause for a moment to ensure the clipboard has the data
time.sleep(1)

# Get the clipboard content
text = pyperclip.paste()

# Print the text to verify
print(text)
