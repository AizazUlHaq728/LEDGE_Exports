from flet import *
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
import firebase_setup
import re
firebase_setup.initialize_firebase()
def main(page: Page) -> None:
    page.title = 'Sign Up'
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    # Setup fields
    text_username: TextField = TextField(label='Username', text_align=TextAlign.LEFT, width=200)
    text_email: TextField = TextField(label='Email', text_align=TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=TextAlign.LEFT, width=200)

    # Checkboxes for user type
    checkbox_executive: Checkbox = Checkbox(label='Executive', value=False)
    checkbox_collector: Checkbox = Checkbox(label='Collector', value=False)

    checkbox_agree: Checkbox = Checkbox(label="I agree to the terms", value=False)
    button_submit: ElevatedButton = ElevatedButton(text="Sign up", width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        email_valid = re.match(r'^[\w\.-]+@[\w\.-]+$', text_email.value)
        if all([text_username.value, email_valid, text_password.value, user_type_selected(), checkbox_agree.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        username = text_username.value
        email = text_email.value
        password = text_password.value
        user_type = "Executive" if checkbox_executive.value else "Collector"

        if checkbox_agree.value:
            user = firebase_setup.sign_up(username, email, password, user_type)
            print(user)
            if user:
                page.clean()
                page.add(
                    Row(
                        controls=[Text(value=f'Welcome: {username}', size=20)],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
        else:
            print("Please agree to the terms before signing up.")

    def user_type_selected() -> bool:
        # Ensure only one of the checkboxes is selected at a time
        return checkbox_executive.value or checkbox_collector.value

    def unselect_other_checkbox(checkbox):
        if checkbox == checkbox_executive:
            checkbox_collector.value = False
        elif checkbox == checkbox_collector:
            checkbox_executive.value = False

    # Attach event handlers
    checkbox_agree.on_change = validate
    text_username.on_change = validate
    text_email.on_change = validate
    text_password.on_change = validate

    checkbox_executive.on_change = lambda e: (unselect_other_checkbox(checkbox_executive), validate(e))
    checkbox_collector.on_change = lambda e: (unselect_other_checkbox(checkbox_collector), validate(e))

    button_submit.on_click = submit

    # Render page
    page.add(
        Row(
            controls=[
                Column(
                    [text_username, text_email, text_password, checkbox_executive, checkbox_collector, checkbox_agree, button_submit]
                )
            ],
            alignment=MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    app(target=main)
