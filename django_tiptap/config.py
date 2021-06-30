from typing import Any, Dict

TIPTAP_DEFAULT_CONFIG = {
    "width": "500px",
    "height": "500px",
    "extensions": [
        "bold",
        "italic",
        "underline",
        "strikethrough",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "textAlign",
        "indent",
        "table",
        "bulletList",
        "orderedList",
        "typography",
        "clearFormat",
        "jinjaSyntaxHighlight",
    ],
    "placeholderText": "Begin typing here...",
    "unsavedChangesWarningText": None,
    "lang": "EN",
    "custom_extensions": [],
}

TIPTAP_DEFAULT_TOOLTIPS = {
    "EN": {
        "bold": "Bold | (ctrl / ⌘) + B",
        "italic": "Italic | (ctrl / ⌘) + I",
        "underline": "Underline | (ctrl / ⌘) + U",
        "strike": "Strikethrough | (ctrl / ⌘) + shift + X",
        "h1": "Header 1 | (ctrl + alt) / (⌘ + ⌥) + 1",
        "h2": "Header 2 | (ctrl + alt) / (⌘ + ⌥) + 2",
        "h3": "Header 3 | (ctrl + alt) / (⌘ + ⌥) + 3",
        "h4": "Header 4 | (ctrl + alt) / (⌘ + ⌥) + 4",
        "h5": "Header 5 | (ctrl + alt) / (⌘ + ⌥) + 5",
        "h6": "Header 6 | (ctrl + alt) / (⌘ + ⌥) + 6",
        "alignLeft": "Align Left | (ctrl + shift ⇧) / (⌘ + shift ⇧) + L",
        "alignCenter": "Align Center | (ctrl + shift ⇧) / (⌘ + shift ⇧) + E",
        "alignRight": "Align Right | (ctrl + shift ⇧) / (⌘ + shift ⇧) + R",
        "alignJustify": "Justify | (ctrl + shift ⇧) / (⌘ + shift ⇧) + J",
        "indent": "Indent (Tab ↹)",
        "outdent": "Outdent (shift ⇧ + Tab ↹)",
        "bulletList": "Bullet List | (ctrl + shift ⇧) / (⌘ + shift ⇧) + 8",
        "orderedList": "Numbered List | (ctrl + shift ⇧) / (⌘ + shift ⇧) + 7",
        "addTable": "Add Table",
        "deleteTable": "Delete Table",
        "addColumnBefore": "Add Column Before",
        "addColumnAfter": "Add Column After",
        "deleteColumn": "Delete Column",
        "addRowBefore": "Add Row Before",
        "addRowAfter": "Add Row After",
        "deleteRow": "Delete Row",
        "mergeCells": "Merge Cells",
        "splitCell": "Split Cell",
        "toggleHeaderColumn": "Toggle Header Column",
        "toggleHeaderRow": "Toggle Header Row",
        "toggleHeaderCell": "Toggle Header Cell",
        "clearFormat": "Clear Format",
        "jinjaHighlight": "Jinja Highlight",
    },
    "DE": {
        "bold": "Fett | (ctrl / ⌘) + B",
        "italic": "Kursiv | (ctrl / ⌘) + I",
        "underline": "Unterstrichen | (ctrl / ⌘) + U",
        "strike": "Durchstreichen | (ctrl / ⌘) + Umschalt + X",
        "h1": "Überschrift 1 | (ctrl + alt) / (⌘ + ⌥) + 1",
        "h2": "Überschrift 2 | (ctrl + alt) / (⌘ + ⌥) + 2",
        "h3": "Überschrift 3 | (ctrl + alt) / (⌘ + ⌥) + 3",
        "h4": "Überschrift 4 | (ctrl + alt) / (⌘ + ⌥) + 4",
        "h5": "Überschrift 5 | (ctrl + alt) / (⌘ + ⌥) + 5",
        "h6": "Überschrift 6 | (ctrl + alt) / (⌘ + ⌥) + 6",
        "alignLeft": "Linksbündig | (ctrl + Umschalt ⇧) / (⌘ + Umschalt ⇧) + L",
        "alignCenter": "Zentriert | (ctrl + Umschalt ⇧) / (⌘ + Umschalt ⇧) + E",
        "alignRight": "Rechtsbündig | (ctrl + Umschalt ⇧) / (⌘ + Umschalt ⇧) + R",
        "alignJustify": "Blocksatz | (ctrl + Umschalt ⇧) / (⌘ + Umschalt ⇧) + J",
        "indent": "Einrücken (Tab ↹)",
        "outdent": "Ausrücken (Umschalt ⇧ + Tab ↹)",
        "bulletList": "Aufzählungsliste | (ctrl + Umschalt ⇧) / (⌘ + Umschalt ⇧) + 8",
        "orderedList": "Nummerierte Liste | (ctrl + Umschalt ⇧) / (⌘ + Umschalt ⇧) + 7",
        "addTable": "Tabelle hinzufügen",
        "deleteTable": "Tabelle löschen",
        "addColumnBefore": "Spalte links einfügen",
        "addColumnAfter": "Spalte rechts einfügen",
        "deleteColumn": "Spalte löschen",
        "addRowBefore": "Zeile darüber einfügen",
        "addRowAfter": "Zeile darunter einfügen",
        "deleteRow": "Zeile löschen",
        "mergeCells": "Zellen zusammenführen",
        "splitCell": "Zelle aufteilen",
        "toggleHeaderColumn": "Kopfspalte ein/ausschalten",
        "toggleHeaderRow": "Kopfzeile ein/auschalten",
        "toggleHeaderCell": "Kopfzelle ein/auschalten",
        "clearFormat": "Formatierung entfernen",
        "jinjaHighlight": "Jinja Markierungen",
    },
}

TIPTAP_DEFAULT_TRANSLATIONS = {
    "EN": {"row": "Row", "column": "Column", "add": "Add"},
    "DE": {"row": "Zeile", "column": "Spalte", "add": "Hinzufügen"},
}


def getUpdatedContextForProperty(context: dict, property: str) -> Dict[str, Any]:
    ctx = context.copy()

    if property in ctx["widget"]["config"]:
        return ctx
    elif "lang" in ctx["widget"]["config"]:
        langs: list = ["EN", "DE"]
        givenLang: str = ctx["widget"]["config"].get("lang")

        if givenLang.upper() in langs:
            ctx["widget"]["config"][property] = TIPTAP_DEFAULT_TOOLTIPS.copy()[
                givenLang.upper()
            ]
        else:
            ctx["widget"]["config"][property] = TIPTAP_DEFAULT_TOOLTIPS.copy()["EN"]
            print(
                "\n *** The language given to django_tiptap was not found, "
                "using english as default. *** \n"
            )
    else:
        ctx["widget"]["config"][property] = TIPTAP_DEFAULT_TOOLTIPS.copy()["EN"]

    return ctx
