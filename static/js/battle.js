function attackPokemon(attackId) {
    console.log(attackId)
    fetch(`/attack/${attackId}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"}
    })
        .then(response => response.json())  // Récupère la réponse en JSON
        .then(data => {
            // update data displayed
            // if data[0] is true the player attacked first
            // if data[0] is false the opponent attacked first
            if (data[0]) {
                // player attacked first
                attaquePlayer()
                update_display_pokemon(data[2], 'op')
                // wait 2 seconds before updating the opponent
                setTimeout(() => {
                    attaqueAdversaire()
                    update_display_pokemon(data[1])
                }, 2000)
            } else {
                // opponent attacked first
                attaqueAdversaire()
                update_display_pokemon(data[1])
                // wait 2 seconds before updating the player
                setTimeout(() => {
                    attaquePlayer()
                    update_display_pokemon(data[2], 'op')
                }, 2000)
            }
        })
        .catch(error => console.error("Erreur:", error));
}

function forfet() {
    // forfeit and return a redirect to new page
    fetch(`/forfeit`, {
        method: "POST",
        headers: {"Content-Type": "application/json"}
    }) // response is a redirect
        .then(response => response.json())  // Convertit la réponse en JSON
        .then(data => {
            if (data.redirect) {
                window.location.href = data.redirect;  // Redirige vers la page cible
            } else {
                console.log("Action réussie, mais pas de redirection.");
            }
        })
        .catch(error => console.error("Erreur:", error));

}

function update_display_pokemon(pokemonJson, player = 'self') {
    const first_type = document.getElementById('pokemon_' + player + '_first_type');
    const second_type = document.getElementById('pokemon_' + player + '_second_type');
    const level = document.getElementById('pokemon_' + player + '_level');
    const health = document.getElementById('pokemon_display_' + player + '_hp_text');
    const sprite = document.getElementById('pokemon_' + player + '_sprite');
    const name = document.getElementById('pokemon_' + player + '_name');
    const status = document.getElementById('pokemon_' + player + '_status');
    const hp_bar = document.getElementById('pokemon_' + player + '_hp_bar');

    // Met à jour le nom
    name.innerText = pokemonJson.name;

    // Met à jour le sprite de l'image
    sprite.src = pokemonJson.sprite_url;
    sprite.alt = pokemonJson.name;

    // Met à jour le niveau
    level.innerText = `Lv. ${pokemonJson.level}`;

    // Met à jour le statut
    status.innerText = pokemonJson.status;

    // Met à jour les types de Pokémon
    if (pokemonJson.first_type) {
        first_type.src = pokemonJson.first_type;
        first_type.style.display = 'inline'; // Si un premier type existe, on l'affiche
    } else {
        first_type.style.display = 'none'; // Masque le premier type s'il est absent
    }

    if (pokemonJson.second_type) {
        second_type.src = pokemonJson.second_type;
        second_type.style.display = 'inline'; // Si un deuxième type existe, on l'affiche
    } else {
        second_type.style.display = 'none'; // Masque le deuxième type s'il est absent
    }

    // Met à jour la barre de vie (HP)
    const hpPercentage = (pokemonJson.hp_current / pokemonJson.hp_max) * 100;
    hp_bar.style.width = `${hpPercentage}%`;

    // Modifie la couleur de la barre de vie en fonction de la santé
    if (hpPercentage > 50) {
        hp_bar.style.backgroundColor = '#4CAF50'; // Vert
    } else if (hpPercentage > 20) {
        hp_bar.style.backgroundColor = '#FF9800'; // Orange
    } else {
        hp_bar.style.backgroundColor = '#F44336'; // Rouge
    }

    // Met à jour le texte des HP
    health.innerText = `HP: ${pokemonJson.hp_current} / ${pokemonJson.hp_max}`;
}
