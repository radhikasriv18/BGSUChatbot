import React from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

import "./ChatWindow.css";

function ChatWindow({ messages, onSend, loading }) {
  return (
    <div className="chat-container">
      {/* HEADER */}
      <div className="chat-header">
        <h2>BGSU Student Support Chatbot</h2>
        <p className="subtitle">Here to help you succeed 🧡</p>
      </div>

      {/* MESSAGES */}
      <div className="chat-body">
        {messages.map((msg, index) => (
          <MessageBubble
            key={index}
            sender={msg.sender}
            text={msg.text}
            resources={msg.resources}
          />
        ))}

        {loading && <MessageBubble sender="bot" text="Typing..." />}
      </div>

      {/* INPUT */}
      <ChatInput onSend={onSend} />
    </div>
  );
}

export default ChatWindow;
