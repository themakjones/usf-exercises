const guessForm = $(".guess-form");

async function checkWord() {
  guessForm.submit((e) => e.preventDefault());

  const input = $(".guess-input").val();
  const res = await axios.get(`/guess?word=${input}`);

  resultMessage(res);
}

const resultMessage = (res) => {
  console.log(res);
};
