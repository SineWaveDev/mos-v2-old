import React, { useState, useRef, useEffect } from 'react';
import './App.css';

function parseMarkdown(text) {
  // Simple markdown parsing for bold (**) and new lines (\n)
  return text
    .split('\n')
    .map((line, index) => {
      let processedLine = line;
      if (line.includes('**')) {
        processedLine = line.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      }
      return processedLine ? <p key={index} dangerouslySetInnerHTML={{ __html: processedLine }} /> : null;
    })
    .filter(Boolean);
}

function App() {
  const [messages, setMessages] = useState(() => {
    const savedMessages = localStorage.getItem('chatHistory');
    return savedMessages ? JSON.parse(savedMessages) : [];
  });
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [voiceOutputEnabled, setVoiceOutputEnabled] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const messagesEndRef = useRef(null);
  const recognitionRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
    localStorage.setItem('chatHistory', JSON.stringify(messages));
  }, [messages]);

  useEffect(() => {
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = false;
      recognitionRef.current.interimResults = false;
      recognitionRef.current.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        setInput(transcript);
        setIsListening(false);
      };
      recognitionRef.current.onend = () => setIsListening(false);
      recognitionRef.current.onerror = () => setIsListening(false);
    }
  }, []);

  const handleSend = async () => {
    if (input.trim() === '') return;

    const userMessage = { text: input, sender: 'user' };
    setMessages([...messages, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      console.log('Sending request to:', 'http://127.0.0.1:8000/api/ask/');
      console.log('Request body:', { bot_name: "Sinewave Chat Bot", question: input });
      const response = await fetch('http://127.0.0.1:8000/api/ask/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ bot_name: "Sinewave Chat Bot", question: input }),
      });

      console.log('Response status:', response.status);
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, ${errorText}`);
      }

      const data = await response.json();
      console.log('Response data:', data);
      const botMessage = { text: data.answer, sender: 'bot' };
      setMessages((prev) => [...prev, botMessage]);

      if (voiceOutputEnabled && 'speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(data.answer);
        speechSynthesis.speak(utterance);
      }
    } catch (error) {
      console.error('Fetch Error:', error);
      const errorMessage = { text: `Sorry, there was an error processing your request. Details: ${error.message}`, sender: 'bot' };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const toggleVoiceOutput = () => {
    setVoiceOutputEnabled(!voiceOutputEnabled);
  };

  const startListening = () => {
    if (recognitionRef.current && !isListening) {
      setIsListening(true);
      recognitionRef.current.start();
    }
  };

  const clearHistory = () => {
    setMessages([]);
    localStorage.removeItem('chatHistory');
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Sinewave Chat Bot</h1>
        <p>Sinewave Computer Services Pvt. Ltd.</p>
      </header>
      <div className="chat-container">
        <div className="sidebar">
          <button onClick={clearHistory}>Clear History</button>
          <button onClick={toggleVoiceOutput}>
            {voiceOutputEnabled ? 'Disable Voice' : 'Enable Voice'}
          </button>
        </div>
        <div className="main-content">
          <div className="messages">
            {messages.map((msg, index) => (
              <div key={index} className={`message ${msg.sender}`}>
                <div className="avatar">{msg.sender === 'user' ? 'You' : 'Bot'}</div>
                <div className="text">
                  {msg.sender === 'bot' ? parseMarkdown(msg.text) : msg.text}
                </div>
              </div>
            ))}
            {isLoading && <div className="message bot loading">Typing...</div>}
            <div ref={messagesEndRef} />
          </div>
          <div className="input-area">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your question or press mic to speak..."
              rows="1"
            />
            <button className="mic-button" onClick={startListening} disabled={isListening}>
              {isListening ? 'Listening...' : '🎤'}
            </button>
            <button onClick={handleSend} disabled={isLoading}>
              Send
            </button>
          </div>
        </div>
      </div>
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} Sinewave Computer Services Pvt. Ltd. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;