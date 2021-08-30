def strip_newline(txt_content):
    new_content = []
    for content in txt_content:
        track_details = {}
        repl_content = content.replace("\n", "").split("-->")
        track_details["artist"] = repl_content[0]
        track_details["title"] = repl_content[1]
        new_content.append(track_details)
    return new_content


def handle_txt(path):
    try:
        tracklist = []
        with open(file=path, mode="r") as txt_file:
            repl_content = strip_newline(txt_content=txt_file.readlines())
            tracklist = repl_content
        return tracklist
    except:
        print("Not a Proper File")