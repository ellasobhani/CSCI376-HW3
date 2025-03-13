from nicegui import ui

ui.colors(
      primary='#1976d2',
      secondary='#26A69A',
      accent='#9C27B0',
      positive='#21BA45',
      negative='#C10015',
      info='#31CCEC',
      warning='#F2C037'
)

# Function to update displayed temperature dynamically
def update_display(value):
    temp_display.set_text(f"Selected Temperature: {value}°")  # Live update

def convert(result_label, type_of_input):
    try: 
        temp = float(type_of_input.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: the result label will be in the color indicated by 'positive' in ui.colors
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: the result label will be in the color indicated by 'negative' in ui.colors

with ui.row().classes("mx-auto gap-4"):     
    with ui.card().classes("w-100 h-[450px] p-6 shadow-xl mx-auto mt-10 rounded-xl bg-gradient-to-b from-white to-gray-700" ):
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 text-center")
        #dynamic temperature display, updated instantly
        temp_display = ui.label("Selected Temperature: 25°").classes("text-xl font-bold text-primary mb-4 text-center")
        #slider input
        temp_slider = ui.slider(min=-50, max=150, value=25, step=1, on_change=lambda e: update_display(e.value)).classes("mb-4 w-full bg-white py-2 px-4")
        #conversion type selection
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        #result label
        slider_label = ui.label("").classes("text-lg mt-4 text-center")
        #convert button
        ui.button("Convert", on_click=lambda: convert(slider_label, temp_slider)).classes("bg-primary text-white font-bold py-2 px-4 rounded hover:bg-blue-700")
    

    with ui.card().classes("w-100 h-[450px] p-6 shadow-xl mx-auto mt-10 rounded-xl bg-gradient-to-b from-white to-gray-700 min-h-[300px]"):
        # w-100: Set element width to be fixed at 100
        # p-6: adds 24px padding
        # shadow-xl: adds an extra-large shadow
        # mx-auto: the card is centered horizontally
        # mt-10: adds 40px to the top margin
        # rounded-xl: adds extra-large rounding to the card's corners
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 text-center")
        # text-2xl: sets text font size to 24px
        # font-bold: sets text to be bold
        # text-accent: colors the text to be the accent color from ui.colors
        # mb-4: adds 16px to the bottom margin for spacing purposes
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-white border-4 border-info focus-within:border-blue-700")
        # w-full: enlargens the input area to fill the card
        # border: adds a border around the input area
        # rounded: rounds the corners of the border
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        input_label = ui.label("").classes("text-lg mt-4")
        convert_button = ui.button("Convert", on_click=lambda: convert(input_label, input_field)).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: sets the text of the button to white
        # py-2: adds 8px vertical padding to both the top and botton in the button
        # px-4: adds 16px horizontal padding to both the left and right in the button

ui.run()