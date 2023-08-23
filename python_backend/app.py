from flask import Flask, request, jsonify, send_file, url_for
import process_file  # Your existing processing script
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/process_file', methods=['POST'])
def process_uploaded_file():
    try:
        # Get the file content from the API response
        uploaded_file_content = request.get_data(as_text=True)

         # Get the original file name from the form data
        original_filename = request.form['filename']
        
        # Process the file content and get the modified file name
        modified_file_name = process_file.process_tab_content(uploaded_file_content, original_filename)
        
        if modified_file_name:
            # Construct the download URL using url_for
            download_url = url_for('download_file', filename=modified_file_name, _external=True)
            print(download_url)
            return jsonify({'message': 'File processed successfully', 'download_url': download_url})
        else:
            return jsonify({'error': 'File processing failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        print('hello i am in download')
        # Construct the absolute path to the modified file
        modified_file_path = os.path.join(os.getcwd(), filename)
        
        # Send the file for download
        return send_file(modified_file_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
