const chatBox = document.getElementById("chat-box");
const form = document.getElementById("chat-form");
const input = document.getElementById("prompt");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const prompt = input.value.trim();
  if (!prompt) return;

  appendMessage("Kamu", prompt, "user");
  input.value = "";
  appendMessage("Axion v1", "🧠 Letmitingg...", "ai");

  try {
    const res = await fetch("/axion-v1/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    const data = await res.json();
    chatBox.lastChild.remove();

    if (data.response) appendMessage("Axion v1", data.response, "ai");
    else appendMessage("Axion v1", "⚠️ Tidak ada respon dari server.", "ai");

  } catch (err) {
    appendMessage("Axion v1", "❌ Error: " + err.message, "ai");
  }
});

function appendMessage(sender, text, cls) {
  const div = document.createElement("div");
  div.className = cls;
  div.innerHTML = `<b>${sender}:</b><br>${formatMarkdown(text)}`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function formatMarkdown(text) {
  return text
    .replace(/```([\s\S]*?)```/g, "<pre><code>$1</code></pre>")
    .replace(/`([^`]+)`/g, "<code>$1</code>");
}
