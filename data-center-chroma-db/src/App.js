import React, { useState } from 'react';
import './App.css';

function App() {
  const [pdfFiles, setPdfFiles] = useState([]);
  const [wordFiles, setWordFiles] = useState([]);
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);

  const handlePdfFileChange = (event) => {
    setPdfFiles(Array.from(event.target.files));
    setStatus(''); // Reset status on file change
  };

  const handleWordFileChange = (event) => {
    setWordFiles(Array.from(event.target.files));
    setStatus(''); // Reset status on file change
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    
    const totalFiles = pdfFiles.length + wordFiles.length;
    if (totalFiles === 0) {
      setStatus('Please select at least one PDF or Word file.');
      return;
    }

    setLoading(true);
    setStatus('');

    // Simulate file upload with a 1-2 second delay
    setTimeout(() => {
      let successMessage = '';
      if (pdfFiles.length > 0) {
        successMessage += `Added ${pdfFiles.length} PDF${pdfFiles.length > 1 ? 's' : ''}`;
      }
      if (wordFiles.length > 0) {
        if (pdfFiles.length > 0) successMessage += ' and ';
        successMessage += ` ${wordFiles.length} Word file${wordFiles.length > 1 ? 's' : ''}`;
      }
      successMessage += ' to TaxbaseBot AI Datacenter.';
      
      setStatus(`Success! ${successMessage}`);
      setPdfFiles([]); // Reset PDF files after success
      setWordFiles([]); // Reset Word files after success
      setLoading(false);
    }, 1500); // 1.5 seconds delay for simulated upload
  };

  const isUploadDisabled = loading || (pdfFiles.length === 0 && wordFiles.length === 0);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Document Upload to TaxbaseBot AI Datacenter</h1>
        <p>Upload your PDF and Word files to enhance the chatbot's knowledge base securely.</p>
        <p className="company-name">Powered by Sinewave Computer Services Pvt. Ltd.</p>
      </header>
      <main className="app-main">
        <div className="upload-card">
          <form onSubmit={handleSubmit} className="upload-form">
            {/* PDF Upload Section */}
            <div className="file-section">
              <h3 className="section-title">📄 PDF Files</h3>
              <label htmlFor="pdf-upload" className="file-label">
                <span>Select PDF Files</span>
              </label>
              <input
                id="pdf-upload"
                type="file"
                multiple
                accept=".pdf"
                onChange={handlePdfFileChange}
                className="file-input"
                disabled={loading}
              />
              <div className="selected-files">
                {pdfFiles.length > 0 && (
                  <p>Selected PDF files: {pdfFiles.map((file) => file.name).join(', ')}</p>
                )}
              </div>
            </div>

            {/* Word Upload Section */}
            <div className="file-section">
              <h3 className="section-title">📝 Word Files</h3>
              <label htmlFor="word-upload" className="file-label">
                <span>Select Word Files</span>
              </label>
              <input
                id="word-upload"
                type="file"
                multiple
                accept=".doc,.docx"
                onChange={handleWordFileChange}
                className="file-input"
                disabled={loading}
              />
              <div className="selected-files">
                {wordFiles.length > 0 && (
                  <p>Selected Word files: {wordFiles.map((file) => file.name).join(', ')}</p>
                )}
              </div>
            </div>

            <button 
              type="submit" 
              className="submit-button" 
              disabled={isUploadDisabled}
            >
              {loading ? 'Uploading...' : `Upload Documents (${pdfFiles.length + wordFiles.length})`}
            </button>
          </form>
          {status && (
            <p className={`status-message ${status.includes('Success') ? 'success' : 'error'}`}>
              {status}
            </p>
          )}
        </div>
      </main>
      <footer className="app-footer">
        <p>© 2025 Sinewave Computer Services Pvt. Ltd. | All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;