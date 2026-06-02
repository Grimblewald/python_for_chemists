# TODO
- [ ] Improve layout (low prio but needs doing before first real release)
   - [ ] Fix how admonition boxes break
   - [ ] Fix how admonition boxes float
- [ ] add quizes to the end of chapters to make use of new quiz tool
- [ ] check all admonitions still belong to correct categories
- [ ] make sure all concepts introduced are shown incorporated in a lab example presented in the same chapter as they were introduced
- [ ] Update to align older sections with proposed contribution values
- [ ] remove hardcoded python from text. Instead use python files that are inserted to text via \input.
- [ ] fix broken figures (e.g. some labels are floating outside of zone) hardly fit for the publicaiton figure readyness this book aims to demonstrate.

# Python and Computational Thinking: A Crash Course for Scientists

A comprehensive LaTeX book geared towards teaching Python programming to scientists with no prior programming experience. Examples focus on chemistry, but lessons translate well beyond the sciences.

## Accessing the PDF

Simply grab the PDF from the latest release on the github repository.

## Using the Quiz tool

This is in the process of being implemented, but will work by simply downloading the script and running it in your python environment. It doesn't require any special pckages, but will use hashing to check quiz answers in order to auto-mark, providing students with automatic feedback on their learning without providing the ability to use back of book style cheating.

## Building the PDF from source

### Prerequisites

You need a LaTeX distribution with the following packages:
- KOMA-Script (`scrbook` document class)
- `tcolorbox` with skins and breakable libraries
- Standard packages: `listings`, `hyperref`, `xcolor`, `geometry`, `amsmath`, `graphicx`, `booktabs`

**Recommended distributions:**
- **Windows:** TeX Live
- **macOS:** MacTeX (LLM recommendation, quick websearch supports but this point would benfit from verificaiton)
- **Linux:** TeX Live (`sudo apt install texlive-full` on Ubuntu/Debian)

### Build Commands
After cloning the repository:

**Simple build (run twice for table of contents):**
```bash
pdflatex main.tex
pdflatex main.tex
```

**Using latexmk (handles multiple passes automatically):**
```bash
latexmk -pdf main.tex
```
---

**Questions for contributors?** Check the repository issues or reach out. The goal is to make this the first stop in every scientists journey into learning to use python, and you are an integral part of this.

---

# Contributing

## Core Philosophy

This textbook aims to keep pace with modern Python programming while remaining faithful to several foundational ideals about how scientists should learn to code.

### Presentation & Pedagogy

This textbook presents Python through **authentic scientific problems**, not abstract exercises. Every concept is introduced with a "why"—what real research question does this solve?—before the "how." We move deliberately from foundations (setup, basics, control flow) through essential skills (functions, file I/O, error handling) to scientific computing libraries (NumPy, Pandas, Matplotlib), building up a coherent mental model at each step.

Code examples are currently anchored in chemistry, but physics and biology examples are equally welcome. As an example, when introducing object-oriented programming, we avoid abstract cataloging ("Encapsulation, Abstraction, Inheritance, Polymorphism"). Instead, readers need practical intuition for *how to use a class*, awareness of unintuitive behaviors that will bite them, and an honest appraisal that their understanding is surface-level. We equip them with essential skills, point them toward deeper learning, and move on.

### Scope: Trunk and Branches

This textbook is intentionally focused. It serves as the **trunk** of a tree—the foundational knowledge every scientist-programmer needs. Topics like neural networks in chemistry, molecular dynamics simulations, or advanced statistical modeling are better served as **branches**: supplementary handbooks and specialized texts that readers are well-equipped to navigate *after* mastering this core material.

We resist the temptation to be comprehensive. Instead, we ask: "Will a novice programmer need this to become productive in scientific Python?" If the answer is no, it belongs in a specialized branch, not here. This keeps the book focused, digestible, and genuinely teachable. Readers who climb the trunk first will find themselves in an entirely new landscape, able to explore whatever branches suit their research. We should trust in our readers ability to continue to self-develop.

### Didactic Approach

We teach **understanding over memorization**. Chapters include "Ponder" blocks that encourage readers to think critically about unexpected behaviors (like why `0.1 + 0.2 ≠ 0.3`), fostering the scientific habit of questioning results and independently investigating to fill knowledge gaps. We emphasize **defensive practices from the start**—error handling, testing, and reproducibility aren't afterthoughts but integral parts of good programming.

Importantly, we acknowledge the emotional and cognitive dimensions of learning: we normalize struggle, celebrate debugging as a path to insight, and reframe error messages as guides rather than indictments. We're honest that learning to program takes time, and that's not a personal failing—it's how your brain forms new mental models.

### Core Values for Contributors

Any contributions should maintain these principles:

1. **Relevance** — Wherever possible, connect concepts to real scientific workflows, not toy problems or contrived examples.
2. **Narrative clarity** — Explain *why* a practice matters before teaching *how* to implement it. Motivation comes first.
3. **Integrity** — Acknowledge limitations, edge cases, and performance trade-offs rather than glossing over them. Honesty builds trust.
4. **Accessibility** — Assume readers are domain experts in their science but novices in programming. Build appropriate scaffolding.
5. **Practicality** — Minimize or exclude coverage of topics not in direct service of building practical skills or preventing harm. Keep scope tight; resist feature creep.

Finally, remember that code is ultimately written for humans—your future self, collaborators, reviewers. Every addition should honor that principle. Code should be readily interpreted by novices with an grasp of English, who have read this book up to that point. If the prior chapters in the book to not make something clear, it is out of place.

### File Organization

```
python_for_scientists/
├── main.tex                # Master file - compile this
├── preamble.tex            # Packages, colors, styling, custom commands
├── frontmatter/
│   ├── titlepage.tex       # Book title page
│   ├── preface.tex         # Who this book is for
│   └── how_to_use.tex      # Reading guide and icon legend
├── chapters/
│   ├── chap00_setup.tex    # Installation, environments, IDEs
│   ├── chap01_basics.tex   # Variables, types, expressions
│   └── chap02_containers.tex # Lists, dicts, sets, tuples
│   └── chapXX_TOPIC.tex 	# Additional Topics
├── backmatter/             # (placeholder for appendices, index)
├── data/                   # (placeholder for example data files)
└── README.md               # This file
```

### Adding New Chapters

0. Consider if a new chapter is _really_ needed here, or if it might fit into a handbook better?
1. Create a new file in `chapters/` following the naming convention: `chapNN_topic.tex`
2. Use the standard chapter structure:
   ```latex
   % chapNN_topic.tex - Brief description
   % ============================================================================

   \chapter{Chapter Title}
   \label{chap:topic}

   Introduction paragraph...

   \section{First Section}
   \label{sec:first-section}

   Content...
   ```
3. Add the include in `main.tex`:
   ```latex
   \input{chapters/chapNN_topic}
   ```

### Custom Environments

The preamble defines several admonition boxes:

```latex
\begin{warning}
Alerts about common mistakes or pitfalls.
\end{warning}

\begin{tip}
Shortcuts and best practices.
\end{tip}

\begin{note}
Additional context or clarification.
\end{note}

\begin{osbox}
Differences between Windows, macOS, and Linux.
\end{osbox}

\begin{labexample}
Scientific/chemistry application examples.
\end{labexample}

\begin{ponder}
Reflection questions at end of sections.
\end{ponder}
```

### Code Listing Styles

Three styles are available:

```latex
% Python code (default)
\begin{lstlisting}
def example():
    return 42
\end{lstlisting}

% Shell/terminal commands
\begin{lstlisting}[style=shellstyle]
pip install numpy
\end{lstlisting}

% Output (no line numbers, lighter background)
\begin{lstlisting}[style=outputstyle]
Result: 42
\end{lstlisting}
```

Inline code commands:
- `\py{code}` - Python code inline
- `\shell{command}` - Shell commands inline
- `\var{name}` - Variable names
- `\filepath{path/to/file}` - File paths
- `\key{Enter}` - Keyboard keys
- `\menu{File > Save}` - Menu navigation

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author
Orignially authored by Frithjof Herb, with the intention of making it a first-stop resource for the borader chemistry community. Check out the [contributors page](https://github.com/Grimblewald/python_for_chemists/graphs/contributors?all=1) for a list of all who've helped make this book what it is today.

## Special Mentions
Some folks gave feedback early on in the writing process outside of github. These people also deserve a mention for keeping motivation going early on in the project's life.

**full list being compiled for V1 release along with prefered reference structure** but interim - thank you to:
- Olivia Dickinson for a thorough early review, making significant contributions to how approachable the document is

# Generative AI statment

Generative AI has been used throughout the production of this text, however everything is scruitinized by humans with the required domain expertise to do so. The post mortem in the closing remarks chapter gives insight into what this looks like.
