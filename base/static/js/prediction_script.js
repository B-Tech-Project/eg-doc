

var inputs = document.getElementById('symptom');
var addButton = document.getElementById('addButton');
var submitButton = document.getElementById('search_submit');

const container = document.getElementById('chipp');
const form1 =  document.getElementById('searchForm');
form1.addEventListener('submit', function(event){
    event.preventDefault();
});

class item{
    constructor(itemName){
        this.createDiv(itemName);
    }
    createDiv(itemName){

        let itemChip = document.createElement('div');
        itemChip.classList.add('chip');

        let deleteButton = document.createElement('span');
        deleteButton.classList.add('deleteButton')
        deleteButton.innerHTML= "&#10006";

        container.appendChild(itemChip);

        itemChip.textContent=itemName;
        itemChip.appendChild(deleteButton);

        deleteButton.addEventListener('click', () => this.remove(itemChip));

    }
    remove(item){
        if(deleteSymptom(item.textContent))
        {
            container.removeChild(item);
        }
    }
}
symptomList = [];

function deleteSymptom(sympt)
{
    sympt.toString();
    var sympt = sympt.slice(0,-1);
    for(var i=0;i<symptomList.length;i++)
    {
        if(symptomList[i] == sympt)
        {
            symptomList.splice(i,1);
            return true;
        }

    }
    return false;
}

function addChips(){

    inputValue = inputs.value;
    if(inputValue.length >= 2 && isUnique(inputValue) || isSymptom(inputValue))
    {
        new item(inputValue);
        symptomList.push(inputValue);
        inputs.value = "";
    }
    else{
        inputs.value = "";
    }
}

function submitSymptoms(){
    if(symptomList.length > 1)
    {
         var user_symptoms_list = JSON.stringify(symptomList)
            $.ajax({
                type:'POST',
                url:"submit/",
                data:{
                    symptom_list:user_symptoms_list,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
                success:showResults,
                dataType:'html'
            });
    }
    else{
        alert("Please add atleast 2 symotoms !!")
    }
}
function showResults(data, TextStatus, jqXHR){
    $('#prediction_results').html(data);
}


function isUnique(val)
{
    for(var i=0;i<symptomList.length;i++)
    {
        if(symptomList[i] == val) {
            alert("This symptom is already added !!");
            inputs.value = '';
            return false
        };
    }
    return true;
}

function isSymptom(sympt){
    for(var i=0;i<symptomList.length;i++)
    if(symptomList[i] == sympt){
        return true;
    }
    return false;
}

addButton.addEventListener('click', addChips);
submitButton.addEventListener('click', submitSymptoms);


$(document).ready(function(){
    $('.disease_info_btn').click(function(){
        disease = document.getElementById('disease_select').value;
        getDiseaseInfo(disease);
    });
});

function getDiseaseInfo(disease){
    var disease_name = JSON.stringify(disease)
    $.ajax({
        type:'POST',
        url:"search/",
        data:{
            disease_name:disease_name,

        },
        success:updateDiseaseInfo,
        dataType:'html'
    });
}

function updateDiseaseInfo(data, TextStatus, jqXHR){
    $('#disease-info').html(data);
}

inputs.addEventListener('keyup',function(e){
    if (e.keyCode === 13) {
    return addChips;
  }
});
