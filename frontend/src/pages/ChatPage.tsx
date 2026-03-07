import { useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { ChatInput } from "@/components/ChatInput";
import { ChatMessageList } from "@/components/ChatMessageList";
import { Button } from "@/components/ui/button";
import { useChat } from "@/hooks/useChat";

export function ChatPage() {
  const { personaId } = useParams<{ personaId: string }>();
  const navigate = useNavigate();
  const { messages, streaming, loading, error, start, send, end } = useChat();

  useEffect(() => {
    if (personaId) {
      start(personaId);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [personaId]);

  const handleEndCall = async () => {
    await end();
    navigate("/");
  };

  if (loading) {
    return (
      <div className="flex h-dvh items-center justify-center">
        <p className="text-muted-foreground">Connecting...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex h-dvh flex-col items-center justify-center gap-4">
        <p className="text-destructive">{error}</p>
        <Button variant="outline" onClick={() => navigate("/")}>
          Back
        </Button>
      </div>
    );
  }

  return (
    <div className="flex h-dvh flex-col bg-background">
      {/* Top bar */}
      <div className="flex items-center justify-between border-b px-4 py-3">
        <span className="text-sm font-medium">Incoming Call</span>
        <Button variant="destructive" size="sm" onClick={handleEndCall}>
          End Call
        </Button>
      </div>

      {/* Messages */}
      <ChatMessageList messages={messages} streaming={streaming} />

      {/* Input */}
      <ChatInput onSend={send} disabled={streaming} />
    </div>
  );
}
