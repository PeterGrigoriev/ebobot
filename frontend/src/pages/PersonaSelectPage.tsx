import { useNavigate } from "react-router-dom";

import { PersonaCard } from "@/components/PersonaCard";
import { usePersonas } from "@/hooks/usePersonas";

export function PersonaSelectPage() {
  const { personas, loading, error } = usePersonas();
  const navigate = useNavigate();

  if (loading) {
    return (
      <div className="flex h-dvh items-center justify-center">
        <p className="text-muted-foreground">Loading personas...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex h-dvh items-center justify-center">
        <p className="text-destructive">{error}</p>
      </div>
    );
  }

  return (
    <div className="min-h-dvh bg-background p-6">
      <div className="mx-auto max-w-md">
        <h1 className="mb-2 text-2xl font-bold">Robot Psychology Hotline</h1>
        <p className="mb-6 text-sm text-muted-foreground">
          Choose a caller to begin the session
        </p>
        <div className="grid gap-4">
          {personas.map((persona) => (
            <PersonaCard
              key={persona.id}
              persona={persona}
              onClick={() => navigate(`/chat/${persona.id}`)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
