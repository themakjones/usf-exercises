const noImg = ` https://tinyurl.com/tv-missing`;
async function searchShows(query) {
  // TODO: Make an ajax request to the searchShows api.
  const res = await axios.get(`http://api.tvmaze.com/search/shows`, {
    params: { q: query },
  });

  const resArr = res.data.map(function (val) {
    let info = val.show;
    return {
      id: info.id,
      name: info.name,
      summary: info.summary,
      image: info.image.medium ? info.image.medium : noImg,
    };
  });
  return resArr;
}

function populateShows(shows) {
  const $showsList = $("#shows-list");
  $showsList.empty();

  for (let show of shows) {
    let $item = $(
      `<div class="col-md-6 col-lg-3 Show" data-show-id="${show.id}">
         <div class="card" data-show-id="${show.id}">
           <div class="card-body">
             <h5 class="card-title">${show.name}</h5>
             <p class="card-text">${show.summary}</p>
             <img class="card-img-top" src="${show.image}">
           </div>
           <button class="episode-btn" type="button">See All Episodes</button>
         </div>
       </div>
      `
    );

    $showsList.append($item);
  }
}

$("#search-form").on("submit", async function handleSearch(evt) {
  evt.preventDefault();

  let query = $("#search-query").val();
  if (!query) return;

  $("#episodes-area").hide();

  let shows = await searchShows(query);

  populateShows(shows);
});

async function getEpisodes(id) {
  const res = await axios.get(`https://api.tvmaze.com/shows/${id}/episodes`);

  const episodeArr = res.data.map(function (val) {
    return {
      name: val.name,
      number: val.number,
      season: val.season,
    };
  });
  return episodeArr;
}

$(`#shows-list`).on(`click`, `.episode-btn`, async function (e) {
  const showId = e.target.parentElement.dataset.showId;
  $(`#episodes-area`).css(`display`, ``);

  let episodes = await getEpisodes(showId);
  populateEpisodes(episodes);
});

const populateEpisodes = (episodes) => {
  const $episodesList = $(`#episodes-list`);
  $episodesList.empty();

  for (let episode of episodes) {
    let $item = `<li>${episode.name} (Season ${episode.season}, Episode ${episode.number})</li>`;

    $episodesList.append($item);
  }
};
