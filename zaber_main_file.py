from tkinter import *
from tkinter import ttk

from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units
from PIL import ImageTk, Image

Library.enable_device_db_store()



def home_all():
    with Connection.open_serial_port("COM4") as connection:
        device_list = connection.detect_devices()
        #print("Found {} devices".format(len(device_list)))
        for i in range(3):
            device_list[i].get_axis(1).home(wait_until_idle=True)

def set():
    btn_home.config(state=DISABLED)
    btn_x_axis.config(state=DISABLED)
    btn_y_axis.config(state=DISABLED)
    btn_z_axis.config(state=DISABLED)
    dropdown_x.config(state=DISABLED)
    dropdown_y.config(state=DISABLED)
    dropdown_y.config(state=DISABLED)
    lbl_show_xaxis.config(text=click_x.get())
    lbl_show_yaxis.config(text=click_y.get())
    lbl_show_zaxis.config(text=click_z.get())

def reset():
    btn_home.config(state=ACTIVE)
    btn_x_axis.config(state=ACTIVE)
    btn_y_axis.config(state=ACTIVE)
    btn_z_axis.config(state=ACTIVE)
    dropdown_x.config(state=ACTIVE)
    dropdown_y.config(state=ACTIVE)
    dropdown_y.config(state=ACTIVE)
    


def move_x():
    
    with Connection.open_serial_port("COM4") as connection:
         device_list = connection.detect_devices()
         device_list[click_x.get()].get_axis(1).move_relative(5, Units.LENGTH_MILLIMETRES,wait_until_idle=True)

def move_y():
    
     with Connection.open_serial_port("COM4") as connection:
         device_list = connection.detect_devices()
         device_list[click_y.get()].get_axis(1).move_relative(5, Units.LENGTH_MILLIMETRES,wait_until_idle=True)

def move_z():
   
     with Connection.open_serial_port("COM4") as connection:
         device_list = connection.detect_devices()
         device_list[click_z.get()].get_axis(1).move_relative(5, Units.LENGTH_MILLIMETRES,wait_until_idle=True)


window=Tk()                                     #created the root window

window.rowconfigure(0,weight=1)
window.rowconfigure([0,1,2],weight=2)





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



option=[0,1,2]
click_x=IntVar(tb_machine_config)
click_y=IntVar(tb_machine_config)
click_z=IntVar(tb_machine_config)                  #this string takes the value input in the dropdown


lbl_frame=ttk.LabelFrame(tb_machine_config,text="Please Configure the Device Number for the axis")
lbl_frame.grid(column=0,row=0, padx=8, pady=4)


lbl_x_axis=ttk.Label(lbl_frame,text="X Axis Device Number")
lbl_x_axis.grid(column=0,row=0,padx=8, pady=4)
dropdown_x=ttk.OptionMenu(lbl_frame,click_x,option[0],*option)
dropdown_x.grid(column=1,row=0,padx=8, pady=4)
btn_x_axis=ttk.Button(lbl_frame,text="Run This Machine",command=lambda:move_x())
btn_x_axis.grid(column=2,row=0,padx=8, pady=4)

lbl_y_axis=ttk.Label(lbl_frame,text="Y Axis Device Number")
lbl_y_axis.grid(column=0,row=1,padx=8, pady=4)
dropdown_y=ttk.OptionMenu(lbl_frame,click_y,option[0],*option)
dropdown_y.grid(column=1,row=1,padx=8, pady=4)
btn_y_axis=ttk.Button(lbl_frame,text="Run This Machine",command=lambda:move_y())
btn_y_axis.grid(column=2,row=1,padx=8, pady=4)


lbl_z_axis=ttk.Label(lbl_frame,text="Z Axis Device Number")
lbl_z_axis.grid(column=0,row=2,padx=8, pady=4)
dropdown_z=ttk.OptionMenu(lbl_frame,click_z,option[0],*option)
dropdown_z.grid(column=1,row=2,padx=8, pady=4)
btn_z_axis=ttk.Button(lbl_frame,text="Run This Machine",command=lambda:move_z())
btn_z_axis.grid(column=2,row=2,padx=8, pady=4)

btn_home=ttk.Button(lbl_frame,text="Home",command=home_all,state=ACTIVE)
btn_home.grid(row=3,columnspan=3,padx=8,pady=4)

btn_set=ttk.Button(lbl_frame,text="Set",command=set,state=ACTIVE)
btn_set.grid(row=4,column=0,sticky="e")

btn_reset=ttk.Button(lbl_frame,text="Reset",command=reset,state=ACTIVE)
btn_reset.grid(row=4,column=2,sticky="w")

#Tab2 Starts from here
lbl_frame_tb2=ttk.LabelFrame(tb_print_config,text="Configure Centre and other info for Print")
lbl_frame_tb2.grid(column=0,row=0, padx=8, pady=4)

var_rbtn=IntVar()
var_cmbbtn=StringVar()

var_cmbbtn.set(1)

lbl_motion=ttk.Label(lbl_frame_tb2,text="Motion (Absolute or Relative):")
lbl_motion.grid(column=0,rowspan=2,padx=8,pady=4)

lbl_show_xaxis=ttk.Label(lbl_frame_tb2,text=click_x.get())
lbl_show_xaxis.grid(column=2,row=0,padx=8,pady=4,sticky="nswe")
lbl_show_xaxis=ttk.Label(lbl_frame_tb2,text="X-Axis")
lbl_show_xaxis.grid(column=2,row=1,padx=8,pady=4,sticky="nswe")


lbl_show_yaxis=ttk.Label(lbl_frame_tb2,text=click_y.get())
lbl_show_yaxis.grid(column=3,row=0,padx=8,pady=4,sticky="nswe")
lbl_show_xaxis=ttk.Label(lbl_frame_tb2,text="Y-Axis")
lbl_show_xaxis.grid(column=3,row=1,padx=8,pady=4,sticky="nswe")

lbl_show_zaxis=ttk.Label(lbl_frame_tb2,text=click_z.get())
lbl_show_zaxis.grid(column=4,row=0,padx=8,pady=4,sticky="nswe")
lbl_show_xaxis=ttk.Label(lbl_frame_tb2,text="Z-Axis")
lbl_show_xaxis.grid(column=4,row=1,padx=8,pady=4,sticky="nswe")

rbtn_abs=ttk.Radiobutton(lbl_frame_tb2,text="Move Absolute",variable=var_rbtn,value=0)
rbtn_rel=ttk.Radiobutton(lbl_frame_tb2,text="Move Relative",variable=var_rbtn,value=1)

rbtn_abs.grid(column=1,row=0,padx=8,pady=4,sticky="w")
rbtn_rel.grid(column=1,row=1,padx=8,pady=4,sticky="w")


travel=[5,1,0.1]

cmbbtn_x=ttk.Combobox(lbl_frame_tb2,textvariable=var_cmbbtn,values=travel)
cmbbtn_x.grid(column=1,row=2,padx=8,pady=4)
lbl_show_xaxis=ttk.Label(lbl_frame_tb2,text="Travel")
lbl_show_xaxis.grid(column=0,row=2,padx=8,pady=4,sticky="nswe")

up_image=Image.open(r"C:\Users\bb237\zaber\GUI-Zaber\up.png")

up_image = up_image.resize((50,50), Image.ANTIALIAS)
up_icn=ImageTk.PhotoImage(up_image)
btn_up=Button(lbl_frame_tb2,image=up_icn,borderwidth=0)
btn_up.grid(column=1,row=6,sticky="nsew")

down_image=Image.open(r"C:\Users\bb237\zaber\GUI-Zaber\up.png")

down_image = down_image.resize((50,50), Image.ANTIALIAS)
down_image=down_image.rotate(180)
down_icn=ImageTk.PhotoImage(down_image)
btn_down=Button(lbl_frame_tb2,image=down_icn,borderwidth=0)
btn_down.grid(column=1,row=8,sticky="nsew")


left_image=Image.open(r"C:\Users\bb237\zaber\GUI-Zaber\up.png")

left_image = left_image.resize((50,50), Image.ANTIALIAS)
left_image=left_image.rotate(90)
left_icn=ImageTk.PhotoImage(left_image)
btn_down=Button(lbl_frame_tb2,image=left_icn,borderwidth=0)
btn_down.grid(column=1,row=7,sticky="w")


right_image=Image.open(r"C:\Users\bb237\zaber\GUI-Zaber\up.png")

right_image = right_image.resize((50,50), Image.ANTIALIAS)
right_image=right_image.rotate(270)
right_icn=ImageTk.PhotoImage(right_image)
btn_right=Button(lbl_frame_tb2,image=right_icn,borderwidth=0)
btn_right.grid(column=1,row=7,sticky="e")

window.mainloop()