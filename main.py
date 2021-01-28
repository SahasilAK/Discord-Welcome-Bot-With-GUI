from tkinter import *
from tkinter import messagebox
import json
from my_bot import MyBot


TITLE_FONT_COLOR ="#f5f5f5"
BUTTON_COLOR_BG ="#b6eb7a"
BUTTON_COLOR_FG ="#000000"

FONT = ("Courier", 12, "normal")

bot_setup = MyBot()
def update_data():
	change_welcome = welcome_input.get(1.0,"end-1c")
	change_activity = activity_input.get()

	new_data = {
	            'welcome':change_welcome,
	            'activity':change_activity
	            }
	


	is_ok = messagebox.askokcancel(title='Update', message='Are You Ready to Start The MalmerBot')
	if is_ok:
		with open('data.json','w') as data_file:
			json.dump(new_data, data_file)
		window.destroy()
		bot_setup.run_the_bot()
		

with open('data.json','r') as avail_file:
	data = json.load(avail_file)

welcome_data =data['welcome']
activity_data =data['activity']


window = Tk()
window.config()

back_img = PhotoImage(file="images/back.png")

canvas = Canvas(width = 640, height=640)
canvas.create_image(320,320,image =back_img)
canvas.grid(row=0,column=0)

welcome_label = canvas.create_text(320,250,text='Customize Your Welcome Message',fill=TITLE_FONT_COLOR, font =FONT)

welcome_input = Text(canvas)
welcome_input.config(height = 2, width=50)
welcome_input.focus()
welcome_input.insert(1.0,welcome_data)
canvas.create_window(320,280,window = welcome_input)

activity_label = canvas.create_text(320,320,text='Customize Bot Activity',fill=TITLE_FONT_COLOR, font =FONT)

activity_input = Entry(canvas)
activity_input.config(width=40)
activity_input.insert(0,activity_data)
canvas.create_window(320,340,window =activity_input)

update_button = Button(text = "Update", command = update_data, anchor = W)
update_button.configure(fg=BUTTON_COLOR_FG,bg=BUTTON_COLOR_BG,font=FONT, relief = FLAT)
update_window = canvas.create_window(300, 360, anchor=NW, window=update_button)

canvas.update()


window.mainloop()