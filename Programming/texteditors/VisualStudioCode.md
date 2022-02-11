# Visual Studio Code

[Cheatsheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

## Neat Tricks

- Most windows are drag-and-dropable!
  - Example: Drag the terminal window into the left sidebar (say, below "Search").
  - You can go the other way too.
- Get the **Search Editor: Apply Changes** extension.
  - It allows you to make the same change across ALL files simultaneously.
- Hover over a function, class, etc. to see its docstring.
  - Hold `Cmd` while hovering to see even more info.
  - `Cmd click` while hovering to jump to that object.
- When creating a new file in the Explorer window, you can make subdirectories:
  - `new_dir/sub_dir/new_file.py`

## Useful Shortcuts for Mac

| **Shortcut** |  **Description** |
| --- | --- |
| `Cmd P` | Search for a file. |
| `F12` | Go to the definition (of a function, class, etc.) |
| `Ctrl -` | Go back to previous page. |
| `Cmd \`| Open a copy of your script/terminal to the side. |
| `Cmd Shift P` | Open Command Palette |
| `Cmd Shift \` | Find matching parenthesis, brace, etc. |
| `Cmd Shift O` "oh" | Search for symbols/methods/classes in a file (like `#` in a `.md`). |
| `Cmd K, Cmd S` | Search for keyboard shortcuts. |
| `Cmd K, Cmd I` | View a function docstring. |
| `Cmd K, Cmd 0` (zero) | Fold all functions. |
| `Cmd K, Cmd J` | Unfold all functions. |
| `Cmd Shift V` | Markdown preview. |
| `Cmd K, V` | Markdown preview to the side. |

## Editing multiple lines simultaneously

Multiple cursors:

- `Cmd D`: Simultaneously highlight another instance of highlighted text.
- `Cmd Shift L`: Select all occurrences of highlighted text.
- `Option click_with_mouse`: Drop additional cursors wherever you click.
- `Option Cmd up-arrow/down-arrow`: Make additional cursors above/below.

Box selection (MacOS):

- `Shift Option Cmd arrow-key`
- `Shift Option highlight`

## Highlighted Words

Some words in comments will be highlighted:

```python
# FIXME, NOTE, TODO, HACK, XXX.
```