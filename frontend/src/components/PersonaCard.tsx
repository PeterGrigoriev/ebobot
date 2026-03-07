import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import type { Persona } from "@/types";

interface Props {
  persona: Persona;
  onClick: () => void;
}

export function PersonaCard({ persona, onClick }: Props) {
  return (
    <Card
      className="cursor-pointer transition-shadow hover:shadow-lg active:scale-[0.98]"
      onClick={onClick}
    >
      <CardHeader>
        <CardTitle className="text-lg">{persona.name}</CardTitle>
        <CardDescription className="text-sm text-muted-foreground">
          {persona.source}
        </CardDescription>
        <p className="mt-2 text-xs text-muted-foreground">{persona.crisis_type}</p>
      </CardHeader>
    </Card>
  );
}
