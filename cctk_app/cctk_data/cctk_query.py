def index_cchar_rule(file_path, phrase_file_path):
    
    data = {}
    with open(file_path) as f:
        for line in f:
            process_line(line, data)

    with open(phrase_file_path) as f:
        for line in f:
            process_line(line, data)

    return data

def process_line(line, data):
    
    line = line.decode('utf-8').strip()

    segs = line.split("\t")
    keys = [segs[0]]
    for c in segs[1].split():
        keys.append(c)

    keys = list(set(keys))

    try:
        explain = segs[2]
    except:
        explain = ""

    try:
        example = segs[3]
    except:
        example = ""

    for k in keys:
        data[k] = {'candidate': keys, 'example': example, 'explain': explain}    


    return data