import type { Persona, SessionStartResponse } from "@/types";

export async function fetchPersonas(): Promise<Persona[]> {
  const res = await fetch("/api/personas");
  if (!res.ok) throw new Error("Failed to fetch personas");
  return res.json();
}

export async function startSession(
  personaId: string
): Promise<SessionStartResponse> {
  const res = await fetch("/api/session/start", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ persona_id: personaId }),
  });
  if (!res.ok) throw new Error("Failed to start session");
  return res.json();
}

export async function endSession(sessionId: string): Promise<void> {
  await fetch(`/api/session/end/${sessionId}`, { method: "POST" });
}

export async function sendMessage(
  sessionId: string,
  message: string,
  onToken: (token: string) => void,
  onDone: () => void,
  onError: (error: string) => void
): Promise<void> {
  const res = await fetch(`/api/chat/${sessionId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  if (!res.ok || !res.body) {
    onError("Failed to send message");
    return;
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() ?? "";

    for (const line of lines) {
      if (line.startsWith("event: ")) {
        continue;
      }
      if (line.startsWith("data: ")) {
        const data = line.slice(6);
        // Look at the previous event type from the buffer context
        // We parse based on content
        try {
          const parsed = JSON.parse(data);
          if (typeof parsed === "string") {
            onToken(parsed);
          } else if (typeof parsed === "object" && Object.keys(parsed).length === 0) {
            onDone();
          }
        } catch {
          // skip unparseable lines
        }
      }
    }
  }
}
