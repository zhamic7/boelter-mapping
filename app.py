from flask import Flask, render_template, request
import boelterMap 
app = Flask(__name__)


''' ADD THIS TO ANOTHER FILE AND IMPORT THAT?
boelterMap = graph.Graph()
boelterMap.add ....
'''

def generate_output_html(path):
    return str(path)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():

    room = request.form['start']
    dest = request.form['dest']
    
    nodeStart = boelterMap.getRoom(room)
    nodeEnd = boelterMap.dest[dest]
    print(nodeStart,nodeEnd)
    path = boelterMap.djikstra(nodeStart,nodeEnd)

    output_html = generate_output_html(path)
    #if room is not None:
        #path = boelterMap.djikstra(room,dest)
        #printExit(path)
    #else:
        #ERROR: NOT A ROOM ROOM MUST BE A NUMBER
    return render_template('index.html', output_html=output_html)

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

