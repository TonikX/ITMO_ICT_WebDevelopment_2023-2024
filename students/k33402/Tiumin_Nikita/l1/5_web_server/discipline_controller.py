

class DisciplineController:

    def __init__(self):
        self.fake_db = {}
        self.last_id = 0

    def index(self, parameters):
        with open('C:\\Users\\tyumi\\Desktop\\web\\students\\k33402\\Tiumin_Nikita\\l1\\5_web_server\\index.html') as f:
            html = f.read()

        html_to_insert = ''

        for name in self.fake_db:
            html_to_insert += '<tr>'
            html_to_insert += '<td>' + name + '</td>'
            html_to_insert += '<td>'
            for grade in self.fake_db[name]:
                html_to_insert += grade + ', '
            html_to_insert = html_to_insert.strip(', ')
            html_to_insert += '</td>'

        html = html.replace('#content', html_to_insert)

        return {'type': 'html', 'code': 200, 'data': html}

    def store(self, data):
        if 'name' not in data or 'grade' not in data:
            return {'type': 'json', 'code': 422, 'data': {'error': 'name and grade are required'}}

        if data['name'] in self.fake_db:
            self.fake_db[self.escape(data['name'])].append(self.escape(data['grade']))
        else:
            self.fake_db[self.escape(data['name'])] = [self.escape(data['grade'])]
        print(self.fake_db)
        return {'type': 'json', 'code': 200, 'data': {'success': True}}

    def escape(self, string):
        return str(string).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
