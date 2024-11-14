from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []

    for node in old_nodes:
        new_nodes = []

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError("Unmatched delimiter found in text")

        for index, part in enumerate(parts):
            if index % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

        result_nodes.extend(new_nodes)

    return result_nodes
