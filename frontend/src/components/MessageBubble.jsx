import React from "react";
import "./MessageBubble.css";

function MessageBubble({ sender, text, resources = [] }) {
  const isUser = sender === "user";

  return (
    <div className={`message-row ${isUser ? "right" : "left"}`}>
      <div className={`bubble ${isUser ? "user-bubble" : "bot-bubble"}`}>
        <p>{text}</p>

        {}
        {resources.length > 0 && (
          <div style={{ marginTop: "12px" }}>
            {resources.map((res, idx) => (
              <div
                key={idx}
                style={{
                  background: "#fff",
                  border: "1px solid #ddd",
                  borderRadius: "8px",
                  padding: "12px",
                  marginTop: "10px",
                  boxShadow: "0 3px 8px rgba(0,0,0,0.08)",
                }}
              >
                <h4 style={{ margin: "0 0 6px 0", color: "#d35400" }}>
                  {res.title}
                </h4>

                <p style={{ margin: "0 0 10px 0", fontSize: "14px" }}>
                  {res.description}
                </p>

                {res.link && (
                  <a
                    href={res.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{
                      display: "inline-block",
                      padding: "6px 10px",
                      background: "#f46d24",
                      color: "white",
                      borderRadius: "6px",
                      textDecoration: "none",
                      fontSize: "13px",
                    }}
                  >
                    Open →
                  </a>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default MessageBubble;
