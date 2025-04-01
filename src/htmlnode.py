class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            pass
        else:
            list = []
            for item in self.props:
                value = self.props[item]
                string = f'{item}="{value}"'
                list.append(string)
            return " ".join(list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        if self.value is None:
            raise ValueError("Value required")
        elif self.tag is None:
            return f"{self.value}"
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        