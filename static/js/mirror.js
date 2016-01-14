$(document).ready(function() {
    updateTime();
});

function updateTime()
{
    var now = moment();

    $(".dayOfWeek").html(now.format('dddd'));
    $(".date").html(now.format('MMMM D'));
    $(".time").html(now.format('h:mm'));
}

setInterval(updateTime, 1000);