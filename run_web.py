import os
import sanic

app = sanic.Sanic(__name__)

@app.route('/', methods=['GET'])
async def get_root(request):
    html = open('show.html', 'r', encoding='utf8').read()
    return sanic.response.html(html)

@app.route('/show', methods=['GET'])
async def get_show_page(request):
    html = open('show.html', 'r', encoding='utf8').read()
    return sanic.response.html(html)

@app.route('/exams', methods=['GET'])
async def get_questions(request):
    json_files = os.listdir('json')
    names = list(map(lambda x: x[:-5], json_files))
    return sanic.response.json(names)

@app.route('/exams/<title>', methods=['GET'])
async def get_question(request, title):
    json_file = f'json/{title}.json'
    print('getq', json_file)
    if os.path.isfile(json_file):
        content = open(json_file, 'r', encoding='utf8').read()
        return sanic.response.text(content, content_type='application/json')
    else:
        return sanic.response.text('', status=404)

app.run(host='0.0.0.0', port=8000)