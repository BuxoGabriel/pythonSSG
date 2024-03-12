def markdown_to_blocks(markdown: str):
    blocks = []
    block = ""
    new_line = False
    for char in markdown:
        if char == '\n':
            if new_line:
                if block != "":
                    blocks.append(block)
                    block = ""
                continue
            else:
                new_line = True
        else:
            new_line = False
        block += char
    if(block !=""):
        blocks.append(block)
    return blocks
