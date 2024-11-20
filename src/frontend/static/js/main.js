html = String.raw;

async function select_file() {
    result = await pywebview.api.system.select_file();
    if (!result) return;

    const fileDisplay = document.getElementById("file-selector-display");
    const fileBtn = document.getElementById("file-selector-btn");

    fileDisplay.textContent = result;
    fileBtn.textContent = "ARQUIVO SELECIONADO";
}
