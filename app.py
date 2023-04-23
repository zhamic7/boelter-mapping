from flask import Flask, render_template, request
import boelterMap 
import visual
import os
import time
app = Flask(__name__)

display_visualization = False

def generate_output_html(path):
    if (path is None):
        return ["Invalid room #. Make sure you enter a real room in Boelter, which will always be a 4-digit number between 1200 and 8800. You can also enter SEASCAFE, CONNECTIONLAB, ROOF, or SEL."]
    return path

@app.route('/')
def hello_world():
    global display_visualization
    display_visualization = False
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    global display_visualization
    display_visualization = False

    room = request.form['start']
    dest = request.form['dest']
    
    nodeStart = boelterMap.getRoom(room)
    nodeEnd = boelterMap.dest[dest]
    timestamp = int(time.time() * 1000)
    if (nodeStart is not None):
        print(os.listdir('templates'))
        visual.createVisual(nodeStart,nodeEnd) # create visualization
        display_visualization = True
        path = boelterMap.djikstra(nodeStart,nodeEnd,room,boelterMap.dest2[dest])
        output_html = generate_output_html(path)
    else:
        output_html = generate_output_html(None)
    return render_template('index.html', output_html=output_html, room_html=room, dest_html=dest, display_visualization=display_visualization,timestamp=timestamp)

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')

@app.get('/templates/d3graph.html')
def show_graph():
    return render_template('d3graph.html')

if __name__ == '__main__':
    app.run(debug=True)

