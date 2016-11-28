def file_index(s):
    if not s:
        return ''

    lines, map = s.split('\n'), {}
    for i, line in enumerate(lines):
        words = line.split()
        for word in words:
            word = word.lower()
            map[word] = map.get(word, [])
            map[word].append(i + 1)

    indexes = []
    for word in sorted(map.keys()):
        indexes.append(word + ' ' + ','.join([str(i) for i in map[word]]))
    return '\n'.join(indexes)


with open('sample-text.txt', 'r') as f:
    content = f.read()
    print file_index(content)
