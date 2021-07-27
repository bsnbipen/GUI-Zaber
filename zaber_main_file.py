from tkinter import *
from tkinter import ttk

from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units


Library.enable_device_db_store()

# def run(txt):
#     #device_list[int(device_number)].axis.move_absolute(5, Units.LENGTH_MILLIMETRES)
#     print(txt+" You Clicked")

def home_all():
    for i in range(2):
        device_list[i].home(wait_until_idle=True)




window=Tk()                                     #created the root window

window.rowconfigure(0,weight=1)
window.rowconfigure([0,1,2],weight=2)

option=["1","2","3"]
click_x=IntVar()
click_y=IntVar()
click_z=IntVar()                  #this string takes the value input in the dropdown
click_x.set(1)
click_y.set(2)
click_z.set(3)

home=PhotoImage(file="home.png")

window.geometry("900x640")
window.title("Control System for Zaber")
notebook= ttk.Notebook(window)

tb_machine_config=Frame(notebook)
tb_print_config=Frame(notebook)
tb_Gcode_config=Frame(notebook)

notebook.add(tb_machine_config,text="Configure Actuator")
notebook.add(tb_print_config,text="Configure Print")
notebook.add(tb_Gcode_config,text="Configure Gcode")

notebook.pack(expand=1, fill="both")





lbl_frame=ttk.LabelFrame(tb_machine_config,text="Please Configure the Device Number for the axis")
lbl_frame.grid(column=0,row=0, padx=8, pady=4)


lbl_x_axis=ttk.Label(lbl_frame,text="X Axis Device Number")
lbl_x_axis.grid(column=0,row=0,padx=8, pady=4)
dropdown_x=ttk.OptionMenu(lbl_frame,click_x,*option)
dropdown_x.grid(column=1,row=0,padx=8, pady=4)
btn_x_axis=ttk.Button(lbl_frame,text="Run This Machine",command=lambda:print(click_x.get()))
btn_x_axis.grid(column=2,row=0,padx=8, pady=4)

lbl_y_axis=ttk.Label(lbl_frame,text="Y Axis Device Number")
lbl_y_axis.grid(column=0,row=1,padx=8, pady=4)
dropdown_y=ttk.OptionMenu(lbl_frame,click_y,*option)
dropdown_y.grid(column=1,row=1,padx=8, pady=4)
btn_y_axis=ttk.Button(lbl_frame,text="Run This Machine",command=lambda:print(click_y.get()))
btn_y_axis.grid(column=2,row=1,padx=8, pady=4)


lbl_z_axis=ttk.Label(lbl_frame,text="Z Axis Device Number")
lbl_z_axis.grid(column=0,row=2,padx=8, pady=4)
dropdown_z=ttk.OptionMenu(lbl_frame,click_z,*option)
dropdown_z.grid(column=1,row=2,padx=8, pady=4)
btn_z_axis=ttk.Button(lbl_frame,text="Run This Machine",command=lambda:print(click_z.get()))
btn_z_axis.grid(column=2,row=2,padx=8, pady=4)

btn_home=ttk.Button(lbl_frame,text="Home",command=home_all,state=DISABLED)
btn_home.grid(row=3,columnspan=3)

#Tab2 Starts from here
lbl_frame_tb2=ttk.LabelFrame(tb_print_config,text="Configure Centre and other info for Print")
lbl_frame_tb2.grid(column=0,row=0, padx=8, pady=4)




window.mainloop()