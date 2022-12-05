const drawBttn = document.getElementById('draw-bttn');
const cardContainer = document.getElementById('card-container');

const deck = {
    async init() {
        let res = await axios.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1");
        this.deckId = res.data.deck_id;
    },
    async drawCard() {
        let newCard = await axios.get(`https://deckofcardsapi.com/api/deck/${this.deckId}/draw/?count=1`);

        console.log(newCard.data.cards[0].value, 'of', newCard.data.cards[0].suit);
        cardContainer.src = newCard.data.cards[0].images.svg; 
    }
}

window.onload = (event) => {
    deck.init();
};
  
drawBttn.addEventListener('click', deck.drawCard());