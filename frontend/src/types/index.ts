export interface Persona {
  id: string;
  name: string;
  source: string;
  language_primary: string;
  crisis_type: string;
}

export interface Message {
  role: "user" | "assistant";
  content: string;
}

export interface Session {
  id: string;
  persona_id: string;
  status: "active" | "ended";
  started_at: string;
  ended_at: string | null;
  duration_seconds: number | null;
  messages: Message[];
}

export interface SessionStartResponse {
  session: Session;
  opening_message: string;
}
