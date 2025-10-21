
# PlantUML Instructions - Editing the C4 Diagram

This file explains how to edit and render `hangman_architecture_diagram.puml`.

## Option A: VS Code (recommended)
1. Install the **PlantUML** extension and **PlantUML Preview** by jebbs.
2. Install **Graphviz** on your machine (required to render diagrams).
   - Ubuntu: `sudo apt install graphviz`
   - macOS (Homebrew): `brew install graphviz`
   - Windows: download installer from graphviz.org
3. Open `hangman_architecture_diagram.puml` in VS Code and use the PlantUML preview pane to render.
4. Edit, save, and export as PNG/SVG from the preview pane.

## Option B: PlantText.com (browser)
1. Go to https://www.planttext.com/
2. Paste the contents of `hangman_architecture_diagram.puml` into the editor.
3. Click **Refresh** to render the diagram, then export as PNG/SVG.

## Notes
- The `.puml` file includes inline comments to explain each component.
- If you want to use C4-PlantUML macros, you can replace the simple rectangles with the C4 include lines and notation. This file uses basic PlantUML to keep it simple for learners.
