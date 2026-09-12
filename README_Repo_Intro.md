# 🛠️ Python Meets the Shop Floor
[![Open In Colab](https://google.com)](https://google.com)



A few lines of Python, and six evenly spaced holes appear around a circle, exactly where you told them to go. A chart that updates itself as sensor readings come in, quietly flagging the one reading that doesn't look like the others. A machine that keeps its own history, checks its own tolerances, and notices a tool wearing down before anyone standing at it would.

This repository is a collection of small, real examples like that — the kind of thing that sits right at the overlap of running a machine and writing code, which honestly doesn't get taught together very often. If you've ever stood at a machine and wondered what code could actually do for you, or written code and never had a reason to think about a spindle, there might be something here worth poking at.

Every notebook was run and checked before it went up here, so if something doesn't work on your machine, that's worth a closer look — not something to shrug off as normal. Clone it, open a notebook, run a cell, and see what happens.

## 👀 What's Actually in Here

Chapter by chapter, this repo builds from a single `print()` statement all the way to a working sensor-monitoring pipeline with real anomaly detection — covering G-code generation, live toolpath visualization, automated quality control, a Raspberry Pi sensor hub, and a genuinely honest look at when machine learning is (and very much isn't) the right tool for the job. Every notebook is self-contained and organized by chapter, so you can jump in wherever your curiosity actually is.

Each chapter here has a matching chapter in **[Book Title — Coming Soon]**, which walks through the reasoning behind the code — the why, not just the what. More on that further down, but wanted to mention it early in case that's exactly what you're looking for.

## 🚀 Running This — No Experience Required

You don't need to have ever run a line of code before. Pick whichever of these feels easier:

### Option 1: Just Open It in Your Browser (Fastest)

1. Go to **[colab.research.google.com](https://colab.research.google.com)**.
2. Click **File → Upload Notebook**, and select any `.ipynb` file from this repository.
3. Click the little **▶ play button** next to the first block of code. Watch it run, see the output appear right underneath.
4. Keep going, one block at a time, top to bottom.

That's genuinely it. Nothing to install, nothing to configure. If you've never coded before, start here.

### Option 2: Run It Locally With VS Code

A little more setup, but worth it once you're hooked and want everything running on your own machine:

1. **Install Python** — [python.org/downloads](https://python.org/downloads). On Windows, check **"Add Python to PATH"** during install.
2. **Install VS Code** — [code.visualstudio.com](https://code.visualstudio.com), free.
3. Open VS Code, click the **Extensions** icon (four little squares in the sidebar), and install **Python** and **Jupyter** (both by Microsoft).
4. **Download this repository** — click the green **Code** button above → **Download ZIP**, then unzip it. (Comfortable with Git? `git clone` works too.)
5. In VS Code, **File → Open Folder**, and select the unzipped folder.
6. Click any `.ipynb` file in the sidebar. VS Code opens it as a notebook — click the **▶** beside any cell to run just that piece and see what it does.

Either path gets you to the exact same place: real code, actually running, with real output you can see and change.

## 📖 Want the Full Story Behind the Code?

This repo shows you *what* to run. It won't tell you *why* it works, what mistakes to watch out for, or how a bolt-circle generator in Chapter 5 quietly becomes the foundation for a sensor-driven anomaly detector eight chapters later. That part lives in the book this repo was written to accompany — **[Book Title — Coming Soon]** — where every one of these examples is explained, tested, and built up one honest step at a time, from someone who'd rather show you a real 76% accuracy number than pretend a demo is perfect.

If this repo made you curious, the book is where that curiosity turns into real, lasting understanding. Consider it the missing manual to everything you just cloned.

## 🤝 Found a Bug? Made It Better?

Issues and pull requests are genuinely welcome — if you spot something broken, or you've adapted a notebook for your own machine in a way others might find useful, open a PR. This project is meant to grow with the people using it.

---

*Clone it. Run it. Break it on purpose. That's the whole point.*
