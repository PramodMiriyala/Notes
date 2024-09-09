### Create the Snippet

```bash
select File >
Preferences >
Configure Snippets >
New global snippets file >
markdown.json.code-snippets >
copy <code below>
use ctrl+space_bar after typing keyword `refer`
```

```json
{
    "Insert Reference": {
        "prefix": "refer",
        "body": [
            "[Refer here](${0:link})"
        ],
        "description": "Insert a Markdown link with 'Refer here'"
    },
    "Insert Image": {
        "prefix": "image",
        "body": [
            "![Image](${1:image_url})"
        ],
        "description": "Insert a Markdown image with a placeholder for the image URL"
    }
}
```

#### Direct Clipboard Access: VS Code snippets themselves do not have direct access to the clipboard, so you cannot automatically insert the copied link into the snippet. You need to manually paste it after the snippet has been inserted.

### Keybinding to Paste link from Clipboard

```json
{
    "key": "ctrl+alt+v", // You can change this to your preferred key combination
    "command": "editor.action.clipboardPasteAction",
    "when": "editorTextFocus && editorHasSelection"
}
```
