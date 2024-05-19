"""
This covers the graphic user interface development of the to_do app
"""

import functions
import FreeSimpleGUI as sg

# Define variables to be used in the gui development
label = sg.Text("Type in a to-do")              # The label adds a suggestion over the input box
input_box = sg.InputText(tooltip="Enter Todo")  # The input box to type in the to-do action
add_button = sg.Button("Add")                   # The Add button is created to enable users add the to-do action

window = sg.Window('My Todo App',
                   layout=[[label],                     # The layout positions the label at the first line
                           [input_box, add_button]])    # This layout positions the input box and add_button at the next line
window.read()
window.close()
