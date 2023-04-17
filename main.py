import json
from app import App
from page_one import PageOne
from page_two import PageTwo
from page_three import PageThree

def main ():

    app = App([
        PageOne,
        PageTwo,
        PageThree
    ])
    app.mainloop()

if __name__ == "__main__":

    main()
