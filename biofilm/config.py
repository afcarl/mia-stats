isolate_code = dict(zip(data['isolate'], data['isolate_coded']))
code_isolate = {v: k for k, v in isolate_code.items()}
macaque_isolate_order = [11, 46, 90, 13, 16, 85, 86, 100, 58, 91, 83, 124, 125, 128, 129]  # isolates ordered by macaque


macaque_isolate = dict(zip(data['macaque'], data['isolate']))
isolate_macaque = dict(zip(data['isolate'], data['macaque']))
isolate_macaque