# PacketLab — Application + Transport Layer Visualizer

A teaching dashboard for Computer Networks Assignments 1 and 2. It has exactly two primary panels: an activity panel on the left and a synchronized protocol visualizer on the right. The right panel has Application Layer and Transport Layer tabs.

## Features

- **Browsing:** simulated DNS query/response and HTTP request/response.
- **Mail:** simulated SMTP greeting, EHLO, MAIL FROM, RCPT TO, DATA, message body, acceptance, QUIT and goodbye.
- **Streaming:** simulated HLS-style master playlist, rendition playlist and media segment requests, with play/pause and quality selector.
- **Transport view:** TCP three-way handshake, illustrative data-bearing segments with sequence/ACK numbers, advertised window, flags and length, and FIN/ACK teardown.
- Previous, Next, Pause/Resume and Replay controls; activity history; responsive layout.
- FastAPI serves the single-page UI and provides `/health` for deployment checks.

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000. Health endpoint: http://127.0.0.1:8000/health.

## Deploy (example: Render)

1. Push this folder to a GitHub repository.
2. In Render, create a **Web Service** connected to that repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Deploy, then open the generated HTTPS URL and test Browse, Mail, Stream and both layer tabs.

The generated preview in Chat is not a public deployment. A real public demo URL must be created through a hosting provider.

## GitHub quick start

```bash
git init
git add .
git commit -m "Build PacketLab protocol visualizer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

## Protocol accuracy notes and simulation boundaries

- DNS is represented as a query followed by a response. The example IP and TTL are illustrative.
- The HTTP messages use an HTTP/1.1 teaching example. For HTTPS, HTTP headers and content are normally protected by TLS; the dashboard explicitly labels the trace as illustrative.
- SMTP commands are application-layer messages carried over one TCP byte stream. TCP segment boundaries do not map one-to-one to SMTP commands.
- TCP SYN and FIN each consume one sequence number. The illustrative handshake uses client initial sequence number 1000 / server initial sequence number 7000 for browsing, then ACKs the SYNs at 1001 and 7001. Payload ACKs advance by the modeled payload length.
- This is a protocol simulator, not a packet capture. TCP data events may aggregate many real packets, and window sizes, payload lengths, endpoints, DNS results, and HTTP response data are teaching values. No real email is sent and no real video is streamed.
- The transport visualization currently models TCP. UDP/QUIC is not implemented in this version and can be added as an extension.

## Suggested demo script (2–4 minutes)

1. Browse to `https://example.com`, show DNS + HTTP, then switch to Transport Layer and step through SYN/SYN-ACK/ACK, data and teardown.
2. Compose the sample email, simulate sending, inspect SMTP and then its TCP stream.
3. Start streaming, change quality, show manifest and segments, then inspect TCP data flow.
4. Demonstrate Previous, Next, Pause/Resume and Replay.

## Submission reminders

- Add the final public GitHub repository and live deployment URLs to your Classroom submission.
- Save genuine AI prompts/chat exports/screenshots from the tools you actually used. Do not claim an AI model or tool was used unless it was.
- Add a reflection describing the actual bugs/corrections you observed while testing this implementation.
