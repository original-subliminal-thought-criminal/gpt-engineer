from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
import zipfile
from gpt_engineer.main import chat

app = Flask(__name__)

# Store user responses in a global dictionary
user_responses = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the project name and main prompt from the form
        project_name = request.form['project_name']
        main_prompt = request.form['main_prompt']

        # Create a directory for the project
        try:
            os.mkdir(project_name)
        except FileExistsError:
            pass        

        # Gather the full path to the project
        project_path = os.path.join(os.getcwd(), project_name)

        # Save the main prompt into the project folder
        with open(project_name + '/main_prompt', 'w') as f:
            f.write(main_prompt)

        # Store the user's main prompt response in the global dictionary
        user_responses[project_name] = main_prompt

        # Call the chat function and pass the project path and the Flask request object
        chat(project_path, "", model='gpt-4', temperature=0.1, steps_config='default', request=request)

        # After generating files, zip them
        with zipfile.ZipFile(f'static/{project_name}.zip', 'w') as zipf:
            for root, dirs, files in os.walk(f"{project_name}/workspace"):
                for file in files:
                    zipf.write(os.path.join(root, file))
        file_to_send = f"./static/{project_name}.zip"
        filename_to_send = f"{project_name}.zip"
        return send_file(file_to_send,
                         mimetype='zip',
                         as_attachment=True)

    # Get the project name if it exists in the query parameters
    project_name = request.args.get('project_name', '')

    # Get the user's previous response for the project (if available)
    previous_response = user_responses.get(project_name, '')

    return render_template('index.html', project_name=project_name, previous_response=previous_response)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
