# LaTeX Thesis Template

A comprehensive LaTeX thesis template designed for local development with easy migration to Overleaf.

## Prerequisites

### macOS Setup

1. **Install MacTeX** (full LaTeX distribution):
   ```bash
   brew install --cask mactex
   ```
   
2. **Install additional tools** (optional but recommended):
   ```bash
   brew install latexmk  # For continuous compilation
   ```

3. **Refresh PATH** after MacTeX installation:
   ```bash
   sudo /usr/libexec/path_helper -v
   # Or restart your terminal
   ```

### VS Code Setup (Recommended)

1. Install the **LaTeX Workshop** extension
2. The project includes pre-configured VS Code settings in `.vscode/settings.json`

## Project Structure

```
thesis-latex/
├── main.tex           # Main thesis file
├── references.bib     # Bibliography file
├── Makefile          # Build automation
├── .gitignore        # Git ignore rules
├── figures/          # Store images here
├── chapters/         # Individual chapter files (optional)
└── appendices/       # Appendix files (optional)
```

## Quick Start

### Method 1: Using Make (Recommended)

```bash
# Full compilation (includes bibliography)
make

# Quick compilation (no bibliography update)
make quick

# Continuous compilation (watches for changes)
make watch

# Clean auxiliary files
make clean
```

### Method 2: Manual Compilation

```bash
# Full compilation with bibliography
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Method 3: VS Code

1. Open the project in VS Code
2. Open `main.tex`
3. Use Cmd+Option+B (or Ctrl+Alt+B) to build
4. The PDF will open automatically

## Writing Your Thesis

1. **Edit the title page** in `main.tex`:
   - Update university name, department, your name, thesis title, etc.

2. **Add your content**:
   - Write directly in `main.tex`, or
   - Create separate files in `chapters/` and include them

3. **Add references** to `references.bib`:
   - Use tools like Zotero, Mendeley, or Google Scholar for BibTeX export

4. **Add figures** to the `figures/` directory:
   - Supported formats: PDF, PNG, JPG
   - Reference them with `\includegraphics{figures/filename}`

## Key Features

- **Modern thesis template** with proper formatting
- **Bibliography management** with BibTeX
- **Cross-references** for chapters, sections, figures, and tables
- **Code listings** with syntax highlighting
- **Automatic table of contents**, list of figures, and list of tables
- **Professional title page**

## Overleaf Migration

This template is fully compatible with Overleaf:

1. **Zip the entire project**:
   ```bash
   make clean  # Clean auxiliary files first
   zip -r thesis.zip . -x "*.git*" ".DS_Store"
   ```

2. **Upload to Overleaf**:
   - Create new project → Upload Project
   - Upload the zip file
   - Set `main.tex` as the main document

3. **Alternative: Git sync**:
   - Push to GitHub/GitLab
   - Import from Git in Overleaf

## Tips

- **Use version control**: Commit your changes regularly
- **Backup frequently**: Keep copies in multiple locations
- **Modular approach**: Split large chapters into separate files
- **Reference management**: Use a reference manager like Zotero
- **Figure quality**: Use vector graphics (PDF) when possible

## Troubleshooting

### Common Issues

1. **"pdflatex not found"**:
   - Make sure MacTeX is installed and PATH is updated
   - Try: `sudo /usr/libexec/path_helper -v`

2. **Bibliography not showing**:
   - Run the full compilation sequence (pdflatex → bibtex → pdflatex → pdflatex)
   - Check that citations exist in your text (e.g., `\cite{example2023}`)

3. **Figures not displaying**:
   - Check file paths and extensions
   - Ensure figures are in the `figures/` directory

### Getting Help

- LaTeX documentation: [LaTeX Project](https://www.latex-project.org/)
- TeX Stack Exchange: [tex.stackexchange.com](https://tex.stackexchange.com/)
- Overleaf documentation: [Overleaf Learn](https://www.overleaf.com/learn)

## License

This template is provided as-is for academic use. Modify as needed for your institution's requirements.