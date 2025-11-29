# Ascendancy: Seasonal Campaign System

Drawing inspiration from sources such as "Atomic Habits", "Objectives and Key Results", and "The 12 Week Year", The Ascendancy: Seasonal Campaign System provides tools for defining a clear Vision for your future, prioritizing your goals, and then acheiving success by working towards and completing attainable wins that are small enough to tackle but are aligned directly to your life's Vision.

## High-level domain structure
```
User
 └─ Vision                     ← “big‑picture” OKRs (free‑form)
      ├─ Objective (vision‑level)   (many)
      │     └─ KeyResult (vision‑level)   (many)
      └─ Outlook3Year               ← 3‑year prioritized list
            └─ OutlookItem           (links a Vision‑Objective/KeyResult to a 3‑yr slot)

Season (13‑week block)               ← tactical OKRs
 ├─ Objective (season‑level)          (many)
 │     └─ KeyResult (season‑level)   (many)
 └─ Week (7‑day slice)               (many per season)
        ├─ Habit                    (repeatable, daily)
        ├─ Task                     (can have subtasks)
        │     └─ SubTask
        └─ DayScore                 (score for that day’s work)

SeasonScore                           ← aggregate of its weeks
YearScore                             ← aggregate of the 4 seasons in a calendar year
```
