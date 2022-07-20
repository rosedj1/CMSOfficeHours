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
| `Cmd D` | Select next instance of highlighted word. |
| `Cmd Shift L` | Select ALL instances of highlighted word. |
| `F12` | Go to the definition (of a function, class, etc.) |
| `Ctrl -` | Go back to previous cursor location. |
| `Cmd /`| Comment multiple highlighted lines. |
| `Cmd \`| Open a copy of your script/terminal to the side. |
| `Cmd Shift P` | Open Command Palette |
| `Cmd Shift \` | Find matching parenthesis, brace, etc. |
| `Cmd Shift O` "oh" | Search for symbols/methods/classes in a file (like `#` in a `.md`). |
| `Cmd K, Cmd S` | Search for keyboard shortcuts. |
| `Cmd K, Cmd I` | View a function docstring. |
| `Cmd K, Cmd 0` "zero" | Fold all functions. |
| `Cmd K, Cmd J` | Unfold all functions. |
| `Cmd Opt [` | Fold innermost region at cursor. |
| `Cmd Opt ]` | Unfold innermost region at cursor. |
| `Cmd K, Z` | Zen mode. Excellent for working on one piece of code. |
| `Cmd K, V` | Markdown preview to the side. |
| `Cmd Shift V` | Markdown preview. |

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

## Connecting to a Remote Host

If VSC keeps failing to connect, then open up the Command Palette
(`Cmd + Shift + P`) and type `Uninstall VS Code Server from Host`.
Then try reconnecting.

- If that doesn't work, then open up a terminal, manually `ssh` into the
remote server and try deleting the `~/.vscode-server` dir.
