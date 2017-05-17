import Tkinter as tkinter
import tkMessageBox
import webbrowser


# noinspection PyUnusedLocal
class Values:
    def __init__(self):
        pass
        # Global variables needed to calculate the Q value
        self.cof = 0
        self.mass = 0
        self.temp = 0
        self.calc = 0
        self.matselect = ""
        self.matchosen = False
        self.SHC_WATER = 4190
        self.SHC_RUBBER = 2500
        self.SHC_POLY = 2100
        self.SHC_OIL = 1800
        self.SHC_AIR = 1005
        self.SHC_LIME = 909
        self.SHC_BRICK = 810
        self.SHC_STEEL = 460
        self.SHC_COPPER = 385
        self.mattext = ""

    # Method to select the heat coefficient of a material
    def materialselect(self, num):
        # selection = raw_input('Please enter your material: ').lower()

        self.matselect = num

        if self.matselect == "7":
            self.cof = self.SHC_WATER
            self.matchosen = True
            self.mattext = 'Water'
            print self.cof

        elif self.matselect == "8":
            self.cof = self.SHC_RUBBER
            self.matchosen = True
            self.mattext = 'Rubber'
            print self.cof

        elif self.matselect == "9":
            self.cof = self.SHC_POLY
            self.matchosen = True
            self.mattext = 'Polystyerene'
            print self.cof

        elif self.matselect == "4":
            self.cof = self.SHC_OIL
            self.matchosen = True
            self.mattext = 'Oil'
            print self.cof


        elif self.matselect == "5":
            self.cof = self.SHC_AIR
            self.matchosen = True
            self.mattext = 'Air'
            print self.cof

        elif self.matselect == "6":
            self.cof = self.SHC_LIME
            self.matchosen = True
            self.mattext = 'Limestone'
            print self.cof

        elif self.matselect == "1":
            self.cof = self.SHC_BRICK
            self.matchosen = True
            self.mattext = 'Brick'
            print self.cof

        elif self.matselect == "2":
            self.cof = self.SHC_STEEL
            self.matchosen = True
            self.mattext = 'Steel'
            print self.cof

        elif self.matselect == "3":
            self.cof = self.SHC_COPPER
            self.matchosen = True
            self.mattext = 'Copper'
            print self.cof

    # method to find the mass with a try and catch encapsulation
    def massselect(self):
        val = entry.get()

        try:
            val = float(val)
            self.mass = val
            print val

        except ValueError:
            print "bad input"

            # entry.delete(0, tkinter.END)

    # method to obtain the 1st and last temperatures of the material, calculate the difference and return that value

    # noinspection PyUnusedLocal
    def tempdiff(self, n):
        first_temp = temp1box.get()
        second_temp = temp2box.get()

        try:
            first_temp = float(first_temp)
            second_temp = float(second_temp)
            first_temp = round(first_temp, 4)
            second_temp = round(second_temp, 4)
            print first_temp
            print second_temp
            if first_temp < -273 or second_temp < -273:
                print 'Incorrect'
            elif first_temp > 1000 or second_temp > 1000:
                print 'Too big a value'
            else:
                diff = second_temp - first_temp
                self.temp = diff
                print diff
        except ValueError:
            print "Incorrect Input."

            # temp1box.delete(0, tkinter.END)
            # temp2box.delete(0, tkinter.END)

    # function to calculate the Heat

    def heatcofcalc(self):
        entry.config(state='disabled')
        temp1box.config(state='disabled')
        temp2box.config(state='disabled')
        self.massselect()
        self.tempdiff(temp2box)
        if self.mass == isinstance(self.mass,str):
            txtbox = tkMessageBox.showinfo(title='Incorrect Mass', message ='Please enter an integer. Decimals are allowed')
        elif self.temp == isinstance(self.temp,str):
            txtbox = tkMessageBox.showinfo(title='Incorrect Temperature', message='Please enter an integer. Decimals are accepted')
        else:
            calc = self.cof * self.mass * self.temp
            calc = round(calc, 2)

            self.calc = calc
            print self.calc
            showcalc = str(self.calc)
            txtbox = tkMessageBox.showinfo(title='Results',
                                           message='Material: %s\n Mass: %s\n Temperature Difference: %s\n Specific Heat Amount: %s Joules' % (
                                               self.mattext, self.mass, self.temp, showcalc))

    def clear(self):
        self.cof = 0
        self.mass = 0
        self.temp = 0
        self.mattext = ""

        entry.config(state='normal')
        temp1box.config(state='normal')
        temp2box.config(state='normal')
        entry.delete(0, tkinter.END)
        temp1box.delete(0, tkinter.END)
        temp2box.delete(0, tkinter.END)
        temp1box.insert(tkinter.END, 'Initial Temp')
        temp2box.insert(tkinter.END, 'Final Temp')

    def theory(self):
        twindow = tkinter.Toplevel(window)

        twindow.title("What is Specific Heat Capacity?")
        twindow.geometry("550x400")
        twindow.resizable(width=False, height=False)

        tlbl = tkinter.Label(twindow, text="Theory for Specific Heat Amount")
        tlbl.config(font=('Avenir', 20, 'bold'))
        tlbl.pack()

        tphoto = tkinter.PhotoImage(file="equation.gif")
        tequation = tkinter.Label(twindow, image=tphoto)
        tequation.image = tphoto
        tequation.pack()

        tltheory = tkinter.Text(twindow, height=6, width=500, wrap=tkinter.WORD)

        quote = """The specific heat is the amount of heat per unit mass required to raise the temperature by one degree Kelvin. The relationship between heat and temperature change is usually expressed in the form shown above where c is the specific heat. The relationship does not apply if a phase change is encountered, because the heat added or removed during a phase change does not change the temperature."""

        tltheory.config(font=('Avenir', 15))
        tltheory.insert(tkinter.END, quote)
        tltheory.config(state=tkinter.DISABLED)
        tltheory.pack()

        webbttn = tkinter.Button(twindow, text='Video Example',
                                 command=lambda: webbrowser.open("https://www.youtube.com/watch?v=BclB8UaSH4g"))
        webbttn.pack()

        rtnbttn = tkinter.Button(twindow, text='Return to Calculator', command=lambda: twindow.destroy())
        rtnbttn.pack()

        credit = tkinter.Label(twindow,
                               text='Credit: Kamal Wafi Youtube\nTheory: http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/spht.html').pack()


# array to display the SHC of the different materials
matlist = ['Water = 4190', 'Rubber = 2500', 'Polyethylene = 2100', 'Oil = 1800',
           'Air = 1005', 'Limestone = 909', 'Brick = 810', 'Steel = 460', 'Copper = 385']
matarray = '\n'.join(matlist)

runcalc = Values()
window = tkinter.Tk()
box = tkinter.Frame(window)
box.grid(row=0, column=0)

window.title("Q-Values Calculator")
window.geometry("525x400+50+50")
window.resizable(width=False, height=False)
window.iconbitmap("calculator.ico")

photo = tkinter.PhotoImage(file='logow.gif')

titlelbl = tkinter.Label(box,
                         image=photo).grid(row=0, column=0, columnspan=4)

gridbox = tkinter.Frame(window)
gridbox.grid(row=1)

units = u"\u207B" + u"\u00B9"

temppicklbl = tkinter.Label(gridbox,
                            text="Please choose a material's specific heat (J kg%s K%s)" % (units, units)).grid(row=1,
                                                                                                                column=0,
                                                                                                                columnspan=3,
                                                                                                                pady=2,
                                                                                                                padx=5)

numbers = "789456123"
i = 0
bttn = []
for j in range(1, 4):
    for k in range(3):
        bttn.append(
            tkinter.Button(gridbox, text=matlist[i]))  # command=lambda x=numbers[i]: runcalc.materialselect(x)).pack())
        bttn[i].grid(row=j + 1, column=k)
        bttn[i]["command"] = lambda x=numbers[i]: runcalc.materialselect(x)
        i += 1

massbox = tkinter.Frame(window)
massbox.grid(row=2, columnspan=3)

masslbl = tkinter.Label(massbox, text='Enter your mass (Kg)').grid(row=6, column=1)

entry = tkinter.Entry(massbox, width=10)
entry.grid(row=7, column=1)

tempbox = tkinter.Frame(window)
tempbox.grid(row=3)

kelvin = u"\u212A"
templbl = tkinter.Label(tempbox,
                        text='Enter both absolute temperatures (%s)' % kelvin)
templbl.grid(row=9, column=1, pady=5, padx=5)


def on_entry_click(self):
    if temp1box.get() == 'Initial Temp':
        temp1box.delete(0, tkinter.END)
        temp1box.insert(0, '')
    if temp2box.get() == 'Final Temp':
        temp2box.delete(0, tkinter.END)
        temp2box.insert(0, '')
def on_focusout(self):
    if temp1box.get() == '':
        temp1box.insert(0, 'Initial Temp')
    if temp2box.get() == '':
        temp2box.insert(0, 'Final Temp')


tempgrid = tkinter.Frame(window)
tempgrid.grid(row=4)
temp1box = tkinter.Entry(tempgrid, width=10, relief=tkinter.SUNKEN)
temp2box = tkinter.Entry(tempgrid, width=10, relief=tkinter.SUNKEN)

temp1box.insert(tkinter.END, 'Initial Temp')
temp2box.insert(tkinter.END, 'Final Temp')
temp1box.bind('<FocusIn>', on_entry_click)
temp2box.bind('<FocusIn>', on_entry_click)
temp1box.bind('<FocusOut>', on_focusout)
temp2box.bind('<FocusOut>', on_focusout)

temp1box.grid(row=11, column=0)
temp2box.grid(row=11, column=1)

bttnbox = tkinter.Frame(window)
bttnbox.grid(row=5, column=0)

cofbttn = tkinter.Button(bttnbox,
                         text='Calculate Q - Value', command=lambda: runcalc.heatcofcalc())
cofbttn.grid(row=14, column=1)

clrbttn = tkinter.Button(bttnbox, text='Clear', command=lambda: runcalc.clear())
clrbttn.grid(row=14, column=2)

thframe = tkinter.Frame(window)
thframe.grid(row=6, column=0)
thrybttn = tkinter.Button(thframe, text='Theory', command=lambda: runcalc.theory())
thrybttn.grid(row=15, column=0)

window.mainloop()
