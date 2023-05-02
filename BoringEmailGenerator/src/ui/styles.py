from tkinter import ttk


# COLORS:
bg_colour = "#bbe1fa"

button_disabled = "8c8c8c"
button_pressed = '#000033'

# Pink button
pink_background = '#be76c4'
pink_background_active = '#fca9f8'

# Purple button
purple_background = '#6666cc'
purple_background_active = '#bc5bf0'

# Red button
red_background = '#cc2b5b'
red_background_active = '#de4831'

# Green button
green_background = '#2bcc3b'
green_background_active = '#89e639'

# Yellow  button
yellow_background = '#ab9e13'
yellow_background_active = '#e8c515'


def configure_main_window_styles():
    configure_combobox_style('TCombobox')
    configure_button_style(
        'Manage.TButton', purple_background, purple_background_active)
    configure_button_style(
        'Delete.TButton', red_background, red_background_active)
    configure_button_style(
        'Copy.TButton', green_background, green_background_active)
    configure_button_style('Translate.TButton',
                           pink_background, pink_background_active)
    configure_textarea_style('ScrolledText')


def configure_management_window_styles():
    configure_group_background_style('Group.TFrame')
    configure_button_style(
        'Group.TButton', purple_background, purple_background_active)
    configure_button_style(
        'New.TButton', yellow_background, yellow_background_active)
    configure_button_style(
        'Delete.TButton', red_background, red_background_active)
    configure_button_style(
        'Save.TButton', green_background, green_background_active)
    configure_button_style(
        'Cancel.TButton', red_background, red_background_active)
    configure_button_style(
        'Create.TButton', green_background, green_background_active)


def configure_messagebox_style():
    messagebox_style = ttk.Style()
    messagebox_style.configure(
        'Info.Messagebox', background=bg_colour, font=("Georgia", 12))


def configure_combobox_style(style_name):
    combobox_style = ttk.Style()
    combobox_style.configure(style_name, padding=(5, 2, 5, 2))


def configure_button_style(style_name, background_color, background_active):
    button_style = ttk.Style()
    button_style.theme_use('default')
    button_style.configure(style_name, padding=6, relief="flat", font=(
        'Georgia', 12, 'bold'), background=background_color, foreground='black')
    button_style.map(style_name, background=[('active', background_active), (
        'disabled', button_disabled)], foreground=[('pressed', button_pressed), ('active', 'black')])


def configure_textarea_style(style_name):
    textarea_style = ttk.Style()
    textarea_style.configure(style_name, background='#F0F0F0', foreground='black', font=(
        'Consolas', 12), relief='flat', borderwidth=2, padx=5, pady=5)


def configure_group_background_style(style_name):
    background_style = ttk.Style()
    background_style.configure(style_name, background=bg_colour)
