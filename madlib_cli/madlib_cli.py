def read_template(path):
    with open(path) as file:
        stripped_content = file.read().strip()

    return stripped_content


def parse_template(string_template):

    capturing = False
    dissected_string = ""
    parts = []
    current_speech_part = ""


    for char in string_template:
        if not capturing:
            dissected_string += char

            if char == "{":
                capturing = True

        else:
            if char == "}":
                capturing = False
                parts.append(current_speech_part)
                dissected_string += char
                current_speech_part = ""
            else:
                current_speech_part += char


def merge(bare_template, responses):

     return bare_template.format(*responses)