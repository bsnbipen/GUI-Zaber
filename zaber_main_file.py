from tkinter import *
from tkinter import ttk

from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units


Library.enable_device_db_store()



def home_all():
    with Connection.open_serial_port("COM4") as connection:
        device_list = connection.detect_devices()
        #print("Found {} devices".format(len(device_list)))
        for i in range(3):
            device_list[i].get_axis(1).home(wait_until_idle=True)

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
btn_home.grid(row=3,columnspan=3)

#Tab2 Starts from here
lbl_frame_tb2=ttk.LabelFrame(tb_print_config,text="Configure Centre and other info for Print")
lbl_frame_tb2.grid(column=0,row=0, padx=8, pady=4)

var_rbtn=IntVar()


lbl_motion=ttk.Label(lbl_frame_tb2,text="Motion (Absolute or Relative):")

lbl_motion.grid(column=0,rowspan=2,padx=8,pady=4)

rbtn_abs=ttk.Radiobutton(lbl_frame_tb2,text="Move Absolute",variable=var_rbtn,value=0)
rbtn_rel=ttk.Radiobutton(lbl_frame_tb2,text="Move Relative",variable=var_rbtn,value=1)

rbtn_abs.grid(column=1,row=0,padx=8,pady=4,sticky="w")
rbtn_rel.grid(column=1,row=1,padx=8,pady=4,sticky="w")


window.mainloop()