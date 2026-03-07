import { useCallback, useRef, useState } from "react";

import { endSession, sendMessage, startSession } from "@/api/client";
import type { Message } from "@/types";

export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [streaming, setStreaming] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const sessionIdRef = useRef<string | null>(null);

  const start = useCallback(async (personaId: string) => {
    setLoading(true);
    setError(null);
    try {
      const { session, opening_message } = await startSession(personaId);
      sessionIdRef.current = session.id;
      setMessages([{ role: "assistant", content: opening_message }]);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setLoading(false);
    }
  }, []);

  const send = useCallback(async (text: string) => {
    if (!sessionIdRef.current || streaming) return;

    setMessages((prev) => [...prev, { role: "user", content: text }]);
    setStreaming(true);

    // Add placeholder for assistant response
    setMessages((prev) => [...prev, { role: "assistant", content: "" }]);

    await sendMessage(
      sessionIdRef.current,
      text,
      (token) => {
        setMessages((prev) => {
          const updated = [...prev];
          const last = updated[updated.length - 1];
          if (last.role === "assistant") {
            updated[updated.length - 1] = {
              ...last,
              content: last.content + token,
            };
          }
          return updated;
        });
      },
      () => {
        setStreaming(false);
      },
      (err) => {
        setError(err);
        setStreaming(false);
      }
    );
  }, [streaming]);

  const end = useCallback(async () => {
    if (sessionIdRef.current) {
      await endSession(sessionIdRef.current);
      sessionIdRef.current = null;
    }
    setMessages([]);
    setStreaming(false);
  }, []);

  return { messages, streaming, loading, error, start, send, end };
}
