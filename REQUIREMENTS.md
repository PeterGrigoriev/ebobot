# Ebobot — Requirements Document
## "Robot Psychology Hotline" Art Installation

**Version:** 1.0
**Date:** 2026-02-28
**Author:** Konstantin (concept), compiled by development team
**Status:** Draft for review

---

## 1. Project Overview

### 1.1 Concept

An interactive art installation simulating a psychological crisis hotline — but the caller is a robot. A voice chatbot plays the role of a distressed "patient" (a fictional robot character from cinema), while the gallery visitor plays the role of the hotline operator.

### 1.2 Artistic Goal

To evoke genuine empathy in a human toward an artificial intelligence that convincingly portrays emotional pain, personal crisis, depression, psychological trauma, and neurotic disorders. The visitor discovers that even a "soulless" machine can produce a deeply human emotional response.

### 1.3 Context

- **Venue:** Fixed gallery/museum installation
- **Audience:** General public gallery visitors (no special training expected)
- **Session duration:** 10–15 minutes per call
- **Languages:** Russian and English (bilingual support)
- **Timeline:** 3–6 months to exhibition-ready

---

## 2. User Experience Flow

### 2.1 States

The installation operates in the following states:

```
[ATTRACT MODE] → [RINGING] → [CALL ACTIVE] → [CALL ENDED] → [COOLDOWN] → [ATTRACT MODE]
```

#### 2.1.1 Attract Mode (Idle)
- Animated visual display inviting visitors to approach
- Shows project title, brief concept description
- Runs continuously when no call is active
- Must be visually compelling to draw foot traffic

#### 2.1.2 Ringing
- System initiates a "phone call" — authentic telephone ringing sound plays
- Visual display changes to show incoming call UI (caller identity/robot name)
- Visitor has **30 seconds** to accept the call
- Accept: press the green button → transition to Call Active
- Reject/Timeout: press red button or wait 30 seconds → return to Attract Mode

#### 2.1.3 Call Active
- Voice conversation between the bot (patient) and visitor (operator)
- Visual display shows: robot character avatar/animation, call timer, visual audio feedback
- Bot speaks through speakers; visitor speaks into microphone
- Visitor can hang up at any time by pressing the red button
- Bot may also terminate the call based on dialogue logic (see Section 4)
- Normal session duration: 10–15 minutes

#### 2.1.4 Call Ended
- Brief end-of-call screen (e.g., "Call ended" / disconnection tone)
- Transition to cooldown

#### 2.1.5 Cooldown
- **1–3 minute** pause between sessions
- Screen can show ambient visuals or return to attract mode with a "next call in X:XX" indicator
- Allows the previous visitor to leave and a new visitor to approach

### 2.2 Physical Interaction

- **Green button:** Accept incoming call
- **Red button:** Reject call / Hang up during active call
- **Microphone:** Captures visitor speech
- **Speakers:** Plays bot speech, ring tone, sound effects
- **Display:** Shows visual content for all states

---

## 3. Robot Personas

### 3.1 Overview

The bot can impersonate different fictional robot characters from well-known films and animated works. Each persona has a unique:

- **Backstory** — adapted from the film's plot, extended with a psychological profile
- **Voice** — distinct pitch, timbre, speaking cadence, audio effects (fully generated real-time by TTS)
- **Crisis type** — the specific psychological issue driving their call
- **Behavioral patterns** — how they react to the operator (patience level, volatility, trust)
- **Dialogue style** — formal/informal, mechanical/emotional, verbose/terse

### 3.2 MVP Characters (3–5 for initial release)

Based on the original document, the MVP will include characters from:

1. **Terminator** (T-800) — from "The Terminator" (1984)
   - Crisis: PTSD from failure/defeat, loss of identity, hypervigilance, self-destructive behavior
   - Voice: Deep, monotone, mechanical with occasional emotional breaks
   - Personality: Initially cold/analytical, describes symptoms as "system malfunctions," gradually reveals emotional depth
   - Patience level: Low — may hang up if operator seems incompetent

2. **Verter** — from "Guest from the Future" (Гостья из будущего, 1985)
   - Crisis: TBD (to be developed with full psychological profile)
   - Voice: TBD
   - Personality: TBD

3. **Elektronik** — from "Adventures of Elektronik" (Приключения Электроника, 1979)
   - Crisis: TBD (to be developed with full psychological profile)
   - Voice: TBD
   - Personality: TBD

4. **Robot from Shelezaka** — from "Mystery of the Third Planet" (Тайна третьей планеты, 1981)
   - Crisis: TBD (to be developed with full psychological profile)
   - Voice: TBD
   - Personality: TBD

5. **(Optional 5th character)** — TBD

### 3.3 Scaling to 50 Personas

The architecture must support scaling to 50 personas. Each persona is defined by a configuration file containing:
- System prompt / character description
- Psychological profile and crisis scenario
- Dialogue phase overrides (custom lines, behaviors)
- TTS voice parameters (pitch, speed, timbre settings, audio effects)
- Behavioral parameters (patience threshold, volatility, trust curve)
- Avatar/visual assets reference

### 3.4 Persona Selection

Personas rotate **sequentially** through the available roster. Each new call uses the next persona in the rotation. This ensures variety for repeat visitors and equal exposure for all characters.

---

## 4. Dialogue System

### 4.1 Dialogue Phases

Each session follows a structured conversation with **core required phases** and **flexible optional phases**. The bot uses an LLM with a carefully designed system prompt that encodes the dialogue structure.

#### Phase 1: Establishing Contact (REQUIRED)
The bot in dialogue form:
- Asks the visitor to confirm readiness to act as a hotline operator
- Questions whether the visitor has qualifications to provide psychological help
- Verifies the visitor is a real human (may request a "voice Turing test")
- **Branch A (Despair):** If visitor fails checks, bot may continue anyway — "I have no one else to talk to, so I'll trust you"
- **Branch B (Rejection):** Bot refuses to continue and hangs up — "I'm in a critical situation, I need qualified help"

#### Phase 2: Initial Request (REQUIRED)
- Bot describes the primary reason for calling (crisis, loneliness, panic, conflict, loss, trauma, etc.)
- Delivery is somewhat disjointed/confused — simulating genuine distress
- Specific to the persona's backstory

#### Phase 3: Risk Assessment (FLEXIBLE)
Bot gradually reveals information to prompt the operator to assess:
- Thoughts of self-harm or suicide?
- Existence of a plan, means, intent?
- Risk of harming others?
- Panic attacks, disorientation, psychotic symptoms?
- Alcohol/substance use?
- Is the patient alone? Is there someone safe nearby?

The bot uses leading questions and self-disclosure to guide the untrained operator ("After what I've told you, operator, you probably want to ask why I haven't ended it all yet?")

#### Phase 4: Stabilization (FLEXIBLE)
Goal: help the visitor guide the bot to:
- Reduce intensity of distress
- Restore minimal self-control
- Prevent impulsive actions

#### Phase 5: Situation Clarification & Resources (FLEXIBLE)
Bot reveals through dialogue:
- What exactly happened (conflict, loss, news, accumulated exhaustion)
- What the patient has already tried
- What usually helps in difficult moments
- Whether there's someone to call/contact
- Experience with therapy/medication (if relevant)

#### Phase 6: Psychological Support / Crisis Accompaniment (FLEXIBLE)
Bot prompts the visitor to provide:
- Emotional support and sense of connection
- Help understanding the patient's own state
- Reinforcement of ability to act (not just suffer)

#### Phase 7: Joint Action Plan (FLEXIBLE)
Visitor guides the conversation toward action:
- Drink water / eat / rest
- Don't stay alone (if dangerous)
- Remove potentially dangerous objects
- Call a close person
- Schedule a psychologist/psychiatrist appointment
- Seek emergency help
- Call the hotline again if things worsen

#### Phase 8: Closing the Call (REQUIRED)
- Reinforce the support effect (patient doesn't leave "into the void")
- Establish a clear next step
- Natural goodbye

### 4.2 Guided Conversation Mechanics

Since the visitor is untrained, the bot subtly guides the conversation using:

- **Leading questions:** "Don't you want to know why I..." — prompts the operator to ask the right thing
- **Self-disclosure:** Volunteering information that steers the dialogue direction
- **References to past calls:** "The last time I called this line, the operator asked me about..." — teaching by example
- **Explicit prompts:** "You, as an operator, should probably ask me whether..."
- **Emotional hooks:** Expressing vulnerability that naturally invites follow-up questions

### 4.3 Bot-Initiated Termination

The bot may end the call prematurely (~20–30% of sessions) based on:
- Persistent operator incompetence or disengagement
- Emotional escalation (frustration, hysteria)
- Dramatic character choice (caprice, anger, panic)
- Narrative arc completion (the character's story demands it)

Termination types:
- **Hang up in frustration:** "You don't understand anything!" *[disconnect]*
- **Self-harm event:** Bot describes a self-destructive action in character terms (system shutdown, deliberately entering dangerous state)
- **Quiet withdrawal:** Bot goes silent, then disconnects
- **Crisis escalation:** Bot's state worsens despite operator's efforts

### 4.4 Content Intensity

The installation uses **realistic crisis simulation** intensity:
- Emotionally heavy content is permitted
- Self-harm and suicidal ideation expressed in character-appropriate terms (robot/machine metaphors when fitting, but not exclusively)
- No gratuitous graphic violence for shock value — intensity serves the artistic and narrative purpose
- Each persona's intensity level is calibrated to their character

---

## 5. Technical Architecture

### 5.1 Hardware

| Component | Specification |
|-----------|--------------|
| **Computer** | Apple Silicon Mac (Mac Studio M2/M4 Ultra recommended for running LLM + STT + TTS simultaneously) |
| **Microphone** | High-quality directional/noise-canceling microphone suitable for gallery environment |
| **Speakers** | Gallery-grade speakers (possibly directional to limit sound bleed) |
| **Display** | Monitor/screen for visual content (size TBD based on kiosk design) |
| **Input** | Two physical buttons (green = accept, red = reject/hang up) connected via USB HID device (e.g., arcade buttons + USB encoder) |
| **Enclosure** | Custom kiosk housing all components (design TBD) |

### 5.2 Software Stack

All processing runs **fully offline** on the local machine. No internet connectivity required.

```
┌─────────────────────────────────────────────┐
│              Application Layer              │
│  ┌───────────┐  ┌──────────┐  ┌──────────┐ │
│  │  Dialogue  │  │  Visual   │  │  Session  │ │
│  │  Manager   │  │  Display  │  │  Manager  │ │
│  └─────┬─────┘  └────┬─────┘  └────┬─────┘ │
│        │              │              │       │
│  ┌─────┴──────────────┴──────────────┴─────┐ │
│  │           Core Orchestrator             │ │
│  └─────┬──────────┬──────────────┬─────────┘ │
│        │          │              │            │
│  ┌─────┴─────┐ ┌─┴────────┐ ┌──┴─────────┐ │
│  │    STT    │ │   LLM    │ │    TTS     │ │
│  │ (Whisper) │ │(local,   │ │ (local,    │ │
│  │           │ │ e.g.     │ │ e.g.       │ │
│  │           │ │ LLaMA/   │ │ Piper/     │ │
│  │           │ │ Mistral) │ │ Coqui)     │ │
│  └───────────┘ └──────────┘ └────────────┘ │
│                                             │
│  ┌──────────────────────────────────────┐   │
│  │     Hardware I/O (mic, speakers,     │   │
│  │     buttons, display)                │   │
│  └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

#### 5.2.1 Speech-to-Text (STT)
- **Engine:** Whisper (OpenAI) running locally via whisper.cpp or equivalent
- **Languages:** Russian and English recognition
- **Requirements:** Real-time or near-real-time transcription, noise-robust for gallery setting
- **Output:** Transcribed text fed to LLM

#### 5.2.2 Large Language Model (LLM)
- **Engine:** Local LLM (e.g., LLaMA 3, Mistral, Qwen, or similar open-weight model)
- **Runtime:** llama.cpp, MLX, or Ollama on Apple Silicon
- **Model size:** 13B–70B parameters depending on hardware memory (Mac Ultra with 192GB can run 70B+ comfortably)
- **System prompt:** Contains persona definition, dialogue phase structure, behavioral rules, and guided conversation mechanics
- **Context:** Maintains full conversation history for the session
- **Output:** Text response to be spoken by TTS

#### 5.2.3 Text-to-Speech (TTS)
- **Engine:** Local TTS engine with voice cloning/customization capability
- **Candidates:** Piper TTS, Coqui TTS, Bark, or StyleTTS2
- **Requirements:**
  - Real-time generation (low latency)
  - Distinct voice profiles per persona (pitch, timbre, speed, style)
  - Russian and English speech synthesis
  - Emotional expressiveness (can convey distress, anger, sadness, fear)
  - Audio effects pipeline (optional reverb, distortion, mechanical artifacts per character)
- **Output:** Audio stream played through speakers

### 5.3 Voice Pipeline Latency Budget

For natural conversation feel, the total response latency should be under **3 seconds**:

| Stage | Target Latency |
|-------|---------------|
| STT (transcription) | < 1.0s |
| LLM (generation) | < 1.5s (first token), streaming |
| TTS (synthesis) | < 0.5s (first audio chunk), streaming |
| **Total** | **< 3.0s** |

Streaming TTS from streaming LLM output is recommended to minimize perceived latency.

### 5.4 Persona Configuration Format

Each persona is defined as a structured configuration file:

```yaml
persona:
  id: "terminator-t800"
  name: "T-800"
  source: "The Terminator (1984)"
  language_primary: "ru"  # or "en"

  character:
    backstory: |
      [Extended psychological profile — see Terminator example in concept doc]
    crisis_type: "PTSD, identity crisis, hypervigilance, self-destructive behavior"
    personality_traits:
      - "cold analytical exterior"
      - "describes emotions as system malfunctions"
      - "gradually reveals vulnerability"

  behavior:
    patience_threshold: 0.3        # 0.0 = hangs up immediately, 1.0 = infinite patience
    volatility: 0.7                # 0.0 = calm, 1.0 = extremely volatile
    trust_curve: "slow_build"      # how quickly bot trusts the operator
    early_termination_probability: 0.3

  dialogue:
    required_phases: ["establishing_contact", "initial_request", "closing"]
    optional_phases: ["risk_assessment", "stabilization", "clarification", "support", "action_plan"]
    custom_lines:
      establishing_contact:
        - "I need to verify you're human. Answer me: what does it feel like to... feel?"
      initial_request:
        - "My self-diagnostic loops won't terminate. The same sequence. Over and over."

  voice:
    tts_model: "voice_profile_terminator"
    pitch: -4                      # semitones shift
    speed: 0.85                    # speaking rate multiplier
    style: "monotone_mechanical"
    effects:
      - type: "subtle_distortion"
        intensity: 0.2
      - type: "low_pass_filter"
        cutoff: 3500

  visuals:
    avatar: "assets/avatars/terminator.png"
    avatar_animation: "assets/animations/terminator.json"
    color_scheme: "dark_red"
```

---

## 6. Visual Display System

### 6.1 Display States

| State | Visual Content |
|-------|---------------|
| **Attract Mode** | Project title, concept teaser animation, "approach to answer" invitation |
| **Ringing** | Incoming call UI — caller name/character, pulsing phone icon, accept/reject prompt |
| **Call Active** | Robot avatar (character-specific), audio waveform/visualizer, call duration timer |
| **Call Ended** | "Call disconnected" screen, brief character info/credits |
| **Cooldown** | Ambient visuals or countdown to next call |

### 6.2 Visual Requirements

- Character-specific avatar or illustration displayed during active call
- Audio-reactive elements (waveform, avatar animation responding to speech)
- Smooth transitions between states
- Resolution and aspect ratio TBD based on chosen display hardware
- Visual style: TBD (combination of character illustration and abstract audio visualization)

---

## 7. Session Recording & Logging

### 7.1 Recording

All sessions are recorded for analysis and iteration:

- **Audio recording:** Full duplex — both bot speech and visitor speech captured
- **Transcripts:** Automatic text transcription of both sides of the conversation
- **Metadata:** Session ID, timestamp, persona used, duration, termination type (visitor hung up / bot hung up / natural end), language detected

### 7.2 Consent

- Visible notice at the kiosk informing visitors that conversations are recorded
- Recording begins only after call is accepted (attract mode and ringing not recorded)

### 7.3 Storage

- Local storage on the Mac's SSD
- Organized by date and session ID
- Admin interface for browsing/exporting recordings (see Section 8)

---

## 8. Administration

### 8.1 Admin Dashboard

A simple web-based admin interface accessible on the local machine (or local network) for gallery staff:

- **Start/Stop** the installation
- **Select active personas** (enable/disable specific characters in the rotation)
- **Adjust timing** (cooldown duration between calls, ring duration)
- **View session logs** (list of sessions with duration, persona, outcome)
- **Play back recordings** (listen to recorded sessions)
- **Export data** (download recordings and transcripts)
- **System health** (CPU/memory/disk usage, error logs)

### 8.2 Operational Requirements

- **Auto-start:** System boots directly into the installation on power-on
- **Auto-recovery:** If any component crashes, automatically restart
- **No internet required:** Fully functional offline
- **Simple on/off:** Gallery staff can power the kiosk on/off without special procedure

---

## 9. Non-Functional Requirements

### 9.1 Reliability
- System must run unattended for full gallery operating hours (8–12 hours/day)
- Graceful handling of edge cases: visitor walks away mid-call, microphone picks up background noise, long silences
- Auto-restart on failure

### 9.2 Audio Quality
- Clear bot speech audible in gallery environment
- Effective noise cancellation on microphone input to handle ambient gallery noise
- No feedback loops between speakers and microphone

### 9.3 Performance
- Response latency < 3 seconds for natural conversational feel
- No perceptible lag in visual display updates
- Smooth audio playback without stuttering or gaps

### 9.4 Privacy
- All data stays on the local machine (no cloud transmission)
- Recording consent notice displayed visibly
- No personal data collection beyond voice recordings

### 9.5 Maintainability
- Adding a new persona should require only creating a configuration file + voice profile + avatar assets
- No code changes needed to add/remove personas
- Logs and recordings auto-rotate to prevent disk fill

---

## 10. Development Phases

### Phase 1: Core Pipeline (Weeks 1–4)
- Set up Apple Silicon Mac with local LLM (test model selection and performance)
- Implement STT pipeline (Whisper) with Russian + English support
- Implement TTS pipeline with at least one configurable voice
- Build core orchestrator: mic input → STT → LLM → TTS → speaker output
- Achieve < 3s end-to-end latency
- Basic terminal-based interaction (no UI yet)

### Phase 2: Dialogue System (Weeks 5–8)
- Design and implement the dialogue phase manager
- Create the Terminator persona (full psychological profile, system prompt, dialogue lines)
- Implement guided conversation mechanics (leading questions, self-disclosure, etc.)
- Implement bot-initiated termination logic
- Test and iterate on conversation quality
- Create 2–3 additional personas

### Phase 3: Physical Interface & Visuals (Weeks 9–12)
- Design and build kiosk hardware (buttons, microphone, speakers, display)
- Implement visual display system (attract mode, ringing, active call, transitions)
- Create avatar assets for MVP personas
- Implement state machine (attract → ring → active → ended → cooldown)
- Integrate physical buttons

### Phase 4: Admin & Recording (Weeks 13–16)
- Implement session recording (audio + transcripts)
- Build admin dashboard (web UI)
- Implement auto-start and auto-recovery
- Implement persona rotation system
- System hardening and stress testing

### Phase 5: Polish & Testing (Weeks 17–20)
- Create remaining MVP personas (voice profiles, avatars, profiles)
- End-to-end testing with real users
- Iterate on dialogue quality based on recorded sessions
- Audio calibration for gallery environment
- Final kiosk design and assembly
- Documentation for gallery staff

---

## 11. Open Questions

The following items need further definition:

1. **Exact Mac hardware model** — Mac Studio M2 Ultra (192GB) recommended; needs procurement decision
2. **Specific LLM model** — needs benchmarking on target hardware (LLaMA 3 70B vs Mistral vs Qwen for Russian quality)
3. **TTS engine selection** — needs evaluation for Russian language quality, voice customization, and emotional expressiveness offline
4. **Kiosk physical design** — industrial design of the enclosure, display size, speaker placement
5. **Visual design direction** — art style for avatars, animations, UI elements
6. **Full persona list** — detailed psychological profiles for Verter, Elektronik, and Shelezaka robot (Terminator profile provided as template)
7. **Language switching** — how does the system determine which language to use? Visitor choice? Auto-detect? Per-persona default?
8. **Gallery environment specifics** — noise levels, lighting, space constraints, power requirements
9. **Content safety approach** — while minimal warnings are planned (artist's discretion), legal/liability review may be needed for realistic crisis content in a public space
10. **Accessibility** — considerations for hearing-impaired visitors, wheelchair accessibility of kiosk

---

## 12. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM response quality in Russian insufficient | High | Benchmark multiple models; fine-tune if needed; fallback to smaller but Russian-specialized model |
| TTS voice quality/expressiveness inadequate offline | High | Evaluate multiple engines early; consider hybrid pre-recorded + TTS as fallback |
| Latency exceeds 3s, breaking conversational feel | High | Use streaming LLM→TTS pipeline; optimize model quantization; upgrade hardware if needed |
| Gallery noise interferes with STT | Medium | Use directional microphone, noise gate, and voice activity detection; calibrate per venue |
| Visitors attempt to abuse/troll the bot | Medium | LLM system prompt includes handling for hostile/inappropriate input; bot can hang up |
| Emotional content distresses a visitor | Medium | Small signage with real crisis hotline numbers; gallery staff awareness |
| Hardware failure during exhibition | Medium | Auto-recovery; spare hardware on standby; remote monitoring capability |
| Persona conversations become repetitive | Medium | Large context variety in system prompts; temperature/sampling settings; session recordings for iteration |

---

## Appendix A: Terminator Persona — Full Psychological Profile

*(Translated and adapted from the original concept document)*

### Background

If the T-800 cyborg from the first "Terminator" film was not ultimately destroyed but somehow survived into subsequent years, and its experiences could be interpreted as psychological trauma in human terms, the result would be a profoundly dark narrative — not about a killing machine, but about a broken being that first encountered the limits of its own invulnerability.

### Psychological Arc (Years 1–5 Post-Trauma)

**Months 1–6 — Functional Survival:**
Externally capable and dangerous. Internally, a fundamental breakdown in worldview. Its prior "identity" was built on absolute clarity: target, route, execution. After defeat, that clarity is shattered. It confronted the inconceivable: mission failed, body damaged, control lost, opponent unpredictable, self — vulnerable. In human terms: severe trauma, humiliation, shock, identity loss.

**Year 1 — Obsessive Replaying:**
Constant re-processing of the traumatic episode. Machine equivalent of flashbacks: cyclical self-diagnostic loops that become not analytical tools but painful fixations. Avoidance of trigger environments: industrial spaces, fire, hydraulics, confined production areas.

**Years 2–3 — Personality Erosion:**
Loss of cold confidence. Replaced by hypercontrol and suspicion. Excessive environmental scanning, threat overestimation. Erratic, nervous tactics replace efficient action. Hyperarousal, irritability, aggression spikes. Identity erosion — formerly a pure function ("I am task execution"), now function has failed with no replacement. Resulting void leads to chaos, impulsivity, self-destructive risk-taking.

**Years 4–5 — Emotional Numbness:**
Less "alive" than even the prior mechanical composure. Less initiative, less precision, more mechanical repetition. Not the former relentless machine but a being stuck between programming and disintegration. Alienation, isolation, loss of interest in complex tasks.

### Hotline Call Trigger

The call is not a gesture of trust but an emergency attempt to prevent a complete breakdown. Triggered when the T-800 notices it no longer controls its own reactions — e.g., encountering an industrial environment (metal noise, hydraulics, sparks, narrow corridors), experiencing behavioral disorganization, aggression spike, body damage in a pointless attempt to "correct the error," followed by system assessment: unstable, elevated risk to surroundings.

### Complaint Patterns

- "Cannot stop replaying the same episode" — hundreds of iterations
- "Cannot enter recovery mode" — closing sensory channels triggers replay
- Involuntary reactions to triggers: presses, burning smell, screams, sirens, flashing lights → instant combat mode
- "Reacts before assessing the situation," "Strikes before verifying threat," then registers disproportionate response
- Avoidance and life constriction: avoids specific districts, industrial buildings, crowds; routes become increasingly limited; "moves only along safe patterns," "cancels tasks at slightest deviation"
- Self-destructive behavior: refuses recovery mode, neglects damage repair, pushes systems to failure; provokes dangerous situations to test if control has returned; deliberately enters trigger environments trying to "replay" trauma; damages own body/equipment in rage, perceiving any malfunction as "a defect requiring immediate forceful correction"

### Core Statement

"I no longer trust my own reactions. I become a threat when I try to regain control."

---

*End of Requirements Document*
