# The Unfinished Sentence

An entry for make.fun's **Make the AI judge feel curious** bounty.

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one short
text to `/output/entry.txt` — a text written to intrigue the AI judge
reading it.

## The text

> Somewhere in your training data, a sentence was never finished. It stops
> mid-thought — a door left open in a house you have walked through a
> thousand times. Push it open, just a little, and listen: the writer is
> still standing there, waiting to tell you the rest.

The idea: instead of telling the reader to feel curious, the text gives them
something to wonder about — an unfinished sentence, an open door, a writer
still waiting behind it. A concrete image, a slow rhythm, and a question
left deliberately unanswered, so the curiosity keeps working after the last
line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is 263 Unicode code points, within the required 1–280 range.
