from nicegui import ui

def greet_user():
    name = name_input.value
    label.text = f"hello {name}"

name_input = ui.input(
    label = "enter your name"
)

greet_button = ui.button("greet", on_click = greet_user)

label = ui.label("")

ui.run(host='0.0.0.0', port=8080, reload=False)
