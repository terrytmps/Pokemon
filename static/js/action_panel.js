let tooltipTimeout;
const boutonsAttaque = document.querySelectorAll('.bouton-attaque');


function startTooltip(button) {
    tooltipTimeout = setTimeout(() => {
        const tooltip = document.getElementById("move-tooltip");

        // Set the tooltip content
        tooltip.innerHTML = `
                <strong>${button.dataset.name}</strong> <br>
                <span>Type: ${button.dataset.type}</span> <br>
                ⚡ <b>Power:</b> ${button.dataset.power} <br>
                🎯 <b>Accuracy:</b> ${button.dataset.accuracy}% <br>
                <em>${button.dataset.description}</em>
            `;

        // Position the tooltip in the center of the screen
        tooltip.style.position = "fixed";
        tooltip.style.left = "50%";
        tooltip.style.top = "50%";
        tooltip.style.transform = "translate(-50%, -50%)"; // Center the tooltip

        // Make sure the tooltip is visible
        tooltip.style.display = "block"; // Show the tooltip
        tooltip.style.opacity = "1"; // Ensure opacity is set to 1 (fully visible)
        tooltip.style.transition = "opacity 0.3s ease-in-out"; // Smooth transition

        // Optional animation for fade-in effect
        tooltip.style.animation = "fadeIn 0.2s ease-in-out";
    }, 1000); // Wait 1 second before showing the tooltip
}

function hideTooltip() {
    clearTimeout(tooltipTimeout); // Clear the timeout if mouse leaves before 1 second
    const tooltip = document.getElementById("move-tooltip");
    tooltip.style.display = "none"; // Hide the tooltip
    tooltip.style.opacity = "0"; // Set opacity to 0 to hide
}

function lancerAttaque(index, pokemonName, moveName) {
    hideTooltip();
    attackPokemon(index)
}

function attaquePlayer() {
    const joueur = document.getElementById('pokemon-joueur');
    const adversaire = document.getElementById('pokemon-adversaire');

    // Animation du Pokémon du joueur
    joueur.classList.add('attaque');
    // Retirer l'animation après son exécution
    joueur.addEventListener('animationend', () => {
        joueur.classList.remove('attaque');
    });

    // Animation du Pokémon adversaire avec un léger délai
    setTimeout(() => {
        adversaire.classList.add('degats');
    }, 250);

    // Retirer l'animation après son exécution
    adversaire.addEventListener('animationend', () => {
        adversaire.classList.remove('degats');
    });
}

function attaqueAdversaire() {
    const adversaire = document.getElementById('pokemon-adversaire');
    const joueur = document.getElementById('pokemon-joueur');

    // Animation du Pokémon adversaire
    adversaire.classList.add('attaque-adversaire');

    // Retirer l'animation après son exécution
    adversaire.addEventListener('animationend', () => {
        adversaire.classList.remove('attaque-adversaire');
    });

    // Animation du Pokémon du joueur avec un léger délai
    setTimeout(() => {
        joueur.classList.add('degats-joueur');
    }, 250);

    // Retirer l'animation après son exécution
    joueur.addEventListener('animationend', () => {
        joueur.classList.remove('degats-joueur');
    });
}

function updateButtonFromJson(index, move, pokemon_hp) {
    let bouton = document.getElementById(`attaque_button${index}`);
    if (!bouton) return;
    if (pokemon_hp <= 0) {
        bouton.disabled = true;
    } else {
        bouton.disabled = false;
    }
    if (move === null) return;
    // Mise à jour des données du bouton
    console.log(move)
    if (!move) {
        bouton.style.display = "btn btn-disabled move-btn w-100";
        bouton.disabled = true;
        bouton.innerHTML = "Libre";
        return;
    }
    bouton.style.display = "btn move-btn w-100 bouton-attaque";
    bouton.style.backgroundColor = move.move_color;


    bouton.dataset.name = move.name;
    bouton.dataset.description = move.description;
    bouton.dataset.power = move.power;
    bouton.dataset.accuracy = move.accuracy;
    bouton.dataset.type = move.move_type;
    bouton.dataset.category = move.move_category;
    bouton.dataset.effect = move.move_effect;
    bouton.innerHTML = move.name;
}
