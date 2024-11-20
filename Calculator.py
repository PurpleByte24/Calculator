from guizero import App, Text, PushButton

##App
app = App(title="NCalc", bg=(0,0,156),layout="grid", height = 218, width = 320)
app.text_color = 0, 0, 0

##Strings
rechnung = ""
neu = "ja"
dot = "nein"
minusop = False

##Listen
number=[""]
ops=["+", " - ", "*", "/", "."]
allsigns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "."]
numbers=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

##Definitionen
def add(wert, operation):
    neurech()
    global dot, minusop
    if results.value == "0":
        results.clear()
    if operation == None:
        number.append(wert)
        results.append(wert)
        minusop = False
    ##adding Ops & Dot
    if operation == "." and number[len(number)-1] not in ops:
        if dot == "nein":
            number.append(operation)
            results.append(operation)
            dot = "ja"
    if operation == "+" and number[len(number)-1] not in ops and minusop == False:
        number.append(operation)
        results.append(" " + operation + " ")
        dot = "nein"
    if operation == "/" and number[len(number)-1] not in ops and minusop == False:
        number.append(operation)
        results.append(" " + operation + " ")
        dot = "nein"
    if operation == "*" and number[len(number)-1] not in ops and minusop == False:
        number.append(operation)
        results.append(" " + operation + " ")
        dot = "nein"
    if operation == "-":
        minus()
    print(number)
        
def minus():
    global dot, minusop
    ##negative Zahlen
    if (results.value == "") or \
        number[len(number)-1] in ops:
        results.append("-")
        number.append("-")
        minusop=True
    elif number[len(number)-1] not in ops and minusop == False:
        number.append(" - ")
        results.append(" - ")
        dot = "nein"
        minusop=True
       
def neurech():
    global neu
    if neu == "ja":
        results.clear()
        number.clear()
        results.append("0")
        neu = "nein"
    
def clear():
    global neu
    number.clear()
    results.clear()
    results.append("0")
    print(number)
    neu = "ja"
    
def calc(operation):
    global rechnung, neu
    rechnung = results.value
    try:
        resultat = eval(rechnung)
        print(resultat)
        results.append(" " + operation + " ")
        results.append(str(resultat))
    except Exception as e:
        results.clear()
        results.append("Fehler: " + str(e))
    neu = "ja"
    number.clear()

def key_pressed(event):
    print(event.key)
    if event.key in allsigns:
        if event.key in numbers:
            add(event.key, None)
        if event.key in ops or event.key == "-":
            add(None, event.key)
    if event.tk_event.keysym == "Return":
        calc("=")
    if event.tk_event.keysym == "c" or event.tk_event.keysym == "C":
        clear()
    if event.tk_event.keysym == "BackSpace":
        number.pop()
        results.value = results.value[:-1]
    
##Resultat
results = Text(app, grid=[0,0,5,1], width=35, color = (255, 255, 255))
results.text_size = 16
results.append("0")

##Buttons
button1 = PushButton(app, text="1", grid=[0,1], width=1, command=add, args=[1, None])
button2 = PushButton(app, text="2", grid=[1,1], width=1, command=add, args=[2, None])
button3 = PushButton(app, text="3", grid=[2,1], width=1, command=add, args=[3, None])
button4 = PushButton(app, text="4", grid=[0,2], width=1, command=add, args=[4, None])
button5 = PushButton(app, text="5", grid=[1,2], width=1, command=add, args=[5, None])
button6 = PushButton(app, text="6", grid=[2,2], width=1, command=add, args=[6, None])
button7 = PushButton(app, text="7", grid=[0,3], width=1, command=add, args=[7, None])
button8 = PushButton(app, text="8", grid=[1,3], width=1, command=add, args=[8, None])
button9 = PushButton(app, text="9", grid=[2,3], width=1, command=add, args=[9, None])
button0 = PushButton(app, text="0", grid=[1,4], width=1, command=add, args=[0, None])
buttondot = PushButton(app, text=".", grid=[2,4], width=1, command=add, args=[None, "."])

buttonadd = PushButton(app, text="+", grid=[3,1], width=1, command=add, args=[None, "+"])
buttonsub = PushButton(app, text="-", grid=[3,2], width=1, command=add, args=[None, "-"])
buttonmul = PushButton(app, text="*", grid=[3,3], width=1, command=add, args=[None, "*"])
buttondiv = PushButton(app, text="/", grid=[3,4], width=1, command=add, args=[None, "/"])

buttoneq = PushButton(app, text="=", grid=[4,1,1,4], width=1, height=10, command=calc, args=["="])
buttonC = PushButton(app, text="C", grid=[0,4], width=1, command=clear)

##Tastatur
app.when_key_pressed = key_pressed

app.display()