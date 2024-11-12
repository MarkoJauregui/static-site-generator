from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props={}):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return f"{self.value}"
        else:
            formatted_props = self.props_to_html()
            props_str = f" {formatted_props}" if formatted_props else ""
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"