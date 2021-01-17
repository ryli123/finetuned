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

			//if (this.files && this.files.length > 1)
			//	fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
			//else
			//	fileName = e.target.value.split('\\').pop();

			//if (fileName)
			//	label.innerHTML = fileName;
			//else
			//	label.innerHTML = labelVal;
		});

	});
};

// Attach event listener for when page is loaded
document.addEventListener("DOMContentLoaded", onLoad);