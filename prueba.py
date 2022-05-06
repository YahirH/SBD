from terminaltables import AsciiTable

data = []
data.append(['Row one column one', 'Row one column two'])
data.append(['Row two column one', 'Row two column two'])
data.append(['Row three column one', 'Row three column two'])

table = AsciiTable(data)

print(table.table)