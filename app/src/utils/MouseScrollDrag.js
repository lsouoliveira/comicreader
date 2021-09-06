export default class MouseScrollDrag {
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

	handleMouseDown(e) {
		this.isMouseDown = true;
		this.lastMousePosition = {
			x: e.clientX,
			y: e.clientY
		};
	}

	handleMouseUp() {
		this.isMouseDown = false;
		this.isDragging = false;
	}

	handleMouseMove(e) {
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
		this.isDragging = false;
		this.isMouseDown = false;
	}

}
