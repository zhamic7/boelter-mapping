from flask import Flask, render_template, request
import boelterMap
import visual
app = Flask(__name__)

display_visualization = False

def generate_output_html(path):
    if (path is None):
        return ["Invalid room #. Make sure you enter a real room in Boelter, which will always be a 4-digit number between 1200 and 8800. You can also enter SEASCAFE, CONNECTIONLAB, ROOF, or SEL."]
    return path

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    global display_visualization 
    room = request.form['start']
    dest = request.form['dest']
    
    nodeStart = boelterMap.getRoom(room)
    nodeEnd = boelterMap.dest[dest]
    
    if (nodeStart is not None):
        display_visualization = True
        visual.createVisual(nodeStart,nodeEnd) # create visualization
        path = boelterMap.djikstra(nodeStart,nodeEnd,room,boelterMap.dest2[dest])
        output_html = generate_output_html(path)
    else:
        output_html = generate_output_html(None)
    return render_template('index.html', output_html=output_html, room_html=room, dest_html=dest,display_visualization=display_visualization)

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

