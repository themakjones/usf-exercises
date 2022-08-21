const guessForm = $(".guess-form");

guessForm.submit((e) => e.preventDefault());

const input = $(".guess-input").val();

async function checkWord() {
  const res = await axios.get(`/guess?word=${input}`);

  resultMessage(res);
}

const resultMessage = () => {};
