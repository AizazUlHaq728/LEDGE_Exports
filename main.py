from flet import *
def main(page:Page):
   myTabs=Tabs(
      selected_index=1,
      animation_duration=400,
      tabs=[
        Tab(
            tab_content=Icon(name="home"),
            content=Container(
               content=Text("Sellers",size=20)
            )
            ),
        Tab(
            tab_content=Icon(name="home"),
            content=Container(
               content=Text("Products",size=20)
            )
           
        ),
        Tab(
            tab_content=Icon(name="home"),
            content=Container(
               content=Text("Buyers",size=20)
            )
        )
      ],
      expand=1
   )
   page.add(
      Column([
         Text("Ledge Works",size=30,weight='bold'),
         myTabs
      ])
    
   )

app(target=main)
