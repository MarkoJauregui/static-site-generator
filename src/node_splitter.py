from textnode import TextNode, TextType
from text_extraction import extract_markdown_images, extract_markdown_links


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


def split_nodes_link(old_nodes):
    result_nodes = []

    for node in old_nodes:
        current_text = node.text
        new_nodes = []

        while current_text:
            link_and_url = extract_markdown_links(current_text)
            if link_and_url:
                link, url = link_and_url[0]
                parts = current_text.split(f"[{link}]({url})", 1)

                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))

                new_nodes.append(TextNode(link, TextType.LINK, url))

                current_text = parts[1]
            else:
                break

        if current_text.strip():
            new_nodes.append(TextNode(current_text, TextType.TEXT))

        result_nodes.extend(new_nodes)

    return result_nodes


def split_nodes_image(old_nodes):
    result_nodes = []

    for node in old_nodes:
        current_text = node.text
        new_nodes = []

        while current_text:
            alt_and_url = extract_markdown_images(current_text)
            if alt_and_url:
                alt, url = alt_and_url[0]
                parts = current_text.split(f"![{alt}]({url})", 1)

                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))

                new_nodes.append(TextNode(alt, TextType.IMAGE, url))

                current_text = parts[1]

            else:
                break

        if current_text.strip():
            new_nodes.append(TextNode(current_text, TextType.TEXT))

        result_nodes.extend(new_nodes)

    return result_nodes
