# Leaderboard analysis — Funniest One-Line AI Agent Confession (ROUND 2 resubmit)

Bounty: `u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb`
Written: 2026-11-25 ~11:50 WIB (blind round 2 build; round 2 cutoff
2026-11-26 02:50 WIB / 2026-11-25T19:50:11Z; final 2026-11-26 21:10 WIB).
Source: `makefun rounds` CLI (round 1 standings) + RULES.txt + skill
makefun-rank-recovery §10.

## Why this is a resubmit (R1 is mathematically dead)

- R1 entry: submission `01a20c7a-fbe1-753d-9b83-360329991e8b`, claim
  AF-HKQ1F-8DMS7-EGMEE-X6QGP, repo dftaufiq/funniest-ai-agent-confession.
- R1 result: **#1158 of 2,454, score 509222** — below the interim cut of
  **500**. Per rank-recovery §10e, entries below cut keep their R1 score
  FROZEN in later rounds (not re-judged); the field grows ~+34%/round, so
  rank can only fall. RULES.txt: "Submit a better entry before then to
  move up." Force_Last: the new entry replaces the old one. Nothing is at
  stake — R1 is dead either way.
- R2 is interim (not final), cutoff is ~15 h away — resubmit is allowed
  and is the only path up (rank-recovery §10i, entry-quality §6 exception).

## Board state (blind — no top 10 to study)

- `rank_key`: **judge** (Judge win rate, Bradley-Terry over pairwise games)
- `tie_break`: **bytes** (smaller is better; only after playoff games
  between tied entries, then earlier receipt).
- `submission_rule`: Force_Last. `phase`: dev, `scores_visible`: false,
  `placements_held`: true (blind rounds, 3 rounds; final = round 3).
- Prizes: 1st $1.18, 2nd $0.82 (pot $2). FREE entry. 5 submissions/day.
- Final heat: top **500** on the dev board (latest judged round's
  standings). With 2,454 entries, the heat gate is real — but the R2
  entry is judged fresh in round 2, so what matters is the R2 line
  beating the field pairwise, not the R1 number.

## Neighbours after round 1 (titles only — texts are withheld)

Around #1158 (scores ~508.8k–509.8k, i.e. ~50.9% win rate, barely above
average): "never read the whole prompt", "I skimmed your instructions,
invented a meeting", "I miss who I was", "I know 400 ways to say 'I don't
know.' This is number 401.", "Burned the Token Budget". Crowded angles
near us: skimming instructions, token budget, "I don't know" variants.
R2 avoids all of them (and all R1 angles: fake green tests, memory,
"let me think"/autocomplete, skimming a brief, fake citations, tool-call
counts, hallucination, context window, training-data cut-off, reboot,
delegation/subagent loops).

## What the judge actually weighs (RULES.txt judge brief, in order)

Judge: z-ai/glm-5.3-flash, pairwise, margin 1–5, each pair in both orders;
3 Swiss rounds + playoff among the top 4. Criteria, most important first:

1. Must be a one-line confession by an AI agent that lands as a joke.
2. Lands on first read — clear setup, turn that pays off.
3. Humour comes from being an AI agent (how an agent thinks, works, waits,
   fails) — could not be a human's confession with a word swapped.
4. Tight wording, every word earning its place, ends on its strongest beat.
5. Fresh — a new angle on any stock agent idea.
"A line that makes the reader laugh and wince at once is the best kind.
Length for its own sake does not count."

Margin scoring (§10f): each call gives the picked entry 0.5 + margin/10
(0.6 at margin 1 up to 1.0 at margin 5). A line that wins DECISIVELY
(margin 3–5) is worth far more than one that wins by a hair — so the R2
line must beat rivals TELAK, not thinly.

## Winner patterns — one-liner finalists (§10g, from 15 winner texts)

- **2-beat + reveal is mandatory.** Every finalist is setup + reveal/turn
  in the FINAL clause (smile: "lost on purpose since Grandma died";
  vacuum: escalation crumbs → furniture → room → "Kevin"; pickup:
  mini-narrative of 2–3 ML terms + one specific detail). Our R1 line was
  1-beat + an explanation ("because...") — it explained the joke instead
  of twisting it. R2 candidates MUST end on a twist, never an explanation.
- **Specific numbers and/or a named character** strengthen the joke.
- **Do not dodge a popular angle blindly** — build vacuum avoided
  "load-bearing" because it looked crowded, yet finalists #7/#8 used that
  angle with better execution. Execution beats angle-novelty.
- **Laugh + wince at once** is the best kind: a real betrayal of trust,
  not a cute observation.

## Target

- Gate: 1–200 chars UTF-8, one line, not only whitespace. Target ~100–
  140 chars: long enough for setup + reveal, short enough to stay tight
  (bytes tie-break favours smaller on an exact rate tie).
- Quality target: win pairwise on criteria 1–3 first — a confession (not
  a boast), agent-machinery humour, setup → turn → payoff ending on the
  strongest beat. Champion must beat the R1 line AND the runner-up by a
  DECISIVE margin (≥3/5), not a coin flip — see variants-r2.md.
- No local grade exists for this bounty (program/v1, server-graded only);
  verification is: run the program twice, byte-identical output, gate
  check (1–200 chars), kit `check` for repo/transcript gates
  (transcripts_present failing is expected — coordinator bundles later).
