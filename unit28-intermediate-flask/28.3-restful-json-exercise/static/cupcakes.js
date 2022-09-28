$(".delete-cupcake").click(deleteCupcake);
const container = $(".cupcakes");

async function deleteCupcake() {
  const id = $(this).data("id");
  await axios.delete(`/api/cupcakes/${id}`);
  alert("deleted");
}

async function getCupcakes() {
  const res = await axios.get(`/api/cupcakes`);
  const cupcakes = res.data.cupcakes;
  console.log(cupcakes);
  addCupcakes(cupcakes);
}

const addCupcakes = (cupcakes) => {
  for (let cupcake of cupcakes) {
    const newLi = document.createElement("li");
    newLi.innerHTML = cupcake.flavor;
    container.append(newLi);
  }
};

getCupcakes();

async function handleForm(e) {
  e.preventDefault();

  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image = $("#image").val();

  await axios.post("/api/cupcakes", {
    flavor,
    rating,
    size,
    image,
  });
}

$(".form").on("submit", handleForm);
