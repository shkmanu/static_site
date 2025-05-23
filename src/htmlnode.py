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
            return ""
        else:
            list = []
            for item in self.props:
                value = self.props[item]
                string = f' {item}="{value}"'
                list.append(string)
            return "".join(list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        if self.value is None:
            raise ValueError("Value required")
        elif self.tag is None:
            return f"{self.value}"
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag required")
        elif self.children is None:
            raise ValueError("Children required")
        else:
            return f"<{self.tag}>{self.children_to_html()}</{self.tag}>"

    def children_to_html(self):
        html_children = ""
        for child in self.children:
            if not child.children is None:
                html_children += f"{ParentNode.to_html(child)}"
            elif child.children is None:
                html_children += f"{LeafNode.to_html(child)}"
        return html_children
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"