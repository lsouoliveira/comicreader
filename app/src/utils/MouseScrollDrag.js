export default class MouseScrollDrag {
	isEnabled = false
	mouseDown = false
	isDragging = false
	lastMousePosition = {
		x: 0,
		y: 0
	}

	constructor(targetElement) {
		targetElement.addEventListener("mousedown", (e) => {
			this.handleMouseDown(e);
		}, false);

		targetElement.addEventListener("mousemove", (e) => {
			this.handleMouseMove(e);
		}, false);

		targetElement.addEventListener("mouseup", (e) => {
			this.handleMouseUp(e);
		}, false);

		targetElement.addEventListener("mouseleave", () => {
			this.handleMouseLeave();
		}, false);
	}

	setEnabled(isEnabled) {
		this.isEnabled = isEnabled;
	}

	handleMouseDown(e) {
		if(!this.isEnabled) return;

		this.isMouseDown = true;
		this.lastMousePosition = {
			x: e.clientX,
			y: e.clientY
		};
	}

	handleMouseUp() {
		if(!this.isEnabled) return;
		this.isMouseDown = false;
		this.isDragging = false;
	}

	handleMouseMove(e) {
		if(!this.isEnabled) return;
		if(this.isMouseDown) {
			this.isDragging = true;
		}

		const currentMousePosition = {
			x: e.clientX,
			y: e.clientY
		};

		if(this.isDragging) {
			window.scrollBy(
				this.lastMousePosition.x - currentMousePosition.x,
				this.lastMousePosition.y - currentMousePosition.y 
			);
		}

		this.lastMousePosition = currentMousePosition;
	}

	handleMouseLeave() {
		if(!this.isEnabled) return;
		this.isDragging = false;
		this.isMouseDown = false;
	}

}
