import React, { useState } from "react";
import { IoSend } from "react-icons/io5";
import "./ChatInput.css";

function ChatInput({ onSend }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  return (
    <div className="chat-input-bar">
      <input
        className="chat-input"
        placeholder="Type your message..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />
      <button className="send-btn" onClick={handleSend}>
        <IoSend size={22} />
      </button>
    </div>
  );
}

export default ChatInput;
