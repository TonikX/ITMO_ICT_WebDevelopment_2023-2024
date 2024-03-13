def generate(table):
	tablecontents = []
	for disc, grades in table.items():
		grades_line = " ".join(grades)
		tablecontents.append(f"<tr><td>{disc}</td><td>{grades_line}</td></tr>")
	precontent = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <table>
    <thead>
      <tr>
        <th>Discipline</th>
        <th>Grade</th>
      </tr>
    </thead>
    <tbody>"""
	content = "\n".join(tablecontents)
	postcontent = """    </tbody>
  </table>
</body>
</html>"""
	page = "\n".join((precontent, content, postcontent))
	return page