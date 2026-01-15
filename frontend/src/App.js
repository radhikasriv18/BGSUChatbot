import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import ChatWindow from "./components/ChatWindow";

function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const handleSend = async (text) => {
    // Add user message
    setMessages((prev) => [...prev, { sender: "user", text }]);
    setLoading(true);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/", {
        message: text,
      });

      const botReply = response.data.reply;
      const resources = response.data.resources || [];

      // Add bot reply
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: botReply,
          resources: resources, // IMPORTANT
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "⚠️ I’m having trouble connecting right now. Please try again.",
          resources: [],
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <ChatWindow messages={messages} onSend={handleSend} loading={loading} />
      <div ref={chatEndRef}></div>
    </div>
  );
}

export default App;
