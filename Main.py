import PySimpleGUI as Sg

input_column = [[Sg.Text("enter your query")],
                [Sg.Multiline(size=(50, 20), key='textbox')],
                [Sg.Button('Execute'), Sg.Button('Close Window')]]
output_column = [[Sg.Text("output")],
                 [Sg.Multiline(size=(50, 20), key='textboxa')]]
layout = [[Sg.Column(input_column),
            Sg.VSeperator(),
           Sg.Column(output_column)]]
window = Sg.Window("Query executor", layout)
while True:
    event, values = window.read()
    if event == "Execute":
        pass
    elif event == "Close Window" or event == Sg.WIN_CLOSED:
        break
window.close()
