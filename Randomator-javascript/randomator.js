var mouseX = innerWidth / 2;
var mouseY = innerHeight / 2;
document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

const randomizationFactor = 283429.2391
const seedStart = new Date(2010, 12, 14, 0, 0, 0)

function RandomNumber(seed=new Date(), seedOrigin=seedStart, returnInt=true)
{
    var seedDiff = seed.getMilliseconds() - seedOrigin.getMilliseconds();
    var seedAsMilli = seedDiff;

    var allElements = document.querySelectorAll("body *");
    var elementCount = 0;
    allElements.forEach(() => {
        elementCount++;
    });

    var random = ((seedAsMilli * Math.abs(mouseX * mouseY)) * (elementCount+1)) * randomizationFactor;

    return returnInt ? parseInt(random) : random;
}

function RandomRange(minIncl, maxExcl, returnInt=true)
{
    var randNum = RandomNumber(new Date(), seedStart, returnInt) % maxExcl;
    if(randNum < maxExcl-minIncl) randNum += minIncl;
    return randNum;
}

function RandomChoice(choicesArray)
{
    var rand = RandomRange(0, choicesArray.length);
    return choicesArray[rand];
}

document.addEventListener("mousedown", () => {
    console.log(RandomNumber().toString());
    console.log(RandomRange(20, 100).toString());
    console.log(RandomChoice([4, 8, 12]));
    //console.log(mouseX);
});