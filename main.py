import App
import PageOne
import PageTwo
import PageThree

def main:

    app = App(
        PageOne,
        PageTwo,
        PageThree
    )
    app.mainloop()

if __name__ == "__main__":

    main()
