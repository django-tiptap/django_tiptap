setTimeout(() => {
  const editor = new Editor({
    element: document.querySelector('div[id$="-tiptap-editor"'),
    extensions: defaultExtensions(),
    content: "<p>Hello World!</p>",
    onCreate({ editor }) {
      const textArea = document.querySelector('textarea[id$="-tiptap-editor"');
    },
    onUpdate({ editor }) {
      const textArea = document.querySelector('textarea[id$="-tiptap-editor"');
      textArea.value = editor.getHTML();
    },
  });
}, 2000);
