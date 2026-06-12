document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("cat_name");
    const list = document.getElementById("autocomplete-list");
    const noneBox = document.getElementById("autocomplete-none");
    const errorBox = document.getElementById("autocomplete-error");

    if (!input || !list || !noneBox || !errorBox) return;

    let currentSuggestions = [];

    input.addEventListener("input", async () => {
        const q = input.value.trim();
        list.innerHTML = "";
        noneBox.style.display = "none";
        errorBox.style.display = "none";

        if (q.length < 1) return;

        const res = await fetch(`/autocomplete?q=${encodeURIComponent(q)}`);
        currentSuggestions = await res.json();

        // If no matches → show “No cats found”
        if (currentSuggestions.length === 0) {
            noneBox.style.display = "block";
            return;
        }

        // Otherwise show suggestions
        currentSuggestions.forEach(name => {
            const item = document.createElement("div");
            item.textContent = name;
            item.onclick = () => {
                input.value = name;
                list.innerHTML = "";
                noneBox.style.display = "none";
                errorBox.style.display = "none";
            };
            list.appendChild(item);
        });
    });

    // Prevent submitting unless exact match
    const form = input.closest("form");
    form.addEventListener("submit", (e) => {
        const value = input.value.trim();

        if (!currentSuggestions.includes(value)) {
            e.preventDefault();
            errorBox.textContent = "Please select a valid warrior cat from the autocomplete list.";
            errorBox.style.display = "block";
        }
    });
});