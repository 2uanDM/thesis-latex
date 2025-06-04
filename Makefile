# Makefile for LaTeX thesis compilation

# Main file name (without .tex extension)
MAIN = main

# LaTeX compiler
LATEX = pdflatex
BIBTEX = bibtex

# Output directory
BUILD_DIR = build

# Default target
all: $(MAIN).pdf

# Compile the main document
$(MAIN).pdf: $(MAIN).tex reference.bib
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

# Quick compile (no bibliography update)
quick:
	$(LATEX) $(MAIN).tex

# Clean auxiliary files
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz

# Clean everything including PDF
distclean: clean
	rm -f $(MAIN).pdf

# Continuous compilation (requires latexmk)
watch:
	latexmk -pvc -pdf $(MAIN).tex

# Install latexmk if not available
install-latexmk:
	brew install latexmk

.PHONY: all quick clean distclean watch install-latexmk 