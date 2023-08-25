import React, { useState } from 'react';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import './App.css';

function App() {
  const [downloadLink, setDownloadLink] = useState('');
  const [newConvert, setNewConvert] = useState(false);

  // Function to trigger the file processing
  const processFile = async (file) => {
    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('filename', file.name);
      console.log('FormDate:', JSON.stringify(formData));

      const response = await fetch('https://katz-tab-converter-python-backend.onrender.com/api/process_file', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const jsonResponse = await response.json();
        console.log('JSON Response:', jsonResponse);
        const downloadUrl = jsonResponse.download_url;
        console.log('Modified File Name:', downloadUrl);
        setDownloadLink(downloadUrl);
        console.log(downloadLink, 'hehe')
      } else {
        console.error('File processing failed');
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  };

  // Function to trigger the file download
  const downloadFile = async (downloadUrl) => {
    try {
        console.log('print I am about to perform get request')
        window.open(downloadUrl, '_self');
        setNewConvert(true);
    } catch (error) {
        console.error('An error occurred:', error);
    }
};

  // Function to trigger the file download
  const newConvertTrigger = async () => {
    try {
        console.log('new convert button')
        window.location.reload();
    } catch (error) {
        console.error('An error occurred:', error);
    }
};

  return (
    <div className="App">
      <header className="App-header">
        <Typography variant="h4">Katz Electronic Conversion App</Typography>
        <Typography style={{ paddingTop: '10px', paddingBottom: '10px' }} variant="body1">
            Upload the KatzLaw Aderant export file (.TAB file).
        </Typography>
        <Typography style={{ paddingTop: '10px', paddingBottom: '30px' }} variant="body2">
            Please Note: A download button will appear once the conversion is finished.
        </Typography>
      {/* Upload file input */}
      <input type="file" accept=".tab" onChange={(e) => processFile(e.target.files[0])} />
      
      {/* Trigger the download */}
      {downloadLink && (
        <Button style={{ marginTop: '30px', marginBottom: '10px' }} variant="contained" onClick={() => downloadFile(downloadLink)}>
          Download Processed File
        </Button>
      )}
      {newConvert && (
        <Button style={{ marginTop: '10px', marginBottom: '10px' }} variant="contained"onClick={() => newConvertTrigger()}>
          Convert a New File
        </Button>
      )}
      </header>
    </div>
  );
}

export default App;
