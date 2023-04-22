from flask import Flask, render_template, request
import boelterMap 
app = Flask(__name__)


''' ADD THIS TO ANOTHER FILE AND IMPORT THAT?
boelterMap = graph.Graph()
boelterMap.add ....
'''

def generate_output_html(name,dest):
    return 'Hello, ' + name + ' you like ' + dest + '.'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():

    room = request.form['name']
    dest = request.form['color']
    output_html = generate_output_html(room,dest)
    #if (room in boelterMap.rooms):
        #path = boelterMap.djikstra(room,dest)
        #printExit(path)
    #else:
        #ERROR: NOT A ROOM ROOM MUST BE A NUMBER
    return render_template('index.html', output_html=output_html)
    return f"Hello {room} you like {dest}"

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

