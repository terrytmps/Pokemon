function attackPokemon(attackId) {
    console.log(attackId)
    fetch(`/attack/${attackId}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"}
    })
        .then(response => response.json())  // Récupère la réponse en JSON
        .then(data => {
            // update data displayed
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

function update_display_pokemon_self(pokemonJson) {
    const first_type = document.getElementById('pokemon_self_first_type');
    const second_type = document.getElementById('pokemon_self_second_type');
    const level = document.getElementById('pokemon_self_level');
    const health = document.getElementById('pokemon_display_self_hp_text');
    const sprite = document.getElementById('pokemon_self_sprite');
    const name = document.getElementById('pokemon_self_name');
    const status = document.getElementById('pokemon_self_status');
    const hp_bar = document.getElementById('pokemon_self_hp_bar');


}