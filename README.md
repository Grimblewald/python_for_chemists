# TODO
- [ ] cover einsum notation and numba for making pyrhon kogic fast (possibly both under numpy, or maybe do numba seperately?)
- [ ] improve installation instructions, things are ambiguous atm, make clearer conceptual splits and be clearer about when something is theory and when students should follow along with something. It should be clear when we are mentioning things that exist, which student's don't need to do right now (e.g. installing jupyter etc) vs what needs to be done to be ready for the next chapter (have a python interpreter of an appropriate version, 3.10+, installed). Perhaps I should add screenshots of what some things like REPL look like in the first chapter?
- [ ] Add more explanations for some things, e.g. in chap00_setup.tex under subsection "Activating the Environment" for the warning starting with "If you get an error about “execution policies” on Windows PowerShell, run this command first (as administrator):" I got this comment "I'm not sure what this means" with a line pointing at the word administrator. So perhaps we need explain it? or just recommend using regular command prompt instead?

# Python and Computational Thinking: A Crash Course for Scientists

A comprehensive LaTeX book teaching Python programming to scientists with no prior programming experience.

## Building the PDF

### Prerequisites

You need a LaTeX distribution with the following packages:
- KOMA-Script (`scrbook` document class)
- `tcolorbox` with skins and breakable libraries
- Standard packages: `listings`, `hyperref`, `xcolor`, `geometry`, `amsmath`, `graphicx`, `booktabs`

**Recommended distributions:**
- **Windows:** MiKTeX or TeX Live
- **macOS:** MacTeX
- **Linux:** TeX Live (`sudo apt install texlive-full` on Ubuntu/Debian)

### Build Commands

**Simple build (run twice for table of contents):**
```bash
pdflatex main.tex
pdflatex main.tex
```

**Using latexmk (handles multiple passes automatically):**
```bash
latexmk -pdf main.tex
```

**Clean auxiliary files:**
```bash
latexmk -c
```

## File Organization

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

## Adding New Chapters

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

## Custom Environments

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

## Code Listing Styles

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

Frithjof Herb
