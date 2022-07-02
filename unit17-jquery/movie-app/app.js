//Contains a form with two inputs for a title and rating along with a button to submit the form.
//When the form is submitted, capture the values for each of the inputs 
//and append them to the DOM along with a button to remove each title and rating from the DOM.
$('#rating-form').on(`submit`, function(e) {
    e.preventDefault();
    let movie = $(`#movie`).val();
    let rating = $(`#rating`).val();

    $(`ul`).append(`<li class="new-rating">` + movie + ` : ` + rating + `<button id="remove-button">Remove Rating</button></li>`);
    $(`input`).val(``);
})

//When the button to remove is clicked, remove each title and rating from the DOM.
$(`#rating-list`).on(`click`,`.new-rating`, function(e) {
    if (e.target !== e.currentTarget) {
        $(e.currentTarget).remove();
    };
});