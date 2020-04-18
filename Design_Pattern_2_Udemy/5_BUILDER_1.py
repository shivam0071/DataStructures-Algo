class HTMLElement:
    indent_size = 2  # +1 point here, we used spacebar in non class approach

    def __init__(self, name="", text=""): # Name is the name of the element and text it the actual text
        self.name = name
        self.text = text
        self.elements = [] # Why is this used? Lets find out - > element here has HTMLElements in it

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)   # if indent is 0 then i is ' ', change indent value add indentations, quite F-ed up logic
        lines.append(f'{i}<{self.name}>')   # creating first opening tag here

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size) # --> '  '
            lines.append(f'{i1}{self.text}') # Adding text to list, no tags in this

        #
        for e in self.elements:
            lines.append(e.__str(indent + 1))  # recursive. based on elements

        lines.append(f"{i}</{self.name}>") # closing the initially opened tag, no hardcoding

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HTMLBuilder(name)

class HTMLBuilder:
    __root = HTMLElement() # Why?

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )

    def add_nest(self, nest_name, nest_text):
        self.__root.elements[-1].elements.append(HTMLElement(nest_name, nest_text))

    def clear(self):
        self.__root = HTMLElement()

    def __str__(self): # this calls __str__ of the HTMLElement class which inturns expands the HTML
        return str(self.__root)

if __name__ == "__main__":
    # REQUIREMENT 1 - Build a simple HTML paragraph using a LIST
    # input - text or [<p>, text ,</p>]
    # output - <p> Hello </p>

    # Lets do it using basic code
    text = "Hello"
    parts = ["<p>", text ,"</p>"]
    print(''.join(parts))

    # Cool
    # Now Requirement 2 - HTML LIST with 2 words in it
    # input: words - ["Hello","World"], parts ["<ul>"]
    # output -
    # <ul>
    # <li>Hello</l1>
    # <li>World</l1>
    # </ul>
    words = ["Hello", "World"]
    parts = ["<ul>"]
    for w in words:
        parts.append("  <li>" + w +"</li>")
    parts.append("</ul>")
    print('\n'.join(parts))
    # NICE



    # LETS BUILD A CLASS FOR THIS for no REASON at all
    # now lets try to create objects for this class
    print("*" * 20)
    print("CLASS BASED SOLUTIONS")
    ul = HTMLElement("ul")
    ul.elements.extend([HTMLElement("li", "Hello"), HTMLElement("li", "World")])
    print(ul)
    # So this is the procedure without using a builder class
    # Lets add a <p> tag in the <li> tag and create nested structure
    print("*" * 20)
    print("CLASS BASED NESTED OBJECT CREATION")
    nested = HTMLElement("ul")

    nest_me = HTMLElement("li", "World")
    nest_me.elements.append(HTMLElement("p", "All the teaching in the world today"))

    nested.elements.append(HTMLElement("li", "Hello"))
    nested.elements.append(nest_me)
    print(nested)

    # DAYUM thats a lot of effort man....for each new nest we have
    # to create a new Object so that we can add a new inner tag to its elements list....
    # this is maddening

    # LETS SEE how thing changes if we ADD a builder to build the objects
    print("*" * 20)
    print("BUILDER SOLUTIONS")
    builder = HTMLBuilder('ul')
    builder.add_child('li','Hello')
    builder.add_child('li', 'World')
    print(builder)
    builder.clear()
    print(builder)
    # DANG, this one is clean and easy as we dont have to access the data members of a class
    # and creat too many object....very clean

    # lets try nested
    print("*" * 20)
    print("BUILDER NESTED SOLUTIONS")
    builder2 = HTMLBuilder('ul')
    builder2.add_child('li', 'Hello')
    builder2.add_child('li', 'World')
    builder2.add_nest('p', 'I am a para inside li')
    print(builder2)
    # THIS WORKS but the new elements are being appended to old data, as __root is class variable is
    # has the old info even when a new obj is created whatttttt?

    # LETS ADD a static method in HTMLElement
    print("*" * 20)
    print("BUILDER3 with static method  SOLUTIONS")
    builder3 = HTMLElement.create('UL')
    print(builder3)
    # Still same problem lol