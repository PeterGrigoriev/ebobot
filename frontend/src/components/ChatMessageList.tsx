import { useEffect, useRef } from "react";

import { ChatBubble } from "@/components/ChatBubble";
import { TypingIndicator } from "@/components/TypingIndicator";
import { ScrollArea } from "@/components/ui/scroll-area";
import type { Message } from "@/types";

interface Props {
  messages: Message[];
  streaming: boolean;
}

export function ChatMessageList({ messages, streaming }: Props) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, streaming]);

  return (
    <ScrollArea className="flex-1">
      <div className="flex flex-col gap-3 p-4">
        {messages.map((msg, i) => (
          <ChatBubble key={i} message={msg} />
        ))}
        {streaming && messages[messages.length - 1]?.content === "" && (
          <TypingIndicator />
        )}
        <div ref={bottomRef} />
      </div>
    </ScrollArea>
  );
}
