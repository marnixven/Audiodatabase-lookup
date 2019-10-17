import PySimpleGUI as sg
import requests

#print(sg.ListOfLookAndFeelValues())
sg.ChangeLookAndFeel('Reddit')

layout = [      
          [sg.Text('Artiest of bandnaam:')],      
          [sg.Text('', size=(15, 1)), sg.InputText(key='-IN-')],           
          [sg.Submit()]    
         ]

window = sg.Window('Artiest en band info').Layout(layout)         
button, values = window.Read()

text_input = values['-IN-'].replace(' ','_')
parameters = {}
parameters ['s'] = text_input

response = requests.get("https://www.theaudiodb.com/api/v1/json/1/search.php?s=", params=parameters)

def button1():
    sg.Popup(response.json()['artists'][0]['strArtistLogo'])

def button2():
    sg.Popup(response.json()['artists'][0]['strCountry'])

def button3():
    sg.Popup(response.json()['artists'][0]['intFormedYear'])

def button4():
    sg.Popup(response.json()['artists'][0]['strWebsite'])

def button5():
    sg.PopupScrolled('ENGELS\n', response.json()['artists'][0]['strBiographyEN'],
      '\n\nNEDERLANDS\n', response.json()['artists'][0]['strBiographyNL'])

func_dict = {'Logo':button1,'Herkomst':button2, 'Formatiejaar':button3, 'Website':button4, 'Biografie':button5}

layout = [[sg.Text('', auto_size_text=True)],
          [sg.Button('Logo'),sg.Button('Herkomst'), sg.Button('Formatiejaar'), sg.Button('Website'), sg.Button('Biografie'), sg.Quit()]]

window = sg.Window('Welke informatie wil je ophalen?', layout)

while True:
    event, value = window.Read()
    if event in ('Quit', None):
        break
    try:
        func_to_call = func_dict[event]   # look for a match in the function dictionary
        func_to_call()                    # if successfully found a match, call the function found
    except:
        pass
    
window.Close()

#sg.PopupOK('Done')