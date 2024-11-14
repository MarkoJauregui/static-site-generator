import re


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    # We need to find all matches in the text using this pattern
    matches = re.findall(pattern, text)

    # matches will now contain tuples of (alt_text, url)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    matches = re.findall(pattern, text)

    return matches
