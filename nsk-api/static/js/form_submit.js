const form = document.querySelector("#abstract_input");
const abstract = document.querySelector("#abstract");
const alert_box = document.querySelector("#alert_box");

function submit_abstract_form(){
    text = abstract.value;
    text = text.trim();

    if (text == null || text == "") {
        alert_box.style.removeProperty("display");
    }
    else {
        form.submit();
    }
}