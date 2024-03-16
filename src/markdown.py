block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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

def block_to_block_type(block: str):
    block = block.strip()
    # Check if ends match code block
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    # Check if header
    header_level = 0
    for char in block:
        if char == "#":
            header_level += 1
        else:
            break
    if header_level != 0:
        if header_level > 6:
            return block_type_paragraph
        return f"{block_type_heading}_{header_level}"

    # check if every line matches a pattern
    lines = block.splitlines()
    block_type =get_block_from_line_start(block, 1)

    for line_index in range(len(lines)):
        line = lines[line_index]
        if get_block_from_line_start(line, line_index + 1) != block_type:
            return block_type_paragraph
    return block_type

def get_block_from_line_start(line: str, line_num: int):
    if line.startswith(">"):
        return block_type_quote
    elif line.startswith("- ") or line.startswith("* "):
        return block_type_unordered_list
    elif line.startswith(f"{line_num}. "):
        return block_type_ordered_list
    else:
        return block_type_paragraph
