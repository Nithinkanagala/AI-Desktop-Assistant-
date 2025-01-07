from tkinter import *
import Actions
import speech_text

# Initialize the main window
wn = Tk()
wn.title('Bujji - Your Assistant')
wn.geometry('500x600')
wn.resizable(False, False)

# Add a gradient-like background using a Canvas
canvas = Canvas(wn, width=500, height=600)
canvas.place(x=0, y=0)

# Creating a gradient effect with shades of blue and white
for i in range(256):
    color = "#%02x%02x%02x" % (255-i, 255-i, 255)
    canvas.create_line(0, i*2, 500, i*2, fill=color)

# Send user input and display bot's response
def send():
    user_input = entry.get()
    if user_input.strip():  # Ensure input is not empty
        bot_response = Actions.actions(user_input)
        update_chat('You', user_input)
        update_chat('Bujji', bot_response)
        entry.delete(0, END)  # Clear entry after sending

# Clear chat window
def delete():
    text.config(state=NORMAL)  # Enable editing to clear text
    text.delete('1.0', END)
    text.config(state=DISABLED)  # Disable editing again

# Get user input via speech and display bot's response
def ask():
    user_input = speech_text.speech_to_text()
    if user_input.strip():  # Ensure input is not empty
        bot_response = Actions.actions(user_input)
        update_chat('You', user_input)
        update_chat('Bujji', bot_response)

# Update chat window with user and bot messages
def update_chat(sender, message):
    text.config(state=NORMAL)  # Enable editing to insert text
    text.insert(END, f'{sender}: {message}\n')
    text.see(END)  # Auto-scroll to the latest message
    text.config(state=DISABLED)  # Disable editing again

# Title label centered
text_label = Label(wn, text='Bujji - Desktop Assistant', font=('Helvetica', 18, 'bold'), bg='#f0f0f0', fg='black')
text_label.place(relx=0.5, rely=0.1, anchor=CENTER)  # Centered using relx and anchor

# Chat window (read-only)
text = Text(wn, font=('Arial', 12), bg='white', fg='black', padx=10, pady=10, wrap=WORD, bd=1, relief='solid')
text.place(x=30, y=150, width=440, height=300)
text.config(state=DISABLED)  # Make it read-only

# Input entry with placeholder effect
entry = Entry(wn, font=('Arial', 14), justify=CENTER, bd=1, relief='solid')
entry.place(x=30, y=470, width=440, height=40)

# Set placeholder text
placeholder_text = 'Give a Text'
entry.insert(0, placeholder_text)

# Bind events to handle placeholder behavior
def on_entry_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, END)  # Clear placeholder text

def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, placeholder_text)  # Restore placeholder text

entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focus_out)

# Buttons with updated styles
button_style = {'bg': '#FFA500', 'fg': 'black', 'font': ('Helvetica', 12, 'bold'), 'relief': SOLID, 'bd': 2}

# Function to change button color on hover
def on_enter(button):
    button['bg'] = 'yellow'

def on_leave(button):
    button['bg'] = '#FFA500'  # Orange color

# Create buttons with hover effects
button_style = {'bg': '#FFA500', 'fg': 'black', 'font': ('Helvetica', 12, 'bold'), 'relief': SOLID, 'bd': 2}

ask_button = Button(wn, text='Ask', **button_style, command=ask)
ask_button.place(x=80, y=530, width=100, height=40)
ask_button.bind("<Enter>", lambda e: on_enter(ask_button))
ask_button.bind("<Leave>", lambda e: on_leave(ask_button))

delete_button = Button(wn, text='Clear', **button_style, command=delete)
delete_button.place(x=200, y=530, width=100, height=40)
delete_button.bind("<Enter>", lambda e: on_enter(delete_button))
delete_button.bind("<Leave>", lambda e: on_leave(delete_button))

send_button = Button(wn, text='Send', **button_style, command=send)
send_button.place(x=320, y=530, width=100, height=40)
send_button.bind("<Enter>", lambda e: on_enter(send_button))
send_button.bind("<Leave>", lambda e: on_leave(send_button))

# Start the main loop
wn.mainloop()
