const colors = ["#5C5980", "#BB97CA", "#403650", "#73B08B", "#D7CDF5"];
const button = document.getElementById('btn');
const color = document.querySelector(".color");

button.addEventListener('click', function() {
    const randomNumber = getRandomNumber();
    console.log(randomNumber);
    document.body.style.backgroundColor = colors[randomNumber];
    color.textContent = colors[randomNumber];
});

function getRandomNumber() {
    return Math.floor(Math.random()*colors.length);
}