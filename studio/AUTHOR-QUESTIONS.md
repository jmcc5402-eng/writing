# The author's questions

The six things the author says on every chapter, in the author's own
shapes, pulled from thirty-five comments on ch 17–22 of campus 1.2
(`studio/agents/audits/2026-09-20-author-comment-study.md`). They are
asked of every scene BEFORE it is drafted — the brief answers them,
one line per scene, in a section THE AUTHOR'S READ — and again of the
draft by `author-proxy` before the panel reads it. The point is that
none of these is ever said on a PR again; a comment on a PR should be
taste the author has not said yet.

The brief's table has one row per scene of THE SCENES and six cells.
A cell is one line: what the page will carry, or "—" and why not.

| # | Token | The author's question, in the author's words | What the cell says |
|---|---|---|---|
| 1 | MORE | "We describe the mental side, the logical side — but we need to talk about the romance side, the ache she feels, the sheer physical reaction. We just have one line that her arm goes warm." | Where the feeling is in this scene and HOW MUCH: the body at any touch or proximity (count the beats — four or more at a key moment), the ache in any apart section, the confusion said plain in her own head. If the scene has no feeling beat, say so and why the matrix allows it. |
| 2 | WHO | "I can't tell if she's trying to help her son or get him back on the field. We aren't sure if they are good guys or bad guys. The end of 22 has Sonny; we need to remind who he is. Why does this football coach read a message board?" | Every named character in the scene: what they want, their pull (STAKES.md), whether the reader is told to like or hate them now, the who-is-this clause if they have been away, the why for any habit shown. |
| 3 | CONFUSING | "It's confusing exactly when Dan comes to pick them up. It keeps saying 'he' — at one point it talks about Ty also. I have no idea if it's snowing or sleeting. Is 'the copies' the letter?" | The clock into and out of the scene (where each person is, how long, how the next one knew); every referent a reader who skipped a week needs; names not "he" where two men share a paragraph; what is falling. |
| 4 | NOSE | "Now we're being too on the nose. Better to have him pull the beer out and nothing be said about it. 'I wanted to say it in this truck' — remove that concept from the writing." | Any place the scene is tempted to explain its own device — a drink, a place, a callback, a rule — and the plainer thing the page does instead. |
| 5 | POINT | "The conversations on the porch are flat. I don't know what the point is. We are making a bigger deal out of a letter that isn't a big deal. How can we raise the stakes of this meeting?" | What the scene is for in one line; what is at stake in it for every person in the room (the sheet); whether the thing the scene treats as big is big, and what the page says if it is small. |
| 6 | SENSES | "Let's spend a little bit of time describing the storm. Let's have a paragraph at least. The dinner looser — the wine, the jar." | What the world is doing in this scene as a physical thing — the weather, the room, the props, the sound — and where its paragraph goes. |

## The rule

- A brief for ch 23 on carries THE AUTHOR'S READ; `brief-gate.py`
  refuses a drafter on a brief without it, or with a scene of THE
  SCENES missing from the table (L056).
- `author-proxy` reads the draft with these six questions and the
  author's comments verbatim, before the panel, and ends with a
  TESTS line of the six tokens; `accept-gate.sh` requires its file
  from ch 23 (L057).
- A real author comment on a PR is afterwards classed against this
  list: a repeat of a shape here is a MISS against the proxy or the
  brief and gets a ledger row; a new shape is the author adding taste
  and joins this table.
