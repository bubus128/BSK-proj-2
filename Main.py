import PySimpleGUI as Sg

layout = [[Sg.Text('type your query below')],
          [Sg.Button('Execute'), Sg.Button('Close Window')],
          [Sg.Multiline(size=(30, 5), key='textbox')]]
window = Sg.Window("Query executor", layout)
while True:
    event, values = window.read()
    if event == "Execute":
        pass
    elif event == "Close Window" or event == Sg.WIN_CLOSED:
        break
