def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(9 / 5 * input.temperature() + 32)
input.on_button_pressed(Button.B, on_button_pressed_b)

music.set_built_in_speaker_enabled(True)
soundExpression.giggle.play()