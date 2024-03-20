from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None or len(self.children) == 0:
            raise ValueError
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        return result + f"</{self.tag}>"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, ParentNode):
            return False
        return self.tag == __value.tag and self.children == __value.children and self.props == __value.props
