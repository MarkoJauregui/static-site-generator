from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, props)
        self.children = children

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag found")
        if not self.children:
            raise ValueError("No children found")

        children_html = ""
        for child in self.children:
            child_html = child.to_html()
            children_html += child_html

        if self.props:
            props_html = " " + self.props_to_html()
        else:
            props_html = ""

        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
