# Basic wodkflow of the engine (Version 1)
  This is the worlflow of the word constructor engine (version 1):

1.  TAKE USER INPUT:
    user_input = input()
    Example:
    "M iS SI sS iP pI"

2.  CLEAN THE INPUT:
    Remove spaces and normalize case.
    mississippi

3.  BUILD INPUT CHARACTER FREQUENCY :
    Example:
    {
    m:1
    i:4
    s:4
    p:2
    }

1. User Input
     ↓
2. Clean Input
     ↓
3. Build Frequency Map
     ↓
4. Load Dictionary
     ↓
5. Loop Each Word
     ↓
6. Length Filter
     ↓
7. can_form()
     ↓
8. Store Valid Word
     ↓
9. Print Results