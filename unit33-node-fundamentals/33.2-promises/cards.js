let newDeck = axios.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1");
// let drawCard = `https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`;
let deckId = '';
const drawBttn = document.getElementById('draw-bttn');
const cardContainer = document.getElementById('card-container');


newDeck.then(res => {
    deckId = res.data.deck_id;
});

drawBttn.addEventListener('click', evt => {
    axios.get(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`)
    .then(res => {

        console.log(res.data.cards[0].value, 'of', res.data.cards[0].suit);
        cardContainer.src = res.data.cards[0].images.svg;
    })
});