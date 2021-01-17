function onLoad (){
	var inputs = document.querySelectorAll('.inputfile');
	Array.prototype.forEach.call(inputs, function (input) {
		var label = document.getElementById("file-label")
			labelVal = label.innerHTML;

		input.addEventListener('change', function (e) {
			var fileName = '';

			if (this.files) {
				for (let i = 0; i < this.files.length; i++) {
					val = this.files[i]["name"]
					fileName = fileName + val + ", ";
                }
            }

			label.innerHTML = fileName;

		});

	});
};

// Attach event listener for when page is loaded
document.addEventListener("DOMContentLoaded", onLoad);