from htmlnode import HTMLNode

def test_htmlnode():
    # Create an HTMLNode instance
    node = HTMLNode(tag='a', value='Click Here', props={'href': 'https://www.example.com'})
    
    # Test __repr__ method
    print(node)  # Expect to see the tag, value, children, and props in the output
    
    # Test props_to_html method
    props_str = node.props_to_html()
    print(props_str)  # Expect to see: 'href="https://www.example.com"'
    
    child1 = HTMLNode(tag='span', value='Child Node 1') 
    child2 = HTMLNode(tag='span', value='Child Node 2')
    
    parent_node = HTMLNode(tag='div',children=[child1, child2])
    
    print(parent_node)

    assert str(node) == "HTMLNode(a, Click Here, None, {'href': 'https://www.example.com'})"
    assert props_str == 'href="https://www.example.com"'
    assert str(parent_node) == "HTMLNode(div, None, [HTMLNode(span, Child Node 1, None, None), HTMLNode(span, Child Node 2, None, None)], None)"

# Run the test
test_htmlnode()