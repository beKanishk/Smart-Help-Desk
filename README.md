# Smart Help Desk 🛠️

A streamlined AI-powered customer support system that combines:

- ✅ **Spring Boot Backend** (User/Auth/Order services with MongoDB)
- ✅ **FastAPI Agent Layer** using **Agno** and **Gemini AI**
- ✅ **Session-Based AI Memory** (no persistent memory)
- ✅ **Secure JWT-based Authentication**

---

## 📦 Tech Stack

- **Backend:** Java, Spring Boot, Spring Security, MongoDB
- **AI Agent Layer:** Python, FastAPI, Agno, Gemini
- **Authentication:** JWT (Stateless)
- **Memory:** In-memory session memory per session_id
- **DevOps:** Railway, Vercel (optional deployment)

---

## 🚀 Features

- 🔐 JWT Login and Secure User APIs
- 📦 Order status, refund, and cancel endpoints
- 🤖 AI Agent (`support_team`) handles user queries intelligently
- 🔄 Calls backend tools: `get_user`, `get_last_order`, `cancel_order`, `issue_refund`
- 💬 Maintains conversation context **only during session**
- ⚡ Session memory auto-resets on server restart

---

## 🧠 AI Agent Memory

This project uses **session memory only** (no long-term memory):

- `session_id` keeps short-term conversation context
- Memory is lost if:
  - You change the session ID
  - The FastAPI server restarts
- ✅ Simple, safe, and avoids storing personal data

---

## 📂 Project Structure

```bash
Smart-Help-Desk/
├── backend-springboot/
│   ├── src/main/java/...       # Spring Boot user/order/auth services
│   └── application.properties  # MongoDB, JWT config
├── ai_backend/
│   ├── app.py                  # FastAPI app with support agent
│   ├── agents/
│   │   └── support_team.py     # Gemini agent definition
│   │   └── knowledge_agent.py
│   │   └── status_agent.py
│   ├── tools/
│   │   ├── order_tools.py      # cancel_order, issue_refund, etc.
│   │   └── user_tools.py       # get_user, get_last_order, etc.
│   └── auth_state.py           # Handles user_id from JWT

```
---

## Example Request:

POST /agent/respond  
{  
  "query": "I want to cancel my order",  
  "session_id": "1234-abcd"  
}  
# Header:  
Authorization: Bearer <JWT_TOKEN>  
