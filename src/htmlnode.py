class HTMLNode():
    def __init__(self, tag=None,value=None,children=None,props=None):
        """
        tag -> Refers to html tag like <p>, <a>
        value -> Refers to content inside the tag
        children -> Refers to a list of HTMLNode objects 
        props -> Refers to a dictionary of attribute for the tag like {"href": "https://google.com"} 
        
        """
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return "".join(f' "{key}:{value}"' for key,value in self.props.items())
       
    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value}, {self.children!r}, {self.props!r})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
        
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        # Default props to an empty dictionary if not provided
        props = props or {}
        super().__init__(tag=tag, value=value, children=[], props=props)
        if not value:
            raise ValueError("LeafNode requires a non-empty value.")
        
    def to_html(self):
    # Generate the string for the tag's properties
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        # Combine the tag, properties, value, and closing tag
        if self.tag == None:
            return self.value
        
        if not props_str:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
