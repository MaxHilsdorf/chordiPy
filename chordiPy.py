import tkinter
import numpy as np

### Algorithm ###

# Chord class

class chord:
    def __init__(self, name, array):
        self.name = name
        self.array = array

# Functions

def create_tab_data(chord):
    name = chord.name
    str1 = chord.array[0]
    str2 = chord.array[1]
    str3 = chord.array[2]
    str4 = chord.array[3]
    str5 = chord.array[4]
    str6 = chord.array[5]
    strings = [str1, str2, str3, str4, str5, str6]

    num_frets = 5

    tab = np.zeros((num_frets, 6), dtype="int")

    for i in range(1, num_frets):
        for j, string in enumerate(strings):
            if i == string:
                tab[i-1][j] = 1        

    return {"Name" : name, "Tab" : tab}


e_min = chord("E Minor", np.array([0,2,2,0,0,0]))
e_maj = chord("E Major", np.array([0,2,2,1,0,0]))
c_maj = chord("C Major", np.array([0,3,2,0,1,0]))
a_min = chord("A Minor", np.array([0,0,2,2,1,0]))
a_maj = chord("A Major", np.array([0,0,2,2,2,0]))
d_min = chord("D Minor", np.array([0,0,0,2,3,1]))
d_maj = chord("D Major", np.array([0,0,0,2,3,2]))
g_maj = chord("G Major", np.array([3,2,0,0,3,3]))
f_maj = chord("F Major", np.array([0,0,3,2,1,1]))

chord = e_min

### GUI ###

# Layout Variables

font_family = "Arial"
font_size_base = 18

# Window

window = tkinter.Tk()
window.title("chordiPy")

# Tk Variables

chord_name_str = tkinter.StringVar()
chord_name_str.set("")

output_str_0_0 = tkinter.StringVar()
output_str_0_1 = tkinter.StringVar()
output_str_0_2 = tkinter.StringVar()
output_str_0_3 = tkinter.StringVar()
output_str_0_4 = tkinter.StringVar()
output_str_0_5 = tkinter.StringVar()

output_str_1_0 = tkinter.StringVar()
output_str_1_1 = tkinter.StringVar()
output_str_1_2 = tkinter.StringVar()
output_str_1_3 = tkinter.StringVar()
output_str_1_4 = tkinter.StringVar()
output_str_1_5 = tkinter.StringVar()

output_str_2_0 = tkinter.StringVar()
output_str_2_1 = tkinter.StringVar()
output_str_2_2 = tkinter.StringVar()
output_str_2_3 = tkinter.StringVar()
output_str_2_4 = tkinter.StringVar()
output_str_2_5 = tkinter.StringVar()

output_str_3_0 = tkinter.StringVar()
output_str_3_1 = tkinter.StringVar()
output_str_3_2 = tkinter.StringVar()
output_str_3_3 = tkinter.StringVar()
output_str_3_4 = tkinter.StringVar()
output_str_3_5 = tkinter.StringVar()

output_str_4_0 = tkinter.StringVar()
output_str_4_1 = tkinter.StringVar()
output_str_4_2 = tkinter.StringVar()
output_str_4_3 = tkinter.StringVar()
output_str_4_4 = tkinter.StringVar()
output_str_4_5 = tkinter.StringVar()

output_str_list = [[output_str_0_0, output_str_0_1, output_str_0_2,
                   output_str_0_3, output_str_0_4, output_str_0_5],

                   [output_str_1_0, output_str_1_1, output_str_1_2,
                   output_str_1_3, output_str_1_4, output_str_1_5],

                   [output_str_2_0, output_str_2_1, output_str_2_2,
                   output_str_2_3, output_str_2_4, output_str_2_5],

                   [output_str_3_0, output_str_3_1, output_str_3_2,
                   output_str_3_3, output_str_3_4, output_str_3_5],

                   [output_str_4_0, output_str_4_1, output_str_4_2,
                   output_str_4_3, output_str_4_4, output_str_4_5]]

for str_list in output_str_list:
    for string in str_list:
        string.set("-")

# Frames

title_fr = tkinter.Frame(window)
title_fr.pack()

input_fr = tkinter.Frame(window)
input_fr.pack()

output_fr = tkinter.Frame(window)
output_fr.pack()

chord_name_fr = tkinter.Frame(output_fr)
chord_name_fr.pack(side="top")

frets_fr = tkinter.Frame(output_fr)
frets_fr.pack(side="left")


# Title

title = tkinter.Label(title_fr, text = "chordiPy")
title.configure(font = (font_family, font_size_base, "bold"))
title.pack()

# Output

chord_name = tkinter.Label(chord_name_fr, textvariable=chord_name_str)
chord_name.configure(font = (font_family, int(font_size_base*0.5), "bold"))
chord_name.pack()

fret_num_1 = tkinter.Label(frets_fr, text = "1")
fret_num_1.grid(row=1, column=0)
fret_num_2 = tkinter.Label(frets_fr, text = "2")
fret_num_2.grid(row=2, column=0)
fret_num_3 = tkinter.Label(frets_fr, text = "3")
fret_num_3.grid(row=3, column=0)
fret_num_4 = tkinter.Label(frets_fr, text = "4")
fret_num_4.grid(row=4, column=0)
fret_num_5 = tkinter.Label(frets_fr, text = "5")
fret_num_5.grid(row=5, column=0)

string_name_1 = tkinter.Label(frets_fr, text = "E")
string_name_1.grid(row=0, column=1)
string_name_2 = tkinter.Label(frets_fr, text = "A")
string_name_2.grid(row=0, column=2)
string_name_3 = tkinter.Label(frets_fr, text = "D")
string_name_3.grid(row=0, column=3)
string_name_4 = tkinter.Label(frets_fr, text = "G")
string_name_4.grid(row=0, column=4)
string_name_5 = tkinter.Label(frets_fr, text = "B")
string_name_5.grid(row=0, column=5)
string_name_6 = tkinter.Label(frets_fr, text = "E")
string_name_6.grid(row=0, column=6)

output_0_0 = tkinter.Label(frets_fr,textvariable=output_str_0_0)
output_0_0.grid(row=1,column=1)
output_0_1 = tkinter.Label(frets_fr,textvariable=output_str_0_1)
output_0_1.grid(row=1,column=2)
output_0_2 = tkinter.Label(frets_fr,textvariable=output_str_0_2)
output_0_2.grid(row=1,column=3)
output_0_3 = tkinter.Label(frets_fr,textvariable=output_str_0_3)
output_0_3.grid(row=1,column=4)
output_0_4 = tkinter.Label(frets_fr,textvariable=output_str_0_4)
output_0_4.grid(row=1,column=5)
output_0_5 = tkinter.Label(frets_fr,textvariable=output_str_0_5)
output_0_5.grid(row=1,column=6)

output_1_0 = tkinter.Label(frets_fr,textvariable=output_str_1_0)
output_1_0.grid(row=2,column=1)
output_1_1 = tkinter.Label(frets_fr,textvariable=output_str_1_1)
output_1_1.grid(row=2,column=2)
output_1_2 = tkinter.Label(frets_fr,textvariable=output_str_1_2)
output_1_2.grid(row=2,column=3)
output_1_3 = tkinter.Label(frets_fr,textvariable=output_str_1_3)
output_1_3.grid(row=2,column=4)
output_1_4 = tkinter.Label(frets_fr,textvariable=output_str_1_4)
output_1_4.grid(row=2,column=5)
output_1_5 = tkinter.Label(frets_fr,textvariable=output_str_1_5)
output_1_5.grid(row=2,column=6)

output_2_0 = tkinter.Label(frets_fr,textvariable=output_str_2_0)
output_2_0.grid(row=3,column=1)
output_2_1 = tkinter.Label(frets_fr,textvariable=output_str_2_1)
output_2_1.grid(row=3,column=2)
output_2_2 = tkinter.Label(frets_fr,textvariable=output_str_2_2)
output_2_2.grid(row=3,column=3)
output_2_3 = tkinter.Label(frets_fr,textvariable=output_str_2_3)
output_2_3.grid(row=3,column=4)
output_2_4 = tkinter.Label(frets_fr,textvariable=output_str_2_4)
output_2_4.grid(row=3,column=5)
output_2_5 = tkinter.Label(frets_fr,textvariable=output_str_2_5)
output_2_5.grid(row=3,column=6)

output_3_0 = tkinter.Label(frets_fr,textvariable=output_str_3_0)
output_3_0.grid(row=4,column=1)
output_3_1 = tkinter.Label(frets_fr,textvariable=output_str_3_1)
output_3_1.grid(row=4,column=2)
output_3_2 = tkinter.Label(frets_fr,textvariable=output_str_3_2)
output_3_2.grid(row=4,column=3)
output_3_3 = tkinter.Label(frets_fr,textvariable=output_str_3_3)
output_3_3.grid(row=4,column=4)
output_3_4 = tkinter.Label(frets_fr,textvariable=output_str_3_4)
output_3_4.grid(row=4,column=5)
output_3_5 = tkinter.Label(frets_fr,textvariable=output_str_3_5)
output_3_5.grid(row=4,column=6)

output_4_0 = tkinter.Label(frets_fr,textvariable=output_str_4_0)
output_4_0.grid(row=5,column=1)
output_4_1 = tkinter.Label(frets_fr,textvariable=output_str_4_1)
output_4_1.grid(row=5,column=2)
output_4_2 = tkinter.Label(frets_fr,textvariable=output_str_4_2)
output_4_2.grid(row=5,column=3)
output_4_3 = tkinter.Label(frets_fr,textvariable=output_str_4_3)
output_4_3.grid(row=5,column=4)
output_4_4 = tkinter.Label(frets_fr,textvariable=output_str_4_4)
output_4_4.grid(row=5,column=5)
output_4_5 = tkinter.Label(frets_fr,textvariable=output_str_4_5)
output_4_5.grid(row=5,column=6)

output_list = [[fret_num_1, fret_num_2, fret_num_3,
                fret_num_4, fret_num_5],

               [string_name_1, string_name_2, string_name_3,
                string_name_4, string_name_5, string_name_6],
               
               [output_0_0, output_0_1, output_0_2,
                output_0_3, output_0_4, output_0_5],

               [output_1_0, output_1_1, output_1_2,
                output_1_3, output_1_4, output_1_5],

               [output_2_0, output_2_1, output_2_2,
                output_2_3, output_2_4, output_2_5],

               [output_3_0, output_3_1, output_3_2,
                output_3_3, output_3_4, output_3_5],

               [output_4_0, output_4_1, output_4_2,
                output_4_3, output_4_4, output_4_5]]


for output in output_list:
    for var in output:
        var.configure(font=(font_family, int(font_size_base*0.6))) 

# Input

input_label = tkinter.Label(input_fr, text = "Enter Chord:")
input_label.configure(font = (font_family, int(font_size_base*0.6)))
input_label.pack(side="top")

input_entry = tkinter.Entry(input_fr)
input_entry.pack(side="left")

def update_output():
    chord = eval(input_entry.get())
    chord_name_str.set(create_tab_data(chord)["Name"])
    for i, j in zip(output_str_list, list(create_tab_data(chord)["Tab"])):
        for k, l in zip(i, list(j)):
            if l == 0:
                k.set("-")
            if l == 1:
                k.set("x")
    
input_button = tkinter.Button(input_fr, text="OK", command=update_output)
input_button.pack(side="left")

# Mainloop

window.mainloop()

