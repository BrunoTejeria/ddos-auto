function _getAttacks() {
    $.ajax({
        url: domain + "request/hub/running/attacks",
        type: "POST",
        data: {},
        success: function (data) {
            var getData = $("#ongoing");
            var itemJSON = {}; // This should be an array to store multiple attacks
            if (data.length > 0) {
                const obj = $.parseJSON(data);
                console.log(obj)
                $("#running").html(parseInt(obj.running_count));
                $("#totalattack").html(parseInt(obj.total_count));
                if (obj.running.length > 0) {
                    for (var i = 0; i < obj.running.length; i++) {
                        var attack = obj.running[i];
                        var opt = $.parseJSON(attack.opt);
                        // Use an object instead of concatenating strings
                        itemJSON.push({
                            "date": formatDate(attack.date),
                            "host": attack.host,
                            "port": opt.port,
                            "method": attack.method,
                            "id": attack.id,
                            "slots": attack.slots,
                        });
                        getTime(attack.id, attack.time, attack.date, attack.old_time);
                    }
                } else {
                    // Push an object to indicate no attacks running
                    itemJSON.push({
                        "message": "no hay ataques corriendo"
                    });
                }
            } else {
                // Push an object to indicate no attacks running
                itemJSON.push({
                    "message": "no hay ataques corriendo"
                });
            }
            // You cannot return data from an asynchronous AJAX call directly.
            // Instead, you can process the retrieved data or trigger a callback.
            processData(itemJSON);
        },
        error: function () {
            // Handle error if AJAX request fails
            handleError();
        }
    });
}

// Function to process retrieved data
function processData(data) {
    // Do something with the retrieved data, such as updating the UI
    console.log(data);
}

// Function to handle errors
function handleError() {
    // Handle error, such as displaying an error message to the user
    console.error("Error fetching attack data.");
}
