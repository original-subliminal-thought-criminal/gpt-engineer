from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
import zipfile
from gpt_engineer.main import chat

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the main prompt from the form
        project_name = request.form['project_name']
        main_prompt = request.form['main_prompt']


        #create directory for project
        os.mkdir(project_name)

        # gather full path to project_name
        project_path = os.path.join(os.getcwd(), project_name)

        # save main prompt into project folder
        with open(project_name + '/main_prompt', 'w') as f:
            f.write(main_prompt)
        
        chat(project_path, "", model='gpt-4', temperature=0.1, steps_config='default')
        
        # After generating files, zip them
        with zipfile.ZipFile(f'static/{project_name}.zip', 'w') as zipf:
            for root, dirs, files in os.walk(f"{project_name}/workspace"):
                for file in files:
                    zipf.write(os.path.join(root, file))
        
        return send_file(f'static/{project_name}.zip',
                         mimetype='zip',
                         attachment_filename=f'{project_name}.zip',
                         as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)