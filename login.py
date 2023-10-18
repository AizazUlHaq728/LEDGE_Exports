from flet import *
from flet import TextField,Checkbox,ElevatedButton,Text,Row,Column
from flet_core.control_event import ControlEvent

def main(page:Page)-> None:
        page.title= 'Sign up'
        page.vertical_alignment=MainAxisAlignment.CENTER
        page.theme_mode=ThemeMode.LIGHT
        page.window_width=400
        page.window_height=400
        page.window_resizable=False

        # setup fields
        text_username:TextField =TextField(label='Username',text_align=TextAlign.LEFT,width=200)
        text_password:TextField =TextField(label='Password',text_align=TextAlign.LEFT,width=200,password=True)
        checkbox_signup:Checkbox=Checkbox(label="i agree to stuff",value=False)
        button_submit: ElevatedButton= ElevatedButton(text="Sign up",width=200,disabled=True)

        def validate(e:ControlEvent)->None:
                if all([text_username.value,text_password.value,checkbox_signup.value]):
                        button_submit.disabled=False
                else:
                    button_submit.disabled=True

                page.update()

        def submit(e:ControlEvent)->None:
               print("User name: ",text_username.value)
               print("Password: ", text_password.value)

               page.clean()
               page.add(
                      Row(
                             controls=[Text(value=f'Welcome: {text_username.value}',size=20)],
                             alignment=MainAxisAlignment.CENTER
                      )
               )
        checkbox_signup.on_change = validate#linking validate function
        text_username.on_change=validate
        text_password.on_change=validate
        button_submit.on_click=submit

        #render page

        page.add(
               Row(
                      controls=[
                             Column(
                                    [text_username,
                                     text_password,
                                     checkbox_signup,
                                     button_submit]
                             )
                      ],
                      alignment=MainAxisAlignment.CENTER
               )
        )
    
if __name__=="__main__":
       app(target=main)
