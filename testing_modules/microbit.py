class Button():
    def __init__(self, parent=None):
        self.pressed = False
        self.press_history = False

    def press(self):
        self.pressed = True
        self.press_history = True

    def unpress(self):
        self.pressed = False

    def is_pressed(self):
        state = self.pressed
        return state

    def was_pressed(self):
        state = self.press_history
        self.press_history = False
        return state

class ButtonHistory():
    """ Mocking Class to record button presses """
    def __init__(self):
        self.buttons = {}
        self.press_history = []
        self.press_call_state = []

    def add_button(self, name, button):
        """ Binds a button to this object

        Notes
        -----
        Buttons have unique names.

        Examples
        --------
        add_button('a', button_a) => 'a' in history activates button_a
        """

        if name in self.buttons:
            raise KeyError(f"Button name {name} already exists")
        self.buttons[name] = button

    def load_history(self, history):
        """ Add to the button press history

        Parameters
        ----------
        history : list
            list of button names. list can contain lists.

        Examples
        --------
        self.load_history(['a', 'b', 'a', 'b'])
        self.load_history(['a', ['a', 'b'], 'b'])
        """
        self.press_history.extend(history)

    def next_button(self):
        """ Updates the button presses

        Notes
        -----
        If the call stack (press_call_state) is non-empty, that means that there are buttons that
        have not yet called is_pressed that could still call it (for example in multi-press states)
        In this case, we block the button_press update until that stack clears.
        """
        for button in self.press_call_state:
            self.buttons[button].unpress()
        next_buttons = self.press_history.pop(0)
        for next_button in next_buttons:
            self.buttons[next_button].press()
        self.press_call_state = next_buttons

class Image(str):
    # if you use any of the in-built Images, you'll need to specify them here
    # e.g.
    # self.HAPPY = "00000:09090:00000:90009:09990"
    pass

class Display():
    def __init__(self):
        self.state = [[0]*5]*5 # blank screen
        self.scroll_state = ""

    def show(self, image, **kwargs):
        # expects an Image object i.e. str object
        if isinstance(image, list):
            for subimage in image:
                self.show(subimage, **kwargs)
                return
        if isinstance(image, Image):
            rows = image.split(":")
            assert len(rows) == 5
            for idx, row in enumerate(rows):
                assert len(row) == 5
                self.state[idx] = [int(val) for val in row]
        if isinstance(image, str):
            # this is not the actual behaviour, but the actual behaviour requires a font,
            # which is too complex to test against
            self.state = [[image]*5]*5

    def scroll(self, string, **kwargs):
        self.scroll_state = string
        self.show(string[-1], **kwargs)

    @staticmethod
    def on():
        pass
        
    @staticmethod
    def off():
        pass

    def clear(self):
        self.state = [[0]*5]*5
        self.scroll_state = ""

def sleep(n):
    """ Used to step in time """
    if n > 0:
        button_history.next_button()

button_a = Button()
button_b = Button()
display = Display()

button_history = ButtonHistory()
button_history.add_button('a', button_a)
button_history.add_button('b', button_b)
