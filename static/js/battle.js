function get_battle_log() {
    fetch('/battle_log')
        .then(response => response.json())
        .then(data => {
            if (data !== '') {  // Si le log n'est pas vide
                console.log(data);
                afficherMessage(data);
                setTimeout(get_battle_log, 5000);
            }
        })
        .catch(error => console.error("Erreur:", error));
}

function changePokemonBack(pokemonId) {
    fetch(`/change/${pokemonId}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"}
    })
        .then(response => response.json())  // Convertit la réponse en JSON
        .then(data => {
            modal.classList.remove('show');
            update_display_pokemon(data[0])
            updateButtonFromJson(0, data[0]['first_move'], data[0]['hp_current'])
            updateButtonFromJson(1, data[0]['second_move'], data[0]['hp_current'])
            updateButtonFromJson(2, data[0]['third_move'], data[0]['hp_current'])
            updateButtonFromJson(3, data[0]['fourth_move'], data[0]['hp_current'])
            get_battle_log()
            attaqueAdversaire()
            update_display_pokemon(data[1], 'op')
        })
        .catch(error => console.error("Erreur:", error));
    check_ending()
}

function attackPokemon(attackId) {
    fetch(`/attack/${attackId}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"}
    })
        .then(response => response.json())  // Récupère la réponse en JSON
        .then(data => {
            // update data displayed
            if (data[1]) {
                // player attacked first
                attaquePlayer()
                update_display_pokemon(data[3], 'op')
                get_battle_log()
                if (data[0]) {
                    setTimeout(() => {
                        update_display_pokemon(data[2])
                        check_ending()
                    }, 2000)
                    return
                }
                // wait 2 seconds before updating the opponent
                setTimeout(() => {
                    attaqueAdversaire()
                    update_display_pokemon(data[2])
                    get_battle_log()
                    setTimeout(() => {
                        check_ending()
                    }, 2000)
                }, 4000)
            } else {
                // opponent attacked first
                attaqueAdversaire()
                update_display_pokemon(data[2])
                get_battle_log()
                if (data[0]) {
                    setTimeout(() => {
                        check_ending()
                    }, 2000)

                    return
                }
                // wait 2 seconds before updating the player
                setTimeout(() => {
                    attaquePlayer()
                    update_display_pokemon(data[3], 'op')
                    get_battle_log()
                    setTimeout(() => {
                        check_ending()
                    }, 2000)
                }, 4000)
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
            get_battle_log()
            // Redirige vers la page cible après 5 secondes

            setTimeout(() => {
                if (data.redirect) {
                    window.location.href = data.redirect;  // Redirige vers la page cible
                } else {
                    console.log("Action réussie, mais pas de redirection.");
                }
            }, 5000)
        })
        .catch(error => console.error("Erreur:", error));

}

function check_ending() {
    fetch('/is/winner', {
        method: "PUT",
        headers: {"Content-Type": "application/json"}
    })
        .then(response => response.json())
        .then(data => {
            if (data === false) {
                console.log("Le combat continue...");
            } else if (data === true) {
                // wait 8sec and redirect to  /
                setTimeout(() => {
                    get_battle_log()
                    window.location.href = "/"
                }, 8000)

            } else if (typeof data === "object" && data.name) {
                get_battle_log()
                update_display_pokemon(data, 'op');
            } else {
                get_battle_log()
            }
        })
        .catch(error => console.error("Erreur lors de la vérification du gagnant:", error));
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
    updateButtonFromJson(0, null, pokemonJson.hp_current)
    updateButtonFromJson(1, null, pokemonJson.hp_current)
    updateButtonFromJson(2, null, pokemonJson.hp_current)
    updateButtonFromJson(3, null, pokemonJson.hp_current)
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
