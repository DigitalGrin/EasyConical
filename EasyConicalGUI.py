import tkinter as tk                    
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path
import Transformation_STL_var_angle as tf1
import Backtransformation_GCode_var_angle as tf2

inputf1="select an STL"
inputp1="a"
output1="select output path"
inputf2="select a gcode file"
inputp2="b"
output2="select output path"
transformation_types=("outward","inward")

root = tk.Tk()
root.title("Conical Slicing Helper")
root.geometry('500x370')
tabControl = ttk.Notebook(root)
cone_angle=tk.StringVar(value="16")
cone_angle2=tk.StringVar(value="16")
refinement_iterations=tk.StringVar(value="1")
ttypes=tk.StringVar(value="outward")
cone_type=tk.StringVar(value="outward")
first_layer_height=tk.StringVar(value="-0.2")
x_shift=tk.StringVar(value="110")
y_shift=tk.StringVar(value="90")

def selectpath(method):
    global inputf1, inputp1, inputf2, inputp2, output1, output2, file1, file2, path1, path2
    if (method=="1" or method=="2"):
        if (method=="1"):
            nameandpath = Path(fd.askopenfilename(filetypes=(("STL file", "*.stl"),("STL file","*.STL"))))
        elif (method=="2"):
            nameandpath = Path(fd.askopenfilename(filetypes=(("Gcode file", "*.gcode"),("Gcode file","*.gx"),("Gcode file","*.g"))))
        else:
            print("something unforseen has hapened")
        namewe = str(nameandpath.name)
        namene = namewe.removesuffix(str(nameandpath.suffix))
        path = str(nameandpath.parent).replace("\\","/")+"/"
        if (method=="1"):
            inputf1=namene
            inputp1=path
            file1.configure(text=inputf1)
        elif (method=="2"):
            inputf2=namewe
            inputp2=path
            file2.configure(text=inputf2)
        else:
            print("Something messed up method 1/2")
    elif (method=="3" or method=="4"):
        path = str(fd.askdirectory())
        if (method=="3"):
            output1=path+"/"
            path1.configure(text=output1)
        elif (method=="4"):
            output2=path+"/"
            path2.configure(text=output2)
        else:
            print("Something messed up method 3/4")
    else:
        print("Something messed up overall")

def ftransform():
    global inputf1, inputp1, output1, cone_angle, refinement_iterations, ttypes
    cag = cone_angle.get()
    refit = refinement_iterations.get()
    tty = ttypes.get()
    err1.configure(text="Working, please be patient")
    err1.grid(column = 1, row = 5,padx = 0,pady = 10,sticky='W')
    try:
        tf1.transform1(inputf1,inputp1,output1,float(cag),int(float(refit)),tty)
    except:
        err1.configure(text="Invalid inputs")
        err1.grid(column = 1, row = 5,padx = 0,pady = 10,sticky='W')
    else:
        err1.configure(text="Operation finished")
        err1.grid(column = 1, row = 5,padx = 0,pady = 10,sticky='W')


def btransform():
    global inputf2, inputp2, output2, cone_angle2, cone_type, first_layer_height, x_shift, y_shift
    cag = cone_angle2.get()
    ctp =  cone_type.get()
    flh = first_layer_height.get()
    xsh = x_shift.get()
    ysh = y_shift.get()
    err2.configure(text="Working, please wait")
    err2.grid(column = 1, row = 7,padx = 0,pady = 10,sticky='W')
    try:
        tf2.transform2(inputf2,inputp2,output2,float(cag),ctp,float(flh),float(xsh),float(ysh))
    except:
        err2.configure(text="Invalid inputs")
        err2.grid(column = 1, row = 7,padx = 0,pady = 10,sticky='W')
    else:
        err2.configure(text="Operation finished")
        err2.grid(column = 1, row = 7,padx = 0,pady = 10,sticky='W')

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Forward Transform')
tabControl.add(tab2, text ='Back Transform')
tabControl.add(tab3, text ='Instructions')
tabControl.pack(expand = 1, fill ="both")

#Tab 1 functions
file1 = ttk.Label(tab1,text =inputf1)
path1 = ttk.Label(tab1,text =output1)
file1.grid(column = 0, row = 0,padx = 20,pady = 10,sticky='W')
path1.grid(column = 0, row = 1,padx = 20,pady = 10,sticky='W')
err1 = ttk.Label(tab1,text ="Invalid inputs")
ttk.Label(tab1,text ='Cone Angle').grid(column = 1, row = 2,padx = 0,pady = 0,sticky='W')
ttk.Label(tab1,text ='Refinement Iterations').grid(column = 1, row = 3,padx = 0,pady = 10,sticky='W')
ttk.Label(tab1,text ="Transformation Type").grid(column = 1, row = 4,padx = 0,pady = 10,sticky='W')
ttk.Button(tab1, text = 'Select New File', command = lambda:selectpath('1') ).grid(column = 1, row = 0,padx = 0,pady = 10,sticky='W')
ttk.Button(tab1, text = 'Select New Output', command = lambda:selectpath('3') ).grid(column = 1, row = 1,padx = 0,pady = 10,sticky='W')
ttk.Button(tab1, text = 'Transform!', command = ftransform ).grid(column = 0, row = 5,padx = 0,pady = 10)
ttk.Entry(tab1, textvariable = cone_angle).grid(column = 0, row = 2,padx = 20,pady = 10)
ttk.Entry(tab1, textvariable = refinement_iterations).grid(column = 0, row = 3,padx = 20,pady = 10)
ttypeselect = ttk.Combobox(tab1, width = 17, textvariable = ttypes)
ttypeselect["values"] = transformation_types
ttypeselect.grid(column = 0, row = 4,padx = 20,pady = 10)

#Tab 2 functions
file2 = ttk.Label(tab2,text =inputf2)
path2 = ttk.Label(tab2,text =output2)
file2.grid(column = 0, row = 0,padx = 20,pady = 10,sticky='W')
path2.grid(column = 0, row = 1,padx = 20,pady = 10,sticky='W')
err2 = ttk.Label(tab2,text ="Invalid inputs")
ttk.Label(tab2,text ='Cone Angle').grid(column = 1, row = 2,padx = 0,pady = 0,sticky='W')
ttk.Label(tab2,text ='First Layer Height').grid(column = 1, row = 4,padx = 0,pady = 10,sticky='W')
ttk.Label(tab2,text ='X Shift').grid(column = 1, row = 5,padx = 0,pady = 10,sticky='W')
ttk.Label(tab2,text ='Y Shift').grid(column = 1, row = 6,padx = 0,pady = 10,sticky='W')
ttk.Label(tab2,text ="Cone Type").grid(column = 1, row = 3,padx = 0,pady = 10,sticky='W')
ttk.Button(tab2, text = 'Select New File', command = lambda:selectpath('2') ).grid(column = 1, row = 0,padx = 0,pady = 10,sticky='W')
ttk.Button(tab2, text = 'Select New Output', command = lambda:selectpath('4') ).grid(column = 1, row = 1,padx = 0,pady = 10,sticky='W')
ttk.Button(tab2, text = 'Transform!', command = btransform ).grid(column = 0, row = 7,padx = 0,pady = 10)
ttk.Entry(tab2, textvariable = cone_angle2).grid(column = 0, row = 2,padx = 20,pady = 10)
ttk.Entry(tab2, textvariable = first_layer_height).grid(column = 0, row = 4,padx = 20,pady = 10)
ttk.Entry(tab2, textvariable = x_shift).grid(column = 0, row = 5,padx = 20,pady = 10)
ttk.Entry(tab2, textvariable = y_shift).grid(column = 0, row = 6,padx = 20,pady = 10)
ttypeselect2 = ttk.Combobox(tab2, width = 17, textvariable = cone_type)
ttypeselect2["values"] = transformation_types
ttypeselect2.grid(column = 0, row = 3,padx = 20,pady = 10)

#Tab 3 functions
ttk.Label(tab3,text ="Info").grid(column = 0,row = 0, padx = 30,pady = 30)

root.mainloop()