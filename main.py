import json
from app import App
from page_one import PageOne
from page_two import PageTwo
from page_three import PageThree

def main ():

    config = {
    
        "1" : PageOne,
        "2" : PageTwo
    
    }

    app = App(config)
    app.mainloop()

if __name__ == "__main__":

    main()
